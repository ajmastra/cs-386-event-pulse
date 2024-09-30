# Requirements

*Group 06*: Event Pulse  
*Date:* 9/29/24  
*Group Members*:  

## 1. Positioning

### 1.1 Problem Statement

The problem of not attending NAU and flagstaff events affects NAU students and Flagstaff residents, the impact of which is not making friends, and missing out on valuable memories and being a part of the community.  

### 1.2 Product Position Statement

For NAU students and Flagstaff residents who want to attend more events, make friends, and interact with their community, EventPulse is an app that gives users a platform to explore events and find groups of similar people to attend and discuss events. Unlike NAU event tracker, our product not only notifies users of events, but helps connect people, supports event organizers, and overall provides an all-in-one space to interact with events and the community.

### 1.3 Value Proposition and Customer Segment

Value Proposition: EventPulse is an event tracker app that provides NAU students and Flagstaff residents with an all in one place to explore local events, find groups of similar people, and discuss events. 
Customer Segment: NAU students, and Flagstaff residents looking to make friends and interact with the community.

## 2. Stakeholders

**Users:** NAU Students, Event Organizers, Promoters, Community Active Locals, Tourists  
**Comptetitors:** Meetup, NAUGo, Instagram, Facebook, [Flagstaff Events Calendar](https://www.flagstaff.com/calendar)  
**Developers:** Our six group members (listed above)  
**Detractors:** Team experience, project deadline (end of semester) 

## 3. Functional Requirements (features)

- one
- two
- three

## 4. Non-functional Requirements
- The ability to see reviews about an event is not necessary, it does not show location or other aspects that are mandatory to attend an event.
- The event description is almost necessary, however it doesn't ALWAYS have to be part of an event since some events can be deciphered by just their title.
- Photo attachments to an event aren't necessary, as a title and/or location is good enough to detail the event.

## 5. MVP
- We will have a user authenication system for users to sign up through email. This will be validated by having actual users try to sign up for an account through our web portal.
- Upon sign up, users will be able to add themselves to various groups of interests for the sake of recieving SMS notifications. This will be tested via implementation, ensuring that the prototype users recieve the correct notifications, and not one thats are unrelated to the interests they selected. For example, users can select tags to assign themselves to these interests.
- There will be an event homescreen that users can scroll through, seeing all of the events in their area, and a curated list of the events that are pertaining to their selected interests. This will be testing during the prototyping phase, to ensure that all of the interests for events are being properly registered.

## 6. Use Cases

### 6.1 Use Case Diagram:

![UML Diagram](\D2_media\UML.jpg)

### 6.2 Use Case Decriptions

**Use case**: Sign up For Account  
**Actor**: App User  
**Decription:** User sets up an account with an email address in order to utilize the application.  
**Preconditions:**  User has downloaded the app, and has an email account.  
**Postconditions:** The user now has an account setup for *Event Pulse*.
**Main Flow:**
1. User opens the app that they have now downloaded.
2. User selects signup.
3. User enters name, email address, and password for account setup.
**Alternative Flow**: 
1. User already has an account.
2. User opens the app
3. User selects "Login" on the home screen.
4. User enters their account email and password to sign-in to their account.
![Sign Up UI](\D2_media\signup.png)

**Use case**: Mark Interest in Event  
**Actor**: App User  
**Decription:** User will select an event within the app, and mark that they are interested in attending the event.  
**Preconditions:** User has downloaded the *Event Pulse* app and setup an account that they are currently logged into.  
**Postconditions:** User will now receieve notifications regarding this event.
**Main Flow:**
1. User selects an event that they are interested in.
2. User expresses interest in a particular event.
3. User is now enrolled in push notification for this event, should anything change.
![Interest in Event UI](\D2_media\interest_in_event.png)

**Use case**: Posting an Event  
**Actor**: Event Coordinator  
**Decription:** Event coordinator user posts an event to the app, where it is immediately verified and sent to the events page.  
**Preconditions:** User is a verified Event Coordinator within the app and is currently signed in.  
**Postconditions:** The event is posted to the events page within the app.  
**Main Flow:**
1. User selects "Add an Event" on the events page.
2. User enters the information of the event: name, date, time, and place.
3. User selects the "Submit button".
4. The event is posted to the events page within the app.
![Posting An Event UI](\D2_media\posting_an_event.png)

**Use case**: Approve / Deny Event Post  
**Actor**: Admin  
**Decription:** Every time an event is added from a non-Event Coordinator user, the admin receives a notification in order to approve the event.  
**Preconditions:** User is an *Event Pulse* admin and is on either the mobile app or web admin view.  
**Postconditions:** Event is either approved or rejected, and user that posted the event is notified of the status.  
**Main Flow:**
1. Non event coordinator user posts an event.
2. Admin is notified of the event.
3. Admin goes to the event in the app or web view, and verifies the details of the event ensuring the legitimacy.
4. Admin approves the event and the user that posted it is notified of the status.
**Alternative Flows:**
4. Admin denies the event and the user that posted it is notified of the status.
![Event Approval UI](\D2_media\event_approval.png)


## 7. User Stories

**User Story 1:** As a person who attends lot of events, I want to be notified of new events I'd be interested so that I don't have to spend time searching for them.  Priority: ??? Time Estimation: ???

**User Story 2:** As a person is interested in attending new events, I want to know how and if other attendees enjoyed the event so that I can decide better if I want to go or not.  Priority: ??? Time Estimation: ???

**User Story 3:** As a new user, I want to register an account, so that I can add friends and utilize full functionality. Priority: ??? Time Estimation: ???

**User Story 4:** As a new user, I want to be added to certain event group tags, so that I can get notifications specifically for the categories of events I am interested in. Priority: ??? Time Estimation: ???

**User Story 5:** As a community member, I want to join and follow groups of interest to receive updates on relevant events and friend activity, so I can stay informed and engaged without actively searching.
Priority ??? Time Estimation: ???

**User Story 6:** As an event organizer, I want to publish events to relevant groups so that I can reach a targeted audience and ensure community members are aware of activities they might be interested in. Priority ??? Time Estimation: ???

**User Story 7:** As a college student, I want to see what my friends are doing so that I can interact with them more on a daily basis. Priority: ??? Time Estimation: ???

**User Story 8:** As a new user, I want to see what events are in my area so that I can learn more about the community I'm in. Priority: ??? Time Estimation: ???


## 8. Github Issues Tracker:


