from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Event
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
        
        # Combine date and time strings into a single datetime object
        date_of_event = datetime.strptime(date_of_event_str, '%Y-%m-%d')
        time_of_event = datetime.strptime(time_of_event_str, '%H:%M').time()  # Get only the time part
        # create the new event, assuming you currently have user authentication
        new_event = Event(
            title=title, 
            description=description, 
            date_of_event=date_of_event,
            time_of_event=time_of_event,
            user_id=current_user.id
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
