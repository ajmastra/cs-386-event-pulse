# Requirements

*Group 06*: Event Pulse  
*Date:* 9/29/24  
*Group Members*: Anthony Mastrangelo, Andrew Gajewski, Andrew Sliva, Benjamin Levine, Samuel Butler, Zachary Garza  

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
**Competitors:** Meetup, NAUGo, Instagram, Facebook, [Flagstaff Events Calendar](https://www.flagstaff.com/calendar)  
**Developers:** Our six group members (listed above)  
**Detractors:** Team experience, project deadline (end of semester) 

## 3. Functional Requirements (features)

- Event Title: Title/name of event to attract users.
- Event Location: Location/address of event so users know where to go. 
- Event Time: Time and date of event. 
- Event Description: Field to give more information regarding the event. 
- Interested Button: Button to click if you interested in an event (will trigger notifications feature). 
- Groups: Individuals may join "groupings" of events based off their interests.
- Group Tags: Will be able to select your groups based on if you choose to add a descriptive tag or not. 
- Notifications: Notifications will be sent based off events you have marked as interested in. 
- User Accounts: Users will have an account to use on this site. 
- Authentication: User authentication sent through email to verify users. 
- List of Events: List of events scheduled for users to scroll through. 
- Related Intrest List: List of events related to your intrests instead of all events. 
- User information: Users will sign up with a unique user name and a unique email
- Event Coordinator Contact: This will allow a user to contact the event coordinator if they have problems.


## 4. Non-functional Requirements
- The ability to see reviews about an event is not necessary, it does not show location or other aspects that are mandatory to attend an event.
- The event description is almost necessary, however it doesn't ALWAYS have to be part of an event since some events can be deciphered by just their title.
- Photo attachments to an event aren't necessary, as a title and/or location is good enough to detail the event.

## 4.1. Non-Functional Requirements for Python syntax

 ## **Naming Conventions**

### **Case Naming**
- **Class Names:** PascalCase.
  - Example: `MyClass`, `UserProfile`.
- **Function Names:** snake_case (lowercase words separated by underscores).
  - Example: `get_user_data()`, `calculate_total_price()`.
- **Variable Names:** snake_case (lowercase words separated by underscores).
  - Example: `user_id`, `total_amount`.
- **Constants:** UPPERCASE with words separated by underscores.
  - Example: `MAX_RETRY_LIMIT`, `DEFAULT_TIMEOUT`.

### **File and Module Names**
- Use snake_case for file and module names.
  - Example: `user_service.py`, `data_processor.py`.

### **Package Names**
- Use all lowercase for package names, without underscores if possible.
  - Example: `mypackage`, `utils`.

## 4.2. **Function Design and Structure**

### **Function Length**
- Keep functions short and focused on a single task. A function should ideally not exceed 30 lines of code, excluding documentation and comments.

### **Function Arguments**
- Limit the number of function arguments to 5 or fewer. If more parameters are needed, consider using a dictionary or an object.

### **Return Values**
- Ensure functions have a single, clear return path whenever possible.

## 4.3. **Code Formatting**

### **Indentation**
- Use **4 spaces** per indentation level (no tabs).

### **Line Length**
- Limit all lines to a maximum of **79 characters**.

### **Blank Lines**
- Use blank lines to separate functions and class definitions.
- Two blank lines between top-level functions and class definitions.
- One blank line between methods within a class.

### **Imports**
- Imports should be on separate lines and grouped as follows:
  1. Standard library imports.
  2. Third-party imports.
  3. Local application/library imports.
  
Example:
```python
import os
import sys

import requests

from myproject.module import MyClass
```

## 5. MVP
- We will have a user authenication system for users to sign up through email. This will be validated by having actual users try to sign up for an account through our web portal.
- Upon sign up, users will be able to add themselves to various groups of interests for the sake of recieving SMS notifications. This will be tested via implementation, ensuring that the prototype users recieve the correct notifications, and not one thats are unrelated to the interests they selected. For example, users can select tags to assign themselves to these interests.
- There will be an event homescreen that users can scroll through, seeing all of the events in their area, and a curated list of the events that are pertaining to their selected interests. This will be testing during the prototyping phase, to ensure that all of the interests for events are being properly registered.

## 6. Use Cases

### 6.1 Use Case Diagram:
![UML Diagram](/project_documentation/D2_media/UML.jpg)

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
<img src="/project_documentation/D2_media/singup.png" width=200>

**Use case**: Mark Interest in Event  
**Actor**: App User  
**Decription:** User will select an event within the app, and mark that they are interested in attending the event.  
**Preconditions:** User has downloaded the *Event Pulse* app and setup an account that they are currently logged into.  
**Postconditions:** User will now receieve notifications regarding this event.  
**Main Flow:**
1. User selects an event that they are interested in.
2. User expresses interest in a particular event.
3. User is now enrolled in push notification for this event, should anything change.
<img src="/project_documentation/D2_media/interest_in_event.png" width=200>

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
<img src="/project_documentation/D2_media/posting_an_event.png" width=200>


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
<img src="/project_documentation/D2_media/event_approval.png" width=200>


## 7. User Stories

**Priority Scale**: 1-5. 1 being highest priority, 5 being the lowest.   
**Time Estimation Units:** Hours.   

**User Story 1:** As a person who attends lot of events, I want to be notified of new events I'd be interested so that I don't have to spend time searching for them.    
**Priority:**: 4
**Time Estimation:** 5 

**User Story 2:** As a person is interested in attending new events, I want to know how and if other attendees enjoyed the event so that I can decide better if I want to go or not.  
**Priority:**: 4
**Time Estimation:** 5 

**User Story 3:** As a new user, I want to register an account, so that I can add friends and utilize full functionality.  
**Priority:**: 1
**Time Estimation:** 8 

**User Story 4:** As a new user, I want to be added to certain event group tags, so that I can get notifications specifically for the categories of events I am interested in.  
**Priority:**: 3
**Time Estimation:** 5 

**User Story 5:** As a community member, I want to join and follow groups of interest to receive updates on relevant events and friend activity, so I can stay informed and engaged without actively searching.  
**Priority:** 2
**Time Estimation:** 5 

**User Story 6:** As an event organizer, I want to publish events to relevant groups so that I can reach a targeted audience and ensure community members are aware of activities they might be interested in.  
**Priority:** 4
**Time Estimation:** 5  

**User Story 7:** As a college student, I want to see what my friends are doing so that I can interact with them more on a daily basis.  
**Priority:**: 1
**Time Estimation:** 8 

**User Story 8:** As a new user, I want to see what events are in my area so that I can learn more about the community I'm in.  
**Priority:**: 5
**Time Estimation:** 5

**User Story 9:** As an event planner, I want my notifications to be sent to users so that interested users will be alerted of our events.  
**Priority:**: 5
**Time Estimation:** 3 

**User Story 10:** As a user signing up for events, I want notifications for the events I choose to be interested in so that I can have a reminder before I miss an event.  
**Priority:** 2
**Time Estimation:** 3 

**User Story 11:** As an admin monitoring user event submissions, I want to easily view events submitted for approval on any device of my choosing so I can be as efficient as possible.  
**Priority:** 5  
**Time Estimation:** 5  

**User Story 12:** As an admin verifying the validity of event coordinators, I want to be able to see all of the user's information on the screen at once, so I can easily tell if they are a legitamate source.    
**Priority:** 5   
**Time Estimation:** 2  



## 8. Github Issues Tracker:

**View Our Issues Tracker [Here!](https://github.com/ajmastra/cs-386-event-pulse/issues)**

![Issue Tracker](/project_documentation/D2_media/issue_tracker.png)
