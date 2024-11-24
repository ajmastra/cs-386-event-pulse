from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy import select, delete, intersect, union_all
from .models import Event, User, Interest, Comment, Like, user_interest, event_interest, users_interested_in_events, follow
from . import db
import json
from datetime import datetime

views = Blueprint('views', __name__)

# ROUTING FOR HOME
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    # grab ALL events from the database
    events = Event.query.all()


    # Add supporting variables for the html
    for event in events:
        event_interests_stmt = (
            select(Interest)
            .join(event_interest, event_interest.c.interest_id == Interest.id)
            .where(event_interest.c.event_id == event.id)
        )

        user_interests_stmt = (
            select(Interest)
            .join(user_interest, user_interest.c.interest_id == Interest.id)
            .where(user_interest.c.user_id == current_user.id)
        )

        not_common_interests_stmt = event_interests_stmt.except_(user_interests_stmt)
        common_interests_stmt = event_interests_stmt.intersect(user_interests_stmt)

        common_interests = db.session.execute(common_interests_stmt)
        not_common_interests = db.session.execute(not_common_interests_stmt)
        
        event.common_interest_names = [interest.name for interest in common_interests]
        event.not_common_interest_names = [interest.name for interest in not_common_interests]

        # format date and time for each event to pass into the home.html
        if event.date_of_event:
            event.formatted_date = event.date_of_event.strftime('%m-%d-%Y')
        else:
            event.formatted_date = 'No date set'

        if event.time_of_event:
            event.formatted_time = event.time_of_event.strftime('%I:%M %p')
        else:
            event.formatted_time = 'No time set'

    # return home template
    return render_template("home.html", user=current_user, events=events)



# ROUTING FOR DELETING EVENT
@views.route('/delete-event', methods=['POST'])
def delete_event():
    event_data = json.loads(request.data)
    event_id = event_data.get('eventId')
    event = Event.query.get_or_404(event_id)

    # Ensure the current user is either the owner or an admin
    if event.user_id != current_user.id and not current_user.is_admin:
        flash('You do not have permission to delete this event.', category='error')
        return jsonify({'success': False}), 403

    # Delete the event if authorized
    db.session.delete(event)
    db.session.commit()
    flash('Event deleted successfully!', category='success')
    return jsonify({'success': True})

# ROUTING FOR EVENT DETAILS PAGE
@views.route('/event/<int:event_id>')
def event_details(event_id):
    # grab the event or show 404 if not found
    event = Event.query.get_or_404(event_id)

    # get string of interests using function
    interest_list = interest_list_str(event)

    # Check if the event is already saved
    if event in current_user.events_interested_in:
        user_interested=True
    else:
        user_interested=False


    # render event details template
    return render_template('event_details.html', event=event, user=current_user, interest_list=interest_list, user_interested=user_interested)

# ROUTING FOR ADDING AN EVENT
@views.route('/add-event', methods=['GET', 'POST'])
@login_required  # Ensure user is logged in
def add_event():
    # Get all potential interest that could be selected for event
    interests = Interest.query.all()

    if request.method == 'POST':
        # Get information from the submitted form:
        # get the title
        title = request.form.get('event')
        # get the description
        description = request.form.get('description')
        # get the date
        date_of_event_str = request.form.get('date_of_event')
        # get the time
        time_of_event_str = request.form.get('time_of_event')
        # Get the location
        location = request.form.get('location')

        # Get selected interest id
        selected_interest_ids = request.form.getlist('interest_ids')

        if not selected_interest_ids:
            flash("Please select at least one event type", category="error")
            return redirect(url_for('views.add_event'))

        print(selected_interest_ids)

         # Combine date and time strings into a single datetime object
        date_of_event = datetime.strptime(date_of_event_str, '%Y-%m-%d')
        time_of_event = datetime.strptime(time_of_event_str, '%H:%M').time()

        # Convert IDs to integers
        selected_interest_ids = [int(interest_id) for interest_id in selected_interest_ids]


        # create the new event, assuming you currently have user authentication
        new_event = Event(
            title=title, 
            description=description, 
            date_of_event=date_of_event,
            time_of_event=time_of_event,
            user_id=current_user.id,  # This is now safe
            location=location
        )
        db.session.add(new_event)
        db.session.commit()

        # add interests to the event
        for new_interest_id in selected_interest_ids:
            db.session.execute(
                event_interest.insert().values(event_id=new_event.id, interest_id=new_interest_id)
            )
        db.session.commit()

        flash('Event added successfully!', category='success')

        # redirect home
        return redirect(url_for('views.home'))
    # render the template
    return render_template('add_event.html', user=current_user, interests=interests)  


# ROUTING FOR VIEWING USER PROFILES
@views.route('/profile/<int:user_id>', methods=['GET', 'POST'])
@login_required
def view_profile(user_id):
    user_profile = User.query.get_or_404(user_id)
    # check if the current user is the owner of the profile page they are currently on
    is_own_profile = current_user.id == user_id

    # fetch incoming requests
    incoming_requests = [
        user for user in User.query.join(follow, follow.c.following_id == User.id)
        .filter(follow.c.follower_id == current_user.id, follow.c.status == 'pending')
    ]

    # fetch sent requests
    sent_requests = [
        user for user in User.query.join(follow, follow.c.follower_id == User.id)
        .filter(follow.c.following_id == current_user.id, follow.c.status == 'pending')
    ]

    # fetch friends for current user
    following_id_query = [
        user for user in User.query.join(follow, follow.c.following_id == User.id)
        .filter(follow.c.follower_id == current_user.id, follow.c.status == 'accepted')
    ]
    follower_id_query = [
        user for user in User.query.join(follow, follow.c.follower_id == User.id)
        .filter(follow.c.following_id == current_user.id, follow.c.status == 'accepted')
    ]
    friends = list( set(following_id_query) | set(follower_id_query) )
    

    # generate interest list for the user profile
    interest_list = ", ".join([interest.name for interest in user_profile.interests])

    ######### FRIEND REQUEST HANDLING #########
    if request.method == 'POST':
        # get action type from form
        action = request.form.get('action')
        # get target user id from the form aka the user who is being interacted with
        target_user_id = request.form.get('target_user_id')
        # get target user, or return error if they were not found in db (failsafe)
        target_user = User.query.get_or_404(target_user_id)

        # if user send request
        if action == 'send_request':

            # insert new row to the follow table with status pending
            db.session.execute(
                follow.insert().values(following_id=current_user.id, follower_id=target_user.id, status='pending')
            )

            # commit change to db
            db.session.commit()

            # flask success message to user
            flash(f"Friend request sent to {target_user.username}.", category='success')

        # if user accepts request
        elif action == 'accept_request':

            # update the follow table to set status to accepted
            db.session.execute(
                follow.update()
                .where(follow.c.following_id == target_user.id, follow.c.follower_id == current_user.id)
                .values(status='accepted')
            )

            #commit to db
            db.session.commit()

            # flash success
            flash(f"Friend request from {target_user.username} accepted!", category='success')

        # if user rejects friend request
        elif action == 'reject_request':

            # delete corresponding row in follow table
            db.session.execute(
                follow.delete()
                .where(follow.c.following_id == target_user.id, follow.c.follower_id == current_user.id)
            )

            # commit to db
            db.session.commit()

            # flash success
            flash(f"Friend request from {target_user.username} rejected.", category='info')

        # return redirect
        return redirect(url_for('views.view_profile', user_id=user_id))

    # return template with following data
    return render_template(
        'profile.html',
        user_profile=user_profile,
        is_own_profile=is_own_profile,
        friends=friends,
        incoming_requests=incoming_requests,
        sent_requests=sent_requests,
        interest_list=interest_list,
        user=current_user 
    )




# ROUTING FOR EDITING USER PROFILE
@views.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    if request.method == 'POST':
        # Get the updated data from the form
        new_email = request.form.get('email')
        new_first_name = request.form.get('first_name')

        

        # Update the current user's data
        current_user.email = new_email
        current_user.first_name = new_first_name

        # Commit the changes to the database
        db.session.commit()

        flash('Profile updated successfully!', category='success')
        return redirect(url_for('views.view_profile', user_id=current_user.id))

    return render_template('edit_profile.html', user=current_user)


# ROUTING FOR SEARCH
@views.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    query = request.form.get('query')  # Get the search query from the form
    events = []
    users = []

    if query:
        # Search for events by title
        events = Event.query.filter(Event.title.ilike(f'%{query}%')).all()
        
        # Search for users by first name or email
        users = User.query.filter((User.first_name.ilike(f'%{query}%')) | (User.email.ilike(f'%{query}%'))).all()

    return render_template('search.html', user=current_user, events=events, users=users, query=query)


# ROUTING FOR QUESTIONNAIRE
@views.route('/questionnaire', methods=['GET', 'POST'])
@login_required
def questionnaire():
    all_interests = Interest.query.all()

    selected_user_interests_stmt = (
        select(Interest)
        .join(user_interest, user_interest.c.interest_id == Interest.id)
        .where(user_interest.c.user_id == current_user.id)
    )
    selected_user_interests = db.session.execute(selected_user_interests_stmt).scalars().all()

    # make list that makes sure the correc interests are checked
    for cur_interest in all_interests:
        if(cur_interest in selected_user_interests):
            cur_interest.checked = True
        else:
            cur_interest.checked = False

    if request.method == 'POST':
        # Delete all current user interests
        delete_interests_stmt = (
            delete(user_interest)
            .where(user_interest.c.user_id == current_user.id)
        )
        db.session.execute(delete_interests_stmt)

        # add all selected interests
        selected_interests = request.form
        for interest_id in selected_interests:
            db.session.execute(
                user_interest.insert().values(user_id=current_user.id, interest_id=interest_id)
            )
        
        db.session.commit()

        flash('Interests updated successfully!', category='success')

        return redirect(url_for('views.home'))  
    return render_template("questionnaire.html", user=current_user, interests=all_interests)

# ROUTING FOR COMMENTS
@views.route('/add-comment/<int:event_id>', methods=['POST'])
@login_required
def add_comment(event_id):
    content = request.form.get('content')
    if not content:
        flash('Comment cannot be empty!', category='error')
        return redirect(url_for('views.event_details', event_id=event_id))
    
    event = Event.query.get_or_404(event_id)
    new_comment = Comment(content=content, user_id=current_user.id, event_id=event.id)
    db.session.add(new_comment)
    db.session.commit()
    
    flash('Comment added successfully!', category='success')
    return redirect(url_for('views.event_details', event_id=event_id))

# ROUTING FOR SAVING AN EVENT
@views.route('/save_event/<int:event_id>', methods=['POST'])
def save_event(event_id):
    # get the event
    statement = stmt = select(Event).where(Event.id == event_id)
    event = db.session.execute(stmt).scalar()

    event = db.session.execute(statement).scalar()

    # Check if the event is already saved
    if event in current_user.events_interested_in:
        db.session.execute(
            delete(users_interested_in_events)
            .where(users_interested_in_events.c.event_id == event_id)
            .where(users_interested_in_events.c.user_id == current_user.id)
        )
        db.session.commit()
        flash("Event unsaved!", "success")
    else:
        db.session.execute(
            users_interested_in_events.insert().values(event_id=event_id, user_id=current_user.id)
            )
        db.session.commit()
        flash("Event saved successfully!", "success")


    # Redirect back to the event details page
    return redirect(url_for('views.event_details', event_id=event_id))



@views.route('/delete-comment/<int:comment_id>', methods=['POST'])
@login_required
def delete_comment(comment_id):
    # Fetch the comment by ID or return a 404 if not found
    comment = Comment.query.get_or_404(comment_id)

    # Ensure the current user is either the owner or an admin
    if comment.user_id != current_user.id and not current_user.is_admin:
        flash('You do not have permission to delete this comment.', category='error')
        return redirect(url_for('views.event_details', event_id=comment.event_id))

    # Delete the comment if authorized
    db.session.delete(comment)
    db.session.commit()
    flash('Comment deleted successfully!', category='success')
    return redirect(url_for('views.event_details', event_id=comment.event_id))

# ROUTING FOR SAVED EVENTS
@views.route('/saved_events', methods=['GET', 'POST'])
@login_required
def saved_events():
    # Get events user is interested in
    statement = (
        select(Event)
        .join(users_interested_in_events, users_interested_in_events.c.event_id==Event.id)
        .where(users_interested_in_events.c.user_id==current_user.id)
        )
    events = db.session.execute(statement).scalars().all()

    # Add supporting variables for the html
    for event in events:
        event_interests_stmt = (
            select(Interest)
            .join(event_interest, event_interest.c.interest_id == Interest.id)
            .where(event_interest.c.event_id == event.id)
        )

        user_interests_stmt = (
            select(Interest)
            .join(user_interest, user_interest.c.interest_id == Interest.id)
            .where(user_interest.c.user_id == current_user.id)
        )

        not_common_interests_stmt = event_interests_stmt.except_(user_interests_stmt)
        common_interests_stmt = event_interests_stmt.intersect(user_interests_stmt)

        common_interests = db.session.execute(common_interests_stmt)
        not_common_interests = db.session.execute(not_common_interests_stmt)
        
        event.common_interest_names = [interest.name for interest in common_interests]
        event.not_common_interest_names = [interest.name for interest in not_common_interests]

        # format date and time for each event to pass into the home.html
        if event.date_of_event:
            event.formatted_date = event.date_of_event.strftime('%m-%d-%Y')
        else:
            event.formatted_date = 'No date set'

        if event.time_of_event:
            event.formatted_time = event.time_of_event.strftime('%I:%M %p')
        else:
            event.formatted_time = 'No time set'

    # return home template
    return render_template("saved_events.html", user=current_user, events=events)

# ROUTING FOR FOR YOU PAGE
@views.route('/for-you', methods=['GET'])
@login_required
def for_you():
    # Get user interest id
    user_interest_ids = (
        select(user_interest.c.interest_id)
        .where(user_interest.c.user_id == current_user.id)
    )

    # make a select statment
    statement = (
        select(Event)
        .distinct()
        .join(event_interest, event_interest.c.event_id == Event.id)
        .where(event_interest.c.interest_id.in_(user_interest_ids))
    )

    # Execute the query
    events = db.session.execute(statement).scalars().all()

    #if current_user.interests:
    #    # Split the interests string into a list
    #    user_interests = current_user.interests.split(',')

        # Query events where the type_of_event is in the user's interests
    #    events = Event.query.filter(Event.interests.in_(user_interests)).all()
    #else:
    #    # If the user has no interests set, display no events or a message
    #    events = []

    # Format date and time for each event
    for event in events:
        event_interests_stmt = (
            select(Interest)
            .join(event_interest, event_interest.c.interest_id == Interest.id)
            .where(event_interest.c.event_id == event.id)
        )

        user_interests_stmt = (
            select(Interest)
            .join(user_interest, user_interest.c.interest_id == Interest.id)
            .where(user_interest.c.user_id == current_user.id)
        )

        not_common_interests_stmt = event_interests_stmt.except_(user_interests_stmt)
        common_interests_stmt = event_interests_stmt.intersect(user_interests_stmt)

        common_interests = db.session.execute(common_interests_stmt)
        not_common_interests = db.session.execute(not_common_interests_stmt)
        
        event.common_interest_names = [interest.name for interest in common_interests]
        event.not_common_interest_names = [interest.name for interest in not_common_interests]


        if event.date_of_event:
            event.formatted_date = event.date_of_event.strftime('%m-%d-%Y')
        else:
            event.formatted_date = 'No date set'

        if event.time_of_event:
            event.formatted_time = event.time_of_event.strftime('%I:%M %p')
        else:
            event.formatted_time = 'No time set'

    # Return the For You page template
    return render_template("for_you.html", user=current_user, events=events)

# ROUTING FOR COMMENT LIKES
@views.route('/like-comment/<int:comment_id>', methods=['POST'])
@login_required
def like_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)

    like = Like.query.filter_by(user_id=current_user.id, comment_id=comment_id).first()

    if like:
        db.session.delete(like)
        flash('You unliked this comment.', category='success')

    else:
        new_like = Like(user_id=current_user.id, comment_id=comment_id)
        db.session.add(new_like)
        flash('You liked this comment.', category='success')

    db.session.commit()
    return redirect(url_for('views.event_details', event_id=comment.event_id))

# Create list of interests as a string for easy html rendering
def interest_list_str( obj_with_interests ):
    # start with empty string
    interest_str = ""

    # create an iterator of all the interests
    all_interests_iterator = iter(obj_with_interests.interests)

    # add all interest names to the string
    firstItem = True
    for cur_interest in all_interests_iterator:
        if firstItem:
            firstItem = False
        else:
            interest_str +=  ", "
        
        interest_str += cur_interest.name

    return interest_str

def interest_names_list( obj_with_interests ):
    # start with empty list
    interest_list = []

    # create an iterator of all the interests
    all_interests_iterator = iter(obj_with_interests.interests)

    # add all interest names to the string
    for cur_interest in all_interests_iterator:
        interest_list.append(cur_interest.name)

    print(interest_list)
    return interest_list

# Find common interests between user and events
def common_interests( user_id='', event_id=''):
        common_interests_stmt = (
            select(Interest)
            .join(user_interest, user_interest.c.interest_id == Interest.id)
            .join(event_interest, event_interest.c.interest_id == Interest.id)
            .where(user_interest.c.user_id == user_id)
            .where(event_interest.c.event_id == event_id)
        )

        common_interests = db.session.execute(common_interests_stmt)
        return common_interests