# Event Pulse
## Capturing the heartbeat of local events!

EventPulse is an event tracking application designed for NAU students and Flagstaff residents in mind. It helps users explore local events, connect with groups of people who share similar interests, and engage in discussions about events.

### Version:
Current Version: v0.1.0 (Pre-release)

## Built With

- **Backend:** Flask
- **Frontend:** HTML, CSS, Jinja, JS
- **Database:** SQLite, utilizing Flask's SQLAlchemy

## Installation

To set up the EventPulse application locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/ajmastra/cs-386-event-pulse
   cd cs-386-event-pulse
   ```

2. Install the required pacakges:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application   
   Windows systems:
   ```bash
   python main.py
   ```
   Unix systems:
   ```
   python3 main.py
   ```
4. In the console, open the local host it gives you, for example,
   ```bash
   * Running on http://xxx.x.x.x:xxxx
   ```
Feel free to make accounts and events to test out the software!   

## Deployment
To deploy Event Pulse on a server/website such as Heroku with PostgreSQL...
1. Start by creating a Heroku app, and add the Heroku Postgres add-on, setting up the necessary environment variables in the config settings. 

2. Ensure you have a Procfile with 
   ```bash
   web: gunicorn main:app
   ```
3. Include all dependencies in requirements.txt and push the    code to Heroku. 

4. Finally, verify the deployment of the app by opening the app in your terminal with with 
   ```
   heroku open
   ```
Congratulations! Event Pulse is deployed!

## Built With

- **Backend:** Flask, Python 3.10+
- **Frontend:** HTML, CSS, Jinja, JS
- **Database:** SQLite, utilizing Flask's SQLAlchemy

## Contributing
Please read [CONTRIBUTING.md](/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us. 

## Versioning
We use [SemVer](https://semver.org) for versioning. For the versions available, see the [tags on this repository](https://github.com/ajmastra/cs-386-event-pulse/tags).

## Authors
   * **Anthony Mastrangelo** - *Initial Web Skeleton Deployment, Code Contributor, Repository Owner, Documentation Author*
   * **Zachary Garza** - *Code Contributor, Frequent Pull Request Acceptor, Documentation Author*
   * **Benjamin Levine** - *Code Contributor, Frequent Pull Request Acceptor, Documentation Author*
   * **Andrew Sliva** - *Code Contributor, Unit Test Author, Documentation Author*
   * **Andrew Gajewski** - *Code Contributor, Innovative, Inception, Documentation Author*
   * **Samuel Butler** - *Code Contributor, Innovative, Inception, Documentation Author*  
  

## License
This project is licensed under the MIT License - see the [LICENSE.md](/LICENSE.md) file for details.

## Acknowledgements
* We thank AJ (Anthony Mastrangelo) for doing a lot of the ideas and framework. He is always knowledgeable, helpful, and responsive. 
* We also thank our TA Alyssa Ortiz for giving us tons of feedback to direct us on the right path. 
* Finally, we thank Dr. Marco Gerosa for being our instructor and facilitating our class to help us gain real-world experience working in teams for software development.