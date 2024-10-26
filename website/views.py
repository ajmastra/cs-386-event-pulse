from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Event, User
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

    # format date and time for each event to pass into the home.html
    for event in events:
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
    # render event details template
    return render_template('event_details.html', event=event, user=current_user)  


# ROUTING FOR ADDING AN EVENT
@views.route('/add-event', methods=['GET', 'POST'])
def add_event():
    if request.method == 'POST':
        # get the title
        title = request.form.get('event')
        # get the description
        description = request.form.get('description')
        # Get the date
        date_of_event_str = request.form.get('date_of_event')
        # Get the time
        time_of_event_str = request.form.get('time_of_event')
        # Get type of event
        type_of_event = request.form.get('type_of_event')
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
            type_of_event=type_of_event,
            location=location
        )
        # add it to the database
        db.session.add(new_event)
        # commit it to the database
        db.session.commit()

        flash('Event added successfully!', category='success')
        # redirect to home
        return redirect(url_for('views.home'))  
    # render the template
    return render_template('add_event.html', user=current_user)  


# ROUTING FOR VIEWING USER PROFILES
@views.route('/profile/<int:user_id>', methods=['GET'])
@login_required
def view_profile(user_id):
    # Fetch the user by ID
    user_profile = User.query.get_or_404(user_id)
    
    # Check if the profile belongs to the current user
    is_own_profile = current_user.id == user_id
    
    # Render the profile template
    return render_template('profile.html', user_profile=user_profile, is_own_profile=is_own_profile, user=current_user)


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
    if request.method == 'POST':

        tempList = []
        if request.form.get('live-music') == "on":
            tempList.append("live-music")
        if request.form.get('theatre') == "on":
            tempList.append("theatre")
        if request.form.get('community-event') == "on":
            tempList.append("community-event")
        if request.form.get('political-event') == "on":
            tempList.append("political-event")
        
        # lowkey this is a horrible strat but it basically just puts the genres in a long string separated by commas
        tempString = str(tempList).replace('[', "").replace(']', "").replace(' ', "").replace('\'', "")

        current_user.interests = tempString
        db.session.commit() 

        return redirect(url_for('views.home'))  
    return render_template("questionnaire.html", user=current_user)