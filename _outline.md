# Imagine 2018 Workshop Outline

## Introduction: Setting the stage for the workshop

### Get to know the participants

- Worked only academically?
- Worked professionally? In a company:
    - 5 or fewer software engineers
    - 25 or fewer software engineers
    - 100 or fewer software engineers
    - More than 100 software engineers
- Used Git? GitHub? GitLab? Other?
- Used Python? What other programming languages?
- Used Django? What other web application frameworks?
- Used PostgreSQL? What other relational (or non-relational!) databases?
- Used Docker? Any other container or virtualization systems?
- Used Jenkins? Any other CI/CD systems?
- Used AWS? Any other cloud-based environments?

### Set the stage

- News: you applied for a job when you signed up for this workshop
- Good News: those questions were the interview and you're hired!
- Bad News: the only pay is what you learn in the next couple hours
- A little about me
    - Bachelor's in CS from Cornell
    - Worked at a variety of companies from 5 engineers to > 100 engineers
    - Mostly focused in "server-side business logic" with some UI and some DB experience
- What Are We Doing? App for tracking maintenance on your car(s)

## Starting Up: We've got some decisions to make

### What form will our app take? 

Discuss trade offs:
- Web App
    - Pros: accessible anywhere with an Internet connection; can make cross-platform/device
    - Cons: can't really use disconnected; requires servers, etc. for us
- Mobile App
    - Pros: can use anywhere and at any time; all work done on users' devices
    - Cons: can't aggregate data across users; fewer monetization options?
- In the end we're going to do a web app because that's what I've planned to do but either or both would be OK

### What technologies will we use?

Considerations:
- Who's working with me and what do we already know (well)?
- Is there anything that's particularly suited to this problem / domain?
- How much of what I want to do has already been done and is accessible to me?
- How easy or difficult will it be to change in the future (upgrade or switch platform)?
- Stability and Maturity of the Platform
- Pace of Development of the Platform
- Performance, Safety and Security, Reliability of the Platform

Put differently:
- Time to market
- Freedom to focus on what we're trying to do
- Depth vs. Breadth
- Ability to change and adapt
- Costs and Benefits
    - Can we find people who know this technology and want to work with it?
    - Can we find people who know it well and can fix things that go wrong?

#### Infrastructure Tools

- Source Code Control (Git, other SCC tools; GitHub, GitLab, etc.)
- Deployment / Version Tracking (Jenkins, GitLab, etc.)
- Servers (Docker, AWS, etc.)
- Support and Management Tools (CloudWatch, Sentry, etc.)

#### Database or Repository

- SQLite, PostgreSQL, MySQL, etc. (free)
- MS SQL Server, Oracle, etc. (paid)
- No-SQL databases, etc.

#### Web Application Framework

- ASP.NET (Core), Django
- Ruby on Rails, Express JS, Spring (Java), various PHP frameworks, etc.

#### Web UI Framework / Stack

- Probably want to incorporate something like Bootstrap or Foundation for cross-browser, responsive web
- Also could go the Angular / React / etc. route but not going there (yet)

### Development workflow / process

- Agile, Scrum, etc.
- Some general questions:
    - What are all the things we want/need to do?
    - Which one(s0 are we going to do first/now?
    - How do we know when they're done?
    - How do we get them out to users when they're done?
    - How do we make sure this all happens quickly enough and with sufficient quality?
- How much to define up-front vs. as we go?
- We'll start with tickets for stories/features/changes/bugs and refine as we go along
    - Pull/Merge Requests?
    - Approval? Testing? Etc.?
    - CI? CD?

## Preparation / Startup

### Bootstrap the project

Typically only one person needs to do this... 
I'll run through these steps quickly; feel free to ask questions...
- Create the GitHub repository
    - Adding collaborators
    - Protecting branches
    - README.md, .gitignore, etc.
- [Bootstrap a Django project in Docker](https://docs.docker.com/compose/django/)
- [Add the PostgreSQL client to the app image](https://hub.docker.com/_/django/)
- Add JetBrains files to .gitignore (Google "pycharm gitignore")
- Complete [Part 1 of the Django tutorial](https://docs.djangoproject.com/en/2.1/intro/tutorial01/)
    - This creates a very simple "Hello World" app (adjust for this workshop / project at hand)

### Setup the development environment

#### Note

_Asked Iris to tell participants to do the following, so some/all of this may not be necessary:_
- Create GitHub account and pass along username
- Install Git and configure username, email address, safe/auto CRLF, etc.
- Install Docker
- Install PyCharm Pro (free eval)

#### Overall Steps and Considerations:

- Flexibility can be a great thing, but standardization can be, too
    - Windows, Mac, Linux
    - PyCharm, VS Code, Sublime, etc.
    - Docker or Not?
    - Git Bash, GitHub Desktop, PyCharm, Git Tower, etc.
    - Mix and Match (but sometimes problems between multiple)

#### Docker Desktop (Windows Pro)

- Settings > General: Expose daemon ... without TLS
- Settings > Shared Drives: Make sure to share the drive on which you'll be developing

#### Install Git (for Windows) 

- _**TODO:** Is this necessary with PyCharm?_
- Configure name, email, any other settings (autocrlf, safecrlf, etc.)

#### GitHub

- Register / Create Account (if don't already have one)
- Tell / Send me your GitHub username and I'll invite you to collaborate
- Accept the invitation

#### Install PyCharm Pro (eval)

-  Clone the repo
    - Open PyCharm
    - Checkout from version control
    - Git
    - Paste in the repo URL: `https://github.com/epgremill3/imagine2018.git`
    - Select where to save it and click Go
    - When asked go ahead and open it up
- [Configure PyCharm to use Docker](https://www.jetbrains.com/help/pycharm/using-docker-compose-as-a-remote-interpreter.html)
    - Add the Docker server to PyCharm
        - File > Settings > Build, Execution, and Deployment > Docker
        - Click the "+" to create a new Docker server; accept the defaults and click OK
    - Set the project interpreter
        - File > Settings > Project: imagine2018 > Project Interpreter
        - Click the gear icon and choose "Add..."
        - Select Docker Compose
        - Server=Docker, Configuration File=./docker-compose.yml, Service=web, Python interpreter path=python3
        - Click "OK"
    - Set up the run profile
        - In the dropdown at the top near the run button click and select "Edit Configurations..."
        - Add a Django Server (if not already present)
        - Name=imagine2018, host=0.0.0.0, Python interpreter=<the one we created (_Remote Python 3.7.0 Docker Compose (web at ...)_)>
        - I think all the other defaults are fine; press OK
- Configure PyCharm to connect to the database
    - View > Tool Windows > Database
    - "+" > Data Source > PostgreSQL
    - Name
    - General:
        - Host = 0.0.0.0
        - Database = postgres
        - User = postgres
        - Password = `POSTGRES_PASSWORD` from `docker-compose.yml`
        - Will _probably_ have to click to "Download missing driver" (JDBC)
        - Test connection _**TODO:** will this work without running `docker-compose up`?_
    - Schemas
        - Check current database and check **postgres**
        - Expand **postgres** and ensure Current schema (public) is checked
        - Probably doesn't hurt to check public (Current schema) too

## Development Iteration 1

### Tickets for Development Iteration 1

_Already entered these into GitHub_
- New users should be able to sign up for the app
- Existing users should be able to sign into the app
- A signed in user should see a list of vehicles
- A signed in user should be able to add, update, and remove vehicles
- A signed in user should be able to see the service history for a vehicle
- A signed in user should be able to add, update, and remove service history entries for a vehicle
- If not signed in these things should not be possible
- A signed in user should be able to sign out
- Ideally all of this will work on a desktop and a mobile web browser

### Process

- Divide up into teams of 2-4
- Assign ticket to collaborator
- Code, commit, push
- After a while we'll test and when it looks good we'll go live!

### Problems We'll Run Into

- "Lose" a collaborator part-way through: what happens to his/her work?
- Merge conflicts on `master` (high-touch files like `models.py`, `views.py`, etc.)
- Manual testing is tedious and painful
- Things will break unexpectedly because we're not well coordinated
- Will all the pages (views) look the same (consistent)?
- Will the object model fit together well?

## Development Iteration 2

### Revisions for Development Iteration 2

There are a variety of workflows out there. 
You can look at e.g. Git Flow (just Google "git flow") for a larger-scale, robust example. 
We're going to just do a few key things to improve our workflow without going quite that far:
- Protect master / use branches
    - Push to your branch regularly
    - Also update your ticket with notes / discoveries / decisions / etc.
- Break up files (each gets own folder)
    - models.py
    - views.py
    - tests.py
- Add automated tests
    - Ideally we'd make this part of the automated process
    - To start we can enforce this by convention (reviewer can ask --or-- reviewer can run)
    - We'll start with built-in unit and end-to-end tests
    - Ideally we'd also add full UI tests with something like Nightwatch JS or Protractor (for Angular)
- Do code reviews on Pull Requests (at least to `master`)
    - Does it make sense?
    - Does it look like it will do what it's supposed to do?
    - Does it look like it adheres to our standards?
    - Do the tests pass, is there documentation, etc.?
- Organize and set some lightweight standards in functional areas
    - GUI
    - API / Object Model
    - Testing

### Tickets for Development Iteration 2

_These in addition to those for Development Iteration 1_
- Integrate a GUI toolkit (e.g. Bootstrap) and propose some lightweight standards (in `README.md`)
- Add automated tests for models and views and propose some lightweight standards (in `README.md`)
- Look at the primary features of the app and design the object model and API all at once (details in tickets)

### Revised Development Workflow

- Assign ticket to collaborator
- Collaborator checks out a branch named for that ticket
- Code, commit, push
- When ready submit a pull request and request a review
- Reviewer checks code, confirms tests passed, then approves merge into `master`
- After a while we'll run automated and manual tests on `master`; when it looks good we'll tag and release

### We'll still run into problems

- There will still be merge conflicts that you'll have to resolve; it will just be in your branch...
- Migrations and compatibility (_maybe_)...
- There will still be bugs (there will _**always**_ be bugs)...

## Deployment

### Tickets for Deployment

- 
- [Setup the ECS (App) cluster](https://aws.amazon.com/getting-started/tutorials/deploy-docker-containers/)
    - [Setup a Docker Registry](https://docs.aws.amazon.com/AmazonECR/latest/userguide/ECR_GetStarted.html)
    - Build Docker image(s) and push to Registry
- [Setup the RDS (DB) cluster](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.PostgreSQL.html)
- [Deploy Django/Python3/PostgreSQL app to AWS](https://realpython.com/deploying-a-django-app-and-postgresql-to-aws-elastic-beanstalk/)
    - Was good, but didn't use Docker...
- Secure passwords (e.g. DB)
    - Environments
    - KMS or similar
- Secure the web server (don't use Django development server, etc.)

## Continuous Integration and Deployment

### Tickets for CI/CD

- Setup a Jenkins server
- Script it to do the following when a build is triggered
    - Run automated tests
    - Build Docker image(s)
    - Push Docker image(s) to Docker Registry (if tests passed?)
- Configure it to do those things on commit to `master`
- Discuss other Git workflow steps like merging master into branches before running tests, etc.

## Go-Live and Beyond

### Tickets for Going Live

- Support and Maintenance
    - Integrate real logging
    - Look at logs in CloudWatch
    - Figure out how to get alerts on problems automatically (don't want to scan CloudWatch all day long)
- Ongoing Development
    - How do we deal with backwards-compatibility as we move forward (change models, etc.)?
    - How do we upgrade our components (e.g. database, web app/GUI frameworks, etc.)?
    - Password strength checking
    - Reset password
    - Two-Factor Authentication
    - View all service records across vehicles
    - Sort lists (vehicles, service entries)
    - Search vehicles and service entries
    - Improve object model for vehicles
        - Standardize make, model, etc.
        - Any ways to look up things externally? e.g. VIN?
    - Improve object model for service entries
        - Standardize parts serviced
        - Any ways to look up things externally? e.g. Garage/Station?
- Disaster Recovery
    - AWS data centers / regions
    - AWS backups and other best practices
