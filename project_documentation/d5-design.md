# D5 - Design

In this deliverable, you should describe the architectural design of your system. Structure your deliverable using the following sections. See the  [Team Project Instructions](https://canvas.nau.edu/courses/29116/pages/team-project-%7C-overview "Team Project | Overview")  for details about formatting. Check the lecture materials and perform additional research to produce a high-quality deliverable. As usual, if you have any questions, let me know.

## 1. Description

The EventPulse application utilizes a few key functionalities. There are account creation/login, user profiles, event posts, and user interests. There is a database for users and events. When users create an account, they are required to use a unique username and password. Once a user is logged into an account, they can access the rest of EventPulse's content. Users can edit their user profile, they can change their email and first name. The user database supports all of the user data. It holds a unique user id, email, username, password, first name, ineterests, and events. The list of interests that each user has can be updated at any time by completing the questionare. The questionare allows users to select which types of events they are interested in. Events are an essential feature of the EventPulse application. The Event database stores data about the event posts, such as location, title, address, etc. When a user creates an event, they are assigned to that event as a creator. Events will also have comments, where users can post comments, and view other's comments on a particular event. Events and users are searchable by their title and first name or email. There are also the coordinator and admin user types. These two user types inherit from the user class, and they have extra functionality. Whenever users create an event post, in order for it to be posted, an admin must review and confirm the event. Coordinators are able to post events without the need for admin review. Coordinators will also be able to show their organization name and position within that orginization on their profile.

## 2. Architecture

![](D5_media/package-diagram.png)

The Event Pulse architecture is built in four layers to keep everything organized. The Presentation Layer is the front end that users interact with; it displays information and handles input through HTML, CSS, and JavaScript. The Application Logic layer manages user actions, such as logging in and navigating the app, making sure each request goes to the right place. The Service Layer contains the core functions, like creating and managing events, applying the app’s main rules and logic. Lastly, the Data Layer stores and retrieves all information in the database, ensuring data is safe and accessible. Each layer only interacts with the one below it, which keeps the system clean and easy to manage.
## 3. Class diagram

Present a refined class diagram of your system, including implementation details such as visibilities, attributes to represent associations, attribute types, return types, parameters, etc. The class diagram should match the code you have produced so far but not be limited to it (e.g., it can contain classes not implemented yet).

The difference between this class diagram and the one you presented in D.3 is that the latter focuses on the domain's conceptual model, while the former reflects the implementation. Therefore, the implementation details are relevant in this case.

![Class Diagram](/project_documentation/D5_media/project_class_diagram.png)

_Grading criteria_ (6 points): Adequate use of UML; Adequate choice of classes and relationships; Completeness of the diagram; Adequate presentation of implementation details.

## 4. Sequence diagram

**Use Case**: Post an Event  
**Actor**: User  
**Trigger**: Goes to the 'add event' page  
**Pre-Conditions**: Must be logged in to post an event.  
**Post-Conditions**: The event feed has a new event post.  

**Scenario**: The user posts an event to the home page.  

- User successfully logs into their account.
- User navigates to the add event page.
- System validates user is logged in.
- The system renders the new event page.
- User posts event.
- The system adds the event to the database.
- The system flashes a success message to the user.
- The post is visible.

**Alternative Scenario**: An unregistered user tries to create a post  
- A user tries to navigate to the add event page.
- The system validates if the user is logged in.
- The system flashes an error message to the user.
- The user signs up for an account and logs in.
- The user navigates to the add event page.
- The system validates that the user is logged in.
- The system renders the new event page.
- User posts event.
- The system adds the event to the database.
- The system flashes a success message to the user.
- The post is visible.

![Sequence Diagram](/project_documentation/D5_media/d5_sequence_diagram.png)

## 5. Design Patterns

### Structural Class: Facade  

![Facade UML Diagram](/project_documentation/D5_media/d5-5-facade-uml.png)  

User: [https://github.com/ajmastra/cs-386-event-pulse/blob/main/website/models.py](https://github.com/ajmastra/cs-386-event-pulse/blob/main/website/models.py)  

Auth: [https://github.com/ajmastra/cs-386-event-pulse/blob/main/website/auth.py](https://github.com/ajmastra/cs-386-event-pulse/blob/main/website/auth.py)  

### Behavioral Class: Observer   

![Observer UML Diagram](/project_documentation/D5_media/d5-5-observer-uml.png)  

User: [https://github.com/ajmastra/cs-386-event-pulse/blob/main/website/models.py](https://github.com/ajmastra/cs-386-event-pulse/blob/main/website/models.py)  
 
Event: [https://github.com/ajmastra/cs-386-event-pulse/blob/main/website/models.py](https://github.com/ajmastra/cs-386-event-pulse/blob/main/website/models.py)  

Views: [https://github.com/ajmastra/cs-386-event-pulse/blob/main/website/views.py](https://github.com/ajmastra/cs-386-event-pulse/blob/main/website/views.py)  

## 6. Design Principles

SCP - Single Responsibility Principle
Our classes are all only used once. An example of this would be in models.py, with our “user” class. The definition of SCP is “a class should have only a single responsibility,” and based on our code we follow this. Our user class is created with the sole purpose of being used to create a full user profile with the different options in it. 

OCP - Open/Closed Principle
Our project follows OCP, with an example being the create event actions. When a user goes to create an event, they are able to use as much detail as possible. However, we don’t let them create their own sections or categories for the information. All their information is tied up into a single form, which they can do whatever they want inside of, but not edit how the form works. With OCP being “software entities ... should be open for extension, but closed for modification,” there is a clear way of extension without modifying the forms completely. 

LSP - Liskov Substitution Principle
We find LSP in our project through the use of interests users can select through the questionnaire. LSP is defined as “objects in a program should be replaceable with instances of their subtypes without altering the correctness of that program.” When filling out the questionnaire, you are selecting your own personal interests. These interests will help us determine what events might interest you the most, but it won’t affect other users’ or the overall program, just that specific user’s end of it. 

ISP - Interface Segregation Principle 
I believe that our project follows ISP, which is that “many client-specific” interfaces are better than one general-purpose interface.” If a user creates an event, only that user is able to edit/delete it. Not every user gets to see the delete event button when viewing the details of events. This makes it so not every user sees the same thing, but the format is very similar. An example of this in the code is the event class in models.py. You can see that there is a user id section, and if the user id matches the current user, that user will be able to edit or delete that event. 

DIP - Dependency Inversion Principle
The DIP is defined as follows: ‘one should “Depend upon Abstractions. Do not depend upon concretions.” Our project uses this with the different routes being used throughout the code, leading to different interfaces. These different interfaces keep our project from violating DIP and keeping the design simplistic in use.
