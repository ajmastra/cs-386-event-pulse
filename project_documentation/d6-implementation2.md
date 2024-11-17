# Implementation 2
This deliverable should describe the second release of your project. A release is a fully functional software that delivers a set of features (it doesn’t need to be the complete set, but the software needs to be usable). Structure your deliverable into the following sections. See the “Team Project Instructions” for details about formatting. 

## 1. Introduction
Provide 1-2 paragraphs to describe your system. This description should contain the value proposition and the main features. At the end of the introduction, include a link to your project on GitHub.

Grading criteria (1 point): This section will be evaluated in terms of correctness, completeness, thoroughness, consistency, coherence, and adequate use of language. The description should be consistent with the current state of the project. You should include the link to GitHub.

## 2. Implemented requirements
List in this section the requirements and associated pull request that you implemented for this release, following the example below---include the description of the requirement, a link to the issue,  a link to the pull request(s) that implement the requirement, who implemented the requirement, who approved it, and a print screen that depicts the implemented feature (if applicable). Order the requirements by the name of the student who implemented them. Everyone in the group is expected to have code contributions documented by means of pull requests. Every pull request should be reviewed and approved before the merge. 

At this point, we expect that you implement/prototype the features you specified in your MVP (c.f. D.2 Requirements). Pivots and changes are allowed as soon as you justify them.

See the example:

**Requirement:** As a Student, I want to add a homework assignment so that I can organize my ToDo list.  
**Issue:** https://github.com/user/project/issue  
**Pull request:** https://github.com/user/project/pull  
**Implemented by:** Martin Fowler  
**Approved by:** Ada Lovelace  
**Print screen:** A print screen that depicts the implemented feature (if applicable)  

our example:
**Requirement:** *WhatYouDid - How it makes software better*  
**Issue:** https://github.com/ajmastra/cs-386-event-pulse/issues/ISSUENUMBER   
**Pull request:** https://github.com/ajmastra/cs-386-event-pulse/pull/PRNUMBER    
**Implemented by:** impName    
**Approved by:** appName    
**Print screen:** ![ImpTitle](/project_documentation/D6_media/linkToImageFile)  

---

**Requirement:** *Comments under Events - Allows user to get a feel of the event from the community*  
**Issue:** https://github.com/ajmastra/cs-386-event-pulse/issues/154    
**Pull request:** https://github.com/ajmastra/cs-386-event-pulse/pull/193    
**Implemented by:** Anthony Mastrangelo    
**Approved by:** Andrew Sliva    
**Print screen:** ![Comments](/project_documentation/D6_media/d6-2-comments.png)  

**Requirement:** *Add Friend Functionality - Allows users to connect with their peers and go to events together*  
**Issue:** https://github.com/ajmastra/cs-386-event-pulse/issues/152     
**Pull request:** https://github.com/ajmastra/cs-386-event-pulse/pull/PRNUMBER    
**Implemented by:** Zachary Garza      
**Approved by:** appName    
**Print screen:** ![Friends 1](/project_documentation/D6_media/d6-2-friends-1.png)  
![Friends 2](/project_documentation/D6_media/d6-2-friends-2.png)  
![Friends 3](/project_documentation/D6_media/d6-2-friends-3.png)  
![Friends 4](/project_documentation/D6_media/d6-2-friends-4.png)  

**Requirement:** *Added Comment Like Count - Allows users to know the most popular comments to get an accurate feel of an event*  
**Issue:** https://github.com/ajmastra/cs-386-event-pulse/issues/182     
**Pull request:** https://github.com/ajmastra/cs-386-event-pulse/pull/PRNUMBER    
**Implemented by:** Benjamin Levine      
**Approved by:** appName    
**Print screen:** ![Comment Likes](/project_documentation/D6_media/d6-2-FILENAME)  

**Requirement:** *Added Interested Button - Allows the user to virtual display they're interested in an event*  
**Issue:** https://github.com/ajmastra/cs-386-event-pulse/issues/153    
**Pull request:** https://github.com/ajmastra/cs-386-event-pulse/pull/PRNUMBER    
**Implemented by:** Samuel Butler      
**Approved by:** appName    
**Print screen:** ![Interested Button](/project_documentation/D6_media/d6-2-FILENAME)  

**Requirement:** *Added For You Page - Allows the user to have a centralized page of events dedicated towards their interests*  
**Issue:** https://github.com/ajmastra/cs-386-event-pulse/issues/105     
**Pull request:** https://github.com/ajmastra/cs-386-event-pulse/pull/PRNUMBER    
**Implemented by:** Andrew Gajewski    
**Approved by:** appName    
**Print screen:** ![For You Page](/project_documentation/D6_media/d6-2-FILENAME)  

**Requirement:** *Added Admin User - Allows users to have a moderated experience by giving select people the ability to moderate pages*  
**Issue:** https://github.com/ajmastra/cs-386-event-pulse/issues/194     
**Pull request:** https://github.com/ajmastra/cs-386-event-pulse/pull/PRNUMBER    
**Implemented by:** Andrew Sliva      
**Approved by:** appName    
**Print screen:** ![Admin Users](/project_documentation/D6_media/d6-2-FILENAME)  


Remember that all code contributions should be submitted via pull requests and the reviewer should review and approve each pull request.

Grading criteria (20 points): This section will be evaluated in terms of correctness, completeness, thoroughness, consistency, coherence, adequate use of language, and amount of work put into the implementation. Students can receive different grades depending on their involvement. It is expected that all members contribute with non-trivial implementation. All pull requests should be approved and integrated by the scrum master. You should follow an adequate workflow (description of the requirement on the issue tracker, submission of the implemented requirement as a pull request, and review of the pull request by another developer). 

## 3. Tests
### 3.1 Unit tests

A unit test is an automated test that aims to verify the behavior of a component isolated from the rest of the system. For this deliverable, show an example of a unit test that uses mock objects to isolate the class from the rest of the system. 

Test framework you used to develop your tests (e.g., JUnit, unittest, pytest, etc.)
Link to your GitHub folder where your automated unit tests are located
An example of a test case that makes use of mock objects. Include in your answer a GitHub link to the class being tested and to the test
A print screen showing the result of the unit test execution
Grading criteria (2 points): adequate choice of a test framework, coverage of the tests, quality of the tests, adequate use of Mock objects, and a print screen showing successful test execution.

### 3.2 Acceptance tests

An acceptance test is a test that verifies the correct implementation of a feature from the user interface perspective. An acceptance test is a black box test (the system is tested without knowledge about its internal implementation). Provide the following information:

Test framework you used to develop your tests (e.g., Selenium, Katalon Studio, Espresso2, Cucumber, etc.)
Link to your GitHub folder where your automated acceptance tests are located
An example of an acceptance test. Include a GitHub link to the test and an explanation about the tested feature in your answer.
A print screen/video showing the acceptance test execution
Grading criteria (2 points): adequate choice of a test framework, coverage of the tests, quality of the tests, adequate example of an acceptance test, print screen/video showing successful test execution.

## 4. Demo
Include a link to a video showing the system working.

Grading criteria (10 points): This section will be graded based on the quality of the video and on the evidence that the features are running as expected. Additional criteria are the relevance of the demonstrated functionalities, the correctness of the functionalities, and the quality of the developed system from the external point of view (user interface).

## 5. Code quality
Describe how your team managed code quality. What were your policies, conventions, adopted best practices, etc., to foster high-quality code? 

Grading criteria (3 points): Adequate list of practices that were adopted to improve code quality and clear description with adequate use of language.

## 6. Lessons learned
In retrospect, describe what your team learned during this second release and what you would change if you would continue developing the project. 

Grading criteria (2 points): Adequate reflection about problems and solutions, clear description with adequate use of language.