# D7 - Validation
## 1. Description  
The EventPulse application utilizes a few key functionalities. There are account creation/login, user profiles, event posts, and user interests. There is a database for users and events. When users create an account, they are required to use a unique username and password. Once a user is logged into an account, they can access the rest of EventPulse's content. Users can edit their user profile, they can change their email and first name. The user database supports all of the user data. It holds a unique user id, email, username, password, first name, ineterests, and events. The list of interests that each user has can be updated at any time by completing the questionare. The questionare allows users to select which types of events they are interested in. Events are an essential feature of the EventPulse application. The Event database stores data about the event posts, such as location, title, address, etc. When a user creates an event, they are assigned to that event as a creator. Events will also have comments, where users can post comments, and view other's comments on a particular event. Events and users are searchable by their title and first name or email. There are also the coordinator and admin user types. These two user types inherit from the user class, and they have extra functionality. Whenever users create an event post, in order for it to be posted, an admin must review and confirm the event. Coordinators are able to post events without the need for admin review. Coordinators will also be able to show their organization name and position within that orginization on their profile.  

<hr>

## Validation
### Script

**Tasks for the user to do**  
1. Create account
2. Fill out questionairre interests
3. Post an event
4. Comment on existing event
5. Like a comment
6. Delete a comment
7. Delete an event
8. Edit profile
9. Send a friend request

**Data collected**  
1. Time taken to complete each quest.
2. Completion of tasks without assistance.
3. User satisfaction for each feature tested.

**Questions we Asked**  
1. What did you think of the login process?
2. Do you like the way you tag events you are interested in?
3. What would you improve?
4. Did anything feel clunky?
5. What does this site have that other event sites lack?
6. What does this site lack that other event sites have?

## Results

**User 1**: Nate Grimshaw
- **Task Completetion Times:**
  - Create an Account: 1 minunte
  - Fill out Questionairre: 15 seconds
  - Post an Event: 50 seconds
  - Comment on event: 20 seconds
  - Like a Commment: 15 seconds
  - Delete a Comment: 10 seconds
  - Delete an Event: 25 seconds
  - Edit profile: 20 seconds
  - Send a friend request: 1.5 minutes
- **Success Rate**: 90%
- **Feedback / Answers to Questions:**
  - UI Description: Fairly simple and intuitive, but seems dated.
  - Ease of creating an Event: Simple to understand, thought there should be an add event button in the navigation bar.
  - Missing / needed features: Profile pictures would be nice, and maybe a way to filter the events on the home page.
- **Ratings (Scale 1-10):**
  - User Interface: 6
  - Ease of use: 9
  - Liklihood of use in day to day: 5
 
**User 2**: Conrad Lis
- **Task Completetion Times:**
  - Create an Account: 45 seconds
  - Fill out Questionairre: 15 seconds
  - Post an Event: 40 seconds
  - Comment on event: 15 seconds
  - Like a Commment: 10 seconds
  - Delete a Comment: 10 seconds
  - Delete an Event: 15 seconds
  - Edit profile: 20 seconds
  - Send a friend request: 30 seconds
- **Success Rate**: 88%
- **Feedback / Answers to Questions:**
  - UI Description: Simple and clean, it navigates pretty well.
  - Ease of creating an Event: Very simple and easy to understand. Picking the time for the event is a little clunky.
  - Missing / needed features: Profile pictures or event pictures would be nice for visuals.
- **Ratings (Scale 1-10):**
  - User Interface: 7
  - Ease of use: 8
  - Liklihood of use in day to day: 6
 
**User 3**: William Aft   
- **Task Completetion Times:**
  - Create an Account: 30 seconds  
  - Fill out Questionairre: 10 seconds  
  - Post an Event: 35 seconds  
  - Comment on event: 20 seconds
  - Like a Commment: 5 seconds
  - Delete a Comment: 10 seconds  
  - Delete an Event: 15 seconds  
  - Edit profile: 30 seconds   
  - Send a friend request: 20 seconds   
- **Success Rate**: 95%
- **Feedback / Answers to Questions:**
  - UI Description: Everythig easy to navigate, makes sense where things are placed.  
  - Ease of creating an Event: Easy to understand, might take too long.    
  - Missing / needed features: Notifications for friend requests.    
- **Ratings (Scale 1-10):**
  - User Interface: 9  
  - Ease of use: 8  
  - Liklihood of use in day to day: 7  

## Reflections 

**What worked well:**  The core functionalities, such as creating an account, posting events, commenting, and liking were all deemed intuitive and were completed by the users with relative ease. Users appreciated the simplicity and clarity that the user interface provided, especially in regards to the navigation. The event creation process was deemed to be simple and understandable by all users. The time to complete tasks was also relatively low, indicating a user-friendly expereince for most of our core features.

**What can be changed:**  Multiple users noted that the design looked fairly dated, so an updated and more modernized interface could likely improve user satisfaction. 
**Feature Enhancements**:
- Add profile pictures and event images to improve visual appeal.
- Implement a filtering system on the home page to improve usability for users.
- Look into adding an "Add event" button to the navigation bar.
- Notifications for friend requests could be an engaging addition to the user page.
- Sending friend requests took a lot longer for users than we expected, so streamlining this process would improve task performance.

**Learning Curve:**  
The learning curve was minimal for all users, which was reflected in their ability to complete tasks quickly and successfully. Navigation was intuitive, and taks were clear in their purpose and execution. This suggests that the system's design effectively supports first time users. However, improvements could further enhance long-term engagement with users.  

**Task Performance:**  
Task completetion times for most actions were below a minute, indicating a fairly efficient design. Although, some actions such as sending a friend request took longer than expected for some users (1.5 minutes for User 1). Success rates were slightly varied, with one user achieving 88% and another achieving 95%. This coudl indicate minor issues or confusion in certain tasks. Event creation and profile editing were very straight for all users. Deleting comments and events were also executed quickly and efficiently.

**User Preferences:**
- *What did the users like the most?*
   - Simple navigation and clean layout.
   - Event creation was seen as easy to understand by all users.
   - Users praised the placement of key features.
   - Quick access to editing profiles and interacting with events (liking, commenting, etc)
- *Was the value proposition accomplished?*
   - For the most part. While users did indeed find the core features functional and intuitive, several of them expressed a want for added visuals, through the use of profile and event pictures, as well as filtering options. These suggestions are key to improving the overall usability. Additionally, adding some more modern design elements and addressing clunky workflows would allow our web app to better align with user expectations as an app to be used daily.

