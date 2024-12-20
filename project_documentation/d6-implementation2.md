# Implementation 2  

## 1. Introduction
EventPulse is an event tracker app that provides NAU students and Flagstaff residents with an all in one place to share and discover local events, find groups of similar people, and discuss events.

EventPulse was created out of a desire to connect people, provding a streamlined for events to be broadcast and discovered. The main "Events" page follows through on that idea, putting the list of upcoming events front-and-center while also allowing users to jump right in and start sharing their own events. Upon selecting the prominent "Add Event" button, user will be prompted to add details such as the events' title, time, location, and importantly, the type of event. Depending on the "Type of Event" selected by the user it will change the platform interacts with user who have selected that as one of their interests.

Interests, as selected for the user profile via a small questionaire, is the other half that powers another core idea of the platform, the "For You" page. This provides a place for users to find new things to do, pushing events that match the users' interest at the top, lending an unique aspect of discovery to EventPulse. 

Friend and comment systems have also been built in, supporting community building without over-burdening the site in social features. For example, this might allow questions to be answered by event runners and build further connections between users.

[Link to EventPulse on GitHub](https://github.com/ajmastra/cs-386-event-pulse)

## 2. Implemented Requirements  

**Requirement:** *Comments under Events - Allows user to get a feel of the event from the community*  
**Issue:** https://github.com/ajmastra/cs-386-event-pulse/issues/154    
**Pull request:** https://github.com/ajmastra/cs-386-event-pulse/pull/193    
**Implemented by:** Anthony Mastrangelo    
**Approved by:** Andrew Sliva    
**Print screen:**  
![Comments](/project_documentation/D6_media/d6-2-comments.png)  

**Requirement:** *Add Friend Functionality - Allows users to connect with their peers and go to events together*  
**Issue:** https://github.com/ajmastra/cs-386-event-pulse/issues/152     
**Pull request:** https://github.com/ajmastra/cs-386-event-pulse/pull/197    
**Implemented by:** Zachary Garza      
**Approved by:** Benjamin Levine      
**Print screen:**  
![Friends 1](/project_documentation/D6_media/d6-2-friends-1.png)  
![Friends 2](/project_documentation/D6_media/d6-2-friends-2.png)  
![Friends 3](/project_documentation/D6_media/d6-2-friends-3.png)  
![Friends 4](/project_documentation/D6_media/d6-2-friends-4.png)  

**Requirement:** *Added Comment Like Count - Allows users to know the most popular comments to get an accurate feel of an event*  
**Issue:** https://github.com/ajmastra/cs-386-event-pulse/issues/182     
**Pull request:** https://github.com/ajmastra/cs-386-event-pulse/pull/206    
**Implemented by:** Benjamin Levine      
**Approved by:** Samuel Butler    
**Print screen:**  
![Comment Likes 2](/project_documentation/D6_media/d6-2-likes-1.png)  
![Comment Likes 1](/project_documentation/D6_media/d6-2-likes-2.png)  

**Requirement:** *Added Interested Button - Allows the user to save events they are interested in and view at a list of them*  
**Issue:** https://github.com/ajmastra/cs-386-event-pulse/issues/153    
**Pull request:** https://github.com/ajmastra/cs-386-event-pulse/pull/207    
**Implemented by:** Samuel Butler   
**Approved by:** Andrew Gajewski  
**Print screen:**  
![Interested Button 1](/project_documentation/D6_media/d6-2-interest-button-1.png)
![Interested Button 2](/project_documentation/D6_media/d6-2-interest-button-2.png)
![Interested Button 3](/project_documentation/D6_media/d6-2-interest-button-3.png)

**Requirement:** *Reworked Interest backend and Updated Highlighting - Allows multiple interests to be associated with each event and makes hightlighting cleaner*
**Issue:** https://github.com/ajmastra/cs-386-event-pulse/issues/218    
**Pull request:** https://github.com/ajmastra/cs-386-event-pulse/pull/207    
**Implemented by:** Samuel Butler      
**Approved by:** Andrew Gajewski  
**Print screen:**  
![Interests Rework 1](/project_documentation/D6_media/d6-2-interests-rework-1.png)
![Interests Rework 2](/project_documentation/D6_media/d6-2-interests-rework-2.png)   

**Requirement:** *Added For You Page - Allows the user to have a centralized page of events dedicated towards their interests*  
**Issue:** https://github.com/ajmastra/cs-386-event-pulse/issues/105     
**Pull request:** https://github.com/ajmastra/cs-386-event-pulse/pull/205    
**Implemented by:** Andrew Gajewski    
**Approved by:** Zachary Garza    
**Print screen:**  
![For You Page 1](/project_documentation/D6_media/d6-2-foryou-1.png)
![For You Page 2](/project_documentation/D6_media/d6-2-foryou-2.png)  

**Requirement:** *Added Admin User - Allows users to have a moderated experience by giving select people the ability to moderate pages*  
**Issue:** https://github.com/ajmastra/cs-386-event-pulse/issues/194     
**Pull request:** https://github.com/ajmastra/cs-386-event-pulse/pull/204    
**Implemented by:** Andrew Sliva      
**Approved by:** Anthony Mastrangelo  
**Print screen:**   
Admin View
![admin](/project_documentation/D6_media/admin-view.png)
Non-admin View
![non-admin](/project_documentation/D6_media/non-admin-view.png)

## 3. Tests
### 3.1 Unit tests

1. **Test Framework**: Pytest
2. **Automated Unit Test Files**: https://github.com/ajmastra/cs-386-event-pulse/tree/main/tests/unit_testing
3. **Example Test Case**: We created a variety of test cases for this implementation, but one of the more important ones was to do with the Add Comment functionality. For this, there needs to be a user account setup and logged in, as well as an event already created. The user can then try to post a comment on the event, adding it to the database. The testing that we are performing is on the models.py file, where we have the Comment database schema.
4. **Result of testing**:
![unit_testing](/project_documentation/D6_media/unit_testing.png)

### 3.2 Acceptance tests

1. **Test Framework**: Selenium  
2. **Automated Acceptance Test Files**: https://github.com/ajmastra/cs-386-event-pulse/acceptance_tests  

#### **Login Test**
![login](/project_documentation/D6_media/test_login_results.png)

#### **Event Search Test** 
![event search](/project_documentation/D6_media/test_event_search_results.png)

#### **Event Creation Test**
![event creation](/project_documentation/D6_media/test_event_creation_results.png)

#### **Comment Test**
![comment](/project_documentation/D6_media/test_event_comment.png)

##### **Sign-Up Test** 
![sign up](/project_documentation/D6_media/test_sign_up_results.png)

**These acceptance tests ensure that the core functionalities of the application work seamlessly from a user's perspective:**
- **1. Login Test** Verifies that users can log in successfully by providing valid credentials and navigating to the homepage.
- **2. Event Search Test** Ensures that users can search for events using the search bar and view relevant results.
- **3. Event Creation Test** Confirms that users can create new events by filling in all required fields (title, date, time, location, description, and event type) and successfully submitting the form.
- **4. Comment Test** Validates that users can add a comment to an event, post it successfully, and see it displayed in the comments section.  
- **5. Sign-Up Test** Ensures that new users can register by completing all required fields, such as email, username, and password, and successfully submitting the registration form.

## 4. Demo
Click to watch our demo of our web app!
[![Demo Video](https://i.ytimg.com/vi/27f8P0S_TW0/maxresdefault.jpg)](https://www.youtube.com/watch?v=27f8P0S_TW0)

## 5. Code quality
At the root of our team's code quality is our standards for Python syntax that we defined back in deliverable 2. We have clear and simple standards that ensure any code that is developed is of high quality and consistent across developers. We developed these guidelines and standards before starting the development, and as a result all of our code is very uniform and coherent.

1.	**Naming Conventions**  
We have rules for naming conventions of different things, for example, class names are in PascalCase, constants are UPPERCASE, while functions are in snake_case. These naming conventions help us identify and differentiate what everything is, while also keeping the code looking clean and structured.

2.	**Function Design and Structure**  
We also have guidelines that define how functions should be designed. Functions should be short and focused on a single task, have no more than 5 parameters, and have a single clear return path when possible. 

3.	**Code Formatting**  
We also have rules for general code formatting that help keep the code structured and uniform. For example, all lines have a maximum of 79 characters, and use four spaces per indentation level (no tabs). 

4.	**Metrics**  
One metric that our code measures well in is complexity. The issue with complexity arises in “the large and complex methods problem”. In our project, we have methods that do one task at a time (this is also what we were taught in design principles in D5). If your method only focuses on one thing and doesn't attempt to do multiple things at the same time, it is much easier to limit the complexity and scale of a method.

5.	**Best Practices**  
“User variable names that mean something” - Throughout our project you will see that all our naming is of the same form. All our variable names have meanings related to their functionalities and dependencies. Throughout models.py you can see examples of this.  
Comments - Throughout our code we can see comments labeling what classes do what. Our comments aren't explaining the functionality of the code, simply just giving it a label to make it easier. 

6.	**Testing Standards**  
Whenever developing code, and testing the software, we always do so in a virtual environment. This ensures that any testing we do provides consistent results, as we are all testing in the same environment. With consistent testing results, we can be confident our code will run as expected in all scenarios.


## 6. Lessons learned
During this release, we had to fulfill a lot of daunting requirements we made back in D2. We were pretty nervous regarding relationships and the additions of models to our system, so comments, friends, and interests were pretty scary to implement. During the early stages, interests were returned as strings and set into the User, but now we've worked on Comments, which have their own class, and then a N:N relationship with User towards itself, which was relatively easy to implement. Doing these created a commenting system to be added to events as well as users being able to friend each other. This allowed our software to focus on its core values, like allowing users to connect with one another, learning about what it means to align with our core values. With this in mind, we dedicated some time to learn how to add side-by-side HTML elements and override a previously-existing element in our software, like the previous "interest" system. Having an "admin" user was easy to implement, but doing so meant we had to learn how to previously rewrite a good portion of our if statements in the system. All in all, it's important to see how rewriting a system can take a lot of time and head-scratching, especially since our project is relatively tiny compared to bigger industry software. In the future, I think if we were to focus more time on getting deadlines done early, it would be signifigantly easier to communicate with others about problems, allowing all of us to make seamless implementations and contributions. One other thing we'd do differently would be to work on "daunting" things earlier, as once the "scary" relationships were out of the way, a lot more progress was made regarding final implementation. 

