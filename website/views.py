from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Event
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        event = request.form.get('event')

        if len(event) < 1:
            flash('Event is too short!', category='error')
        else:
            new_event = Event(title=event, user_id=current_user.id)
            db.session.add(new_event)
            db.session.commit()
            flash('Event Added!', category='success')
    return render_template("home.html", user=current_user)


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