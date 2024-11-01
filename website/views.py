from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy import select
from .models import Event, User, Interest
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
        # format the interest list as a string for each event
        event.interest_list = interest_list_str(event)

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
    event = json.loads(request.data)
    eventId = event['eventId']
    event = Event.query.get(eventId)

    if event:
        if event.user_id == current_user.id:
            db.session.delete(event)
            db.session.commit()
    return jsonify({})

# ROUTING FOR EVENT DETAILS PAGE
@views.route('/event/<int:event_id>')
def event_details(event_id):
    # grab the event or show 404 if not found
    event = Event.query.get_or_404(event_id)

    # get string of interests using function
    # !! not checking if a 404 was returned, not sure how to handle this gracefully
    interest_list = interest_list_str(event)

    # render event details template
    return render_template('event_details.html', event=event, user=current_user, interest_list=interest_list)  


# ROUTING FOR ADDING AN EVENT
@views.route('/add-event', methods=['GET', 'POST'])
def add_event():
    # Get all potential interest that could be selected for event
    interests = Interest.query.all()

    if request.method == 'POST':
        # Get information from the submitted form:
        # get the title
        title = request.form.get('event')
        # get the description
        description = request.form.get('description')
        # Get the date
        date_of_event_str = request.form.get('date_of_event')
        # Get the time
        time_of_event_str = request.form.get('time_of_event')
        # Get selected interest id
        selected_interest_id = request.form.get('type_of_event')
        # Get the location
        location = request.form.get('location')

        # Combine date and time strings into a single datetime object
        date_of_event = datetime.strptime(date_of_event_str, '%Y-%m-%d')
        time_of_event = datetime.strptime(time_of_event_str, '%H:%M').time()  # Get only the time part
        # create the new event, assuming you currently have user authentication
        new_event = Event(
            title=title, 
            description=description, 
            date_of_event=date_of_event,
            time_of_event=time_of_event,
            user_id=current_user.id, 
            location=location
        )
        # Add the interest selected
        new_interest_to_add = Interest.query.get(selected_interest_id)
        new_event.interests.append(new_interest_to_add)

        # add it to the database
        db.session.add(new_event)
        # commit it to the database
        db.session.commit()

        flash('Event added successfully!', category='success')
        # redirect to home
        return redirect(url_for('views.home'))  
    # render the template
    return render_template('add_event.html', user=current_user, interests=interests)  


# ROUTING FOR VIEWING USER PROFILES
@views.route('/profile/<int:user_id>', methods=['GET'])
@login_required
def view_profile(user_id):
    # Fetch the user by ID
    user_profile = User.query.get_or_404(user_id)

    # Create list of user's interests
    interest_list = interest_list_str(user_profile)

    # Check if the profile belongs to the current user
    is_own_profile = current_user.id == user_id
    
    # Render the profile template
    return render_template(
        'profile.html', 
        user_profile=user_profile,
        is_own_profile=is_own_profile,
        user=current_user,
        interest_list=interest_list)


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

# ROUTING FOR INTERESTS
@views.route('/interests', methods=['GET', 'POST'])
@login_required
def interests():
    query = request.form.get('query')  # Get the search query from the form
    interests = Interest.query.all()

    if query is not None:
        # Search for interest by name
       interests = Interest.query.filter ( Interest.name.ilike(f'%{query}%') ).all()

    return render_template('interests.html', user=current_user, interests=interests, query=query)

# ROUTING FOR NEW INTEREST
@views.route('/new_interest', methods=['GET', 'POST'])
@login_required
def new_interest():
    # Test queries
    # First, create a new query statement, we'll use the select statment here
    statement = select(User, Interest).join(Interest.users)
    # Now execute the statment and print the results
    for row in db.session.execute( statement ):
        print( f" User ID and Username { row.User.id }, { row.User.username }, Interest ID and Name: { row.Interest.id }, { row.Interest.name }")

    interests = Interest.query.all()

    if request.method == 'POST':
        new_interest_name = request.form.get('new_interest_name')  # get the potentially filled in interest field
        print("new_interest_name: " + str(new_interest_name))
        if new_interest_name:
            # Add new interest
            print("Adding new interest...")
            new_interest = Interest( name=new_interest_name )
            db.session.add( new_interest )
            db.session.commit()

    return render_template('new_interest.html', user=current_user, interests=interests)

# ROUTING FOR QUESTIONNAIRE
@views.route('/questionnaire', methods=['GET', 'POST'])
@login_required
def questionnaire():

    # This need to be moved to a different location, only needs to be run once, tried putting it in __init__ but I
    # was running into errors.
    def default_interests():
        # List of default interests, if changing this you may want to reset db as the old defaults will likely remain
        list = ("Live Music", "Theatre", "Political Event", "Community Events" )

        # Tracker for if a new Interest is added to the db
        new_interest_added = False;
        # Go through default list and add them to the db if not already added
        for interest_name in list:
            query_result = Interest.query.filter_by(name = interest_name).first()
            if query_result is None:
                new_interest_added = True
                new_interest = Interest( name=interest_name )
                db.session.add( new_interest )
            
        # Commit any changes to database if a new Interest is added to the db
        if new_interest_added:
            db.session.commit()

    # create some default interests if they aren't already present
    default_interests()

    interests = Interest.query.all()
    
    if request.method == 'POST':
        selected_interests = request.form
        for interest_id in selected_interests:
            interest_to_add = Interest.query.get(interest_id)
            current_user.interests.append(interest_to_add)
    
        # Commit changes to db
        db.session.commit()

        return redirect(url_for('views.home'))  
    return render_template("questionnaire.html", user=current_user, interests=interests)

# Extra function to avoid redundancy

# Create list of interests as a string for easy html rendering
def interest_list_str( obj_with_interests ):
    # Create list of user's interests

    # start with empty string
    interest_str = ""

    # create an iterator of all the interests
    all_interests_iterator = iter(obj_with_interests.interests)

    # add the first item to the string
    cur_interest = next(all_interests_iterator)
    interest_str += cur_interest.name

    # now add the remaining items to the string  
    for cur_interest in all_interests_iterator:
        interest_str +=  ", " + cur_interest.name

    return interest_str