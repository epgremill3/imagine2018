# Imagine 2018 Workshop Outline

1. Introduction: Setting the stage for the workshop
    1. Get to know them
        1. Worked only academically?
        1. Worked professionally? In a company:
            1. 5 or fewer software engineers
            1. 25 or fewer software engineers
            1. 100 or fewer software engineers
            1. More than 100 software engineers
        1. Used Git? GitHub? GitLab? Other?
        1. Used Python? What other programming languages?
        1. Used Django? What other web application frameworks?
        1. Used PostgreSQL? What other relational (or non-relational!) databases?
        1. Used Docker? Any other container or virtualization systems?
        1. Used Jenkins? Any other CI/CD systems?
        1. Used AWS? Any other cloud-based environments?
    1. Setting the stage
        1. News: you applied for a job when you signed up for this workshop
        1. Good News: those questions were the interview and you're hired!
        1. Bad News: the only pay is what you learn in the next couple hours
    1. A little about me
        1. Bachelor's in CS from Cornell
        1. Worked at a variety of companies from 5 engineers to > 100 engineers
        1. Mostly focused in "server-side business logic" with some UI and some DB experience
    1. What Are We Doing? App for tracking maintenance on your car(s)
1. Starting Up: We've got some decisions to make
    1. What form will our app take? Discuss trade offs:
        1. Web App
            1. Pros: accessible anywhere with an Internet connection; can make cross-platform/device
            1. Cons: can't really use disconnected; requires servers, etc. for us
        1. Mobile App
            1. Pros: can use anywhere and at any time; all work done on users' devices
            1. Cons: can't aggregate data across users; fewer monetization options?
        1. In the end we're going to do a web app because that's what I've planned to do but either or both would be OK
    1. What technologies will we use?
        1. Considerations
            1. Who's working with me and what do we already know (well)?
            1. Is there anything that's particularly suited to this problem / domain?
            1. How much of what I want to do has already been done and is accessible to me?
            1. How easy or difficult will it be to change in the future (upgrade or switch platform)?
            1. Stability and Maturity of the Platform
            1. Pace of Development of the Platform
            1. Performance, Safety and Security, Reliability of the Platform
            1. Extracting the Considerations:
                1. Time to market
                1. Freedom to focus on what we're trying to do
                1. Depth vs. Breadth
                1. Ability to change and adapt
                1. Costs and Benefits
                    1. Can we find people who know this technology and want to work with it?
                    1. Can we find people who know it well and can fix things that go wrong?
        1. Infrastructure Tools?
            1. Source Code Control (Git, other SCC tools; GitHub, GitLab, etc.)
            1. Deployment / Version Tracking (Jenkins, GitLab, etc.)
            1. Servers (Docker, AWS, etc.)
            1. Support and Management Tools (CloudWatch, Sentry, etc.)
        1. Database or Repository?
            1. SQLite, PostgreSQL, MySQL, etc. (free)
            1. MS SQL Server, Oracle, etc. (paid)
            1. No-SQL databases, etc.
        1. Web Application Framework?
            1. ASP.NET (Core), Django
            1. Ruby on Rails, Express JS, Spring (Java), various PHP frameworks, etc.
        1. Web UI Framework / Stack?
            1. Probably want to incorporate something like Bootstrap or Foundation for cross-browser, responsive web
            1. Also could go the Angular / React / etc. route but not going there (yet)
    1. How will we work? What is our development workflow or process?
        1. Agile, Scrum, etc.
        1. Some general questions:
            1. What are all the things we want/need to do?
            1. Which one(s0 are we going to do first/now?
            1. How do we know when they're done?
            1. How do we get them out to users when they're done?
            1. How do we make sure this all happens quickly enough and with sufficient quality?
        1. How much to define up-front vs. as we go?
        1. We'll start with tickets for stories/features/changes/bugs and refine as we go along
            1. Pull/Merge Requests?
            1. Approval? Testing? Etc.?
            1. CI? CD?
1. Getting to Work
    1. Setup the development environment
        1. Flexibility can be a great thing, but standardization can be, too
            1. Windows, Mac, Linux
            1. PyCharm, VS Code, Sublime, etc.
            1. Docker or Not?
            1. Git Bash, GitHub Desktop, PyCharm, Git Tower, etc.
            1. Mix and Match (but sometimes problems between multiple)
        1. Docker Desktop (Windows Pro)
            1. Settings > General: Expose daemon ... without TLS
            1. Settings > Shared Drives: Make sure to share the drive on which you'll be developing
        1. Install Git (for Windows) _**TODO:** Is this necessary with PyCharm?_
            1. Configure name, email, any other settings (autocrlf, safecrlf, etc.)
        1. GitHub
            1. Register / Create Account (if don't already have one)
            1. I'll _probably_ then have to add them as collaborators _**TODO:** test this out!_
            1. Can then clone the repo _**TODO:** do through Git (Bash) or PyCharm?_
        1. Install PyCharm Pro (eval)
            1. Open the project
            1. [Configure PyCharm to use Docker](https://www.jetbrains.com/help/pycharm/using-docker-compose-as-a-remote-interpreter.html)
            1. Configure PyCharm to connect to the database
                1. View > Tool Windows > Database
                1. "+" > Data Source > PostgreSQL
                1. Name
                1. General:
                    1. Host = 0.0.0.0
                    1. Database = postgres
                    1. User = postgres
                    1. Password = `POSTGRES_PASSWORD` from `docker-compose.yml`
                    1. Will _probably_ have to click to "Download missing driver" (JDBC)
                    1. Test connection _**TODO:** will this work without running `docker-compose up`?_
                1. Schemas
                    1. Check current database and check **postgres**
                    1. Expand **postgres** and ensure Current schema (public) is checked
                    1. Probably doesn't hurt to check public (Current schema) too
    1. What I did to bootstrap the project
        1. Created the GitHub repository
            1. Adding collaborators
            1. Protecting branches
            1. README.md, .gitignore, etc.
        1. [Bootstrapped a Django project in Docker](https://docs.docker.com/compose/django/)
        1. [Added the PostgreSQL client to the app image](https://hub.docker.com/_/django/)
        1. Added JetBrains files to .gitignore (Google "pycharm gitignore")
        1. Completed [Part 1 of the Django tutorial](https://docs.djangoproject.com/en/2.1/intro/tutorial01/)
            1. This creates a very simple "Hello World" app (adjust for this workshop / project at hand)
        1. _**At this point** the app is bootstrapped and can be pushed up to the repo for collaboration_
    1. Start working on tickets
    1. Working the Process / Building the Product
    1. Refining the Process
    1. Refining the Product
    1. Defining the Vision / Deciding on Version 1.0
1. Securing It
1. Taking It to Market
1. Extending, Supporting, and Maintaining It
1. Growing It
1. Selling It and Retiring (or Not)

