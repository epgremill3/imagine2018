# Imagine 2018 Workshop Outline

0. Introduction: Setting the stage for the workshop
    0. Get to know them
        0. Worked only academically?
        0. Worked professionally? In a company:
            0. 5 or fewer software engineers
            0. 25 or fewer software engineers
            0. 100 or fewer software engineers
            0. More than 100 software engineers
        0. Used Git? GitHub? GitLab? Other?
        0. Used Python? What other programming languages?
        0. Used Django? What other web application frameworks?
        0. Used PostgreSQL? What other relational (or non-relational!) databases?
        0. Used Docker? Any other container or virtualization systems?
        0. Used Jenkins? Any other CI/CD systems?
        0. Used AWS? Any other cloud-based environments?
    0. Setting the stage
        0. News: you applied for a job when you signed up for this workshop
        0. Good News: those questions were the interview and you're hired!
        0. Bad News: the only pay is what you learn in the next couple hours
    0. A little about me
        0. Bachelor's in CS from Cornell
        0. Worked at a variety of companies from 5 engineers to > 100 engineers
        0. Mostly focused in "server-side business logic" with some UI and some DB experience
    0. What Are We Doing? App for tracking maintenance on your car(s)
0. Starting Up: We've got some decisions to make
    0. What form will our app take? Discuss trade offs:
        0. Web App
            0. Pros: accessible anywhere with an Internet connection; can make cross-platform/device
            0. Cons: can't really use disconnected; requires servers, etc. for us
        0. Mobile App
            0. Pros: can use anywhere and at any time; all work done on users' devices
            0. Cons: can't aggregate data across users; fewer monetization options?
        0. In the end we're going to do a web app because that's what I've planned to do but either or both would be OK
    0. What technologies will we use?
        0. Considerations
            0. Who's working with me and what do we already know (well)?
            0. Is there anything that's particularly suited to this problem / domain?
            0. How much of what I want to do has already been done and is accessible to me?
            0. How easy or difficult will it be to change in the future (upgrade or switch platform)?
            0. Stability and Maturity of the Platform
            0. Pace of Development of the Platform
            0. Performance, Safety and Security, Reliability of the Platform
            0. Extracting the Considerations:
                0. Time to market
                0. Freedom to focus on what we're trying to do
                0. Depth vs. Breadth
                0. Ability to change and adapt
                0. Costs and Benefits
                    0. Can we find people who know this technology and want to work with it?
                    0. Can we find people who know it well and can fix things that go wrong?
        0. Infrastructure Tools?
            0. Source Code Control (Git, other SCC tools; GitHub, GitLab, etc.)
            0. Deployment / Version Tracking (Jenkins, GitLab, etc.)
            0. Servers (Docker, AWS, etc.)
            0. Support and Management Tools (CloudWatch, Sentry, etc.)
        0. Database or Repository?
            0. SQLite, PostgreSQL, MySQL, etc. (free)
            0. MS SQL Server, Oracle, etc. (paid)
            0. No-SQL databases, etc.
        0. Web Application Framework?
            0. ASP.NET (Core), Django
            0. Ruby on Rails, Express JS, Spring (Java), various PHP frameworks, etc.
        0. Web UI Framework / Stack?
            0. Probably want to incorporate something like Bootstrap or Foundation for cross-browser, responsive web
            0. Also could go the Angular / React / etc. route but not going there (yet)
    0. How will we work? What is our development workflow or process?
        0. Agile, Scrum, etc.
        0. Some general questions:
            0. What are all the things we want/need to do?
            0. Which one(s0 are we going to do first/now?
            0. How do we know when they're done?
            0. How do we get them out to users when they're done?
            0. How do we make sure this all happens quickly enough and with sufficient quality?
        0. How much to define up-front vs. as we go?
        0. We'll start with tickets for stories/features/changes/bugs and refine as we go along
            0. Pull/Merge Requests?
            0. Approval? Testing? Etc.?
            0. CI? CD?
0. Getting to Work
    0. Setup the development environment
        0. Flexibility can be a great thing, but standardization can be, too
            0. Windows, Mac, Linux
            0. PyCharm, VS Code, Sublime, etc.
            0. Docker or Not?
            0. Git Bash, GitHub Desktop, PyCharm, Git Tower, etc.
            0. Mix and Match (but sometimes problems between multiple)
        0. Docker Desktop (Windows Pro)
            0. Settings > General: Expose daemon ... without TLS
            0. Settings > Shared Drives: Make sure to share the drive on which you'll be developing
        0. Install Git (for Windows) _**TODO:** Is this necessary with PyCharm?_
            0. Configure name, email, any other settings (autocrlf, safecrlf, etc.)
        0. GitHub
            0. Register / Create Account (if don't already have one)
            0. I'll _probably_ then have to add them as collaborators _**TODO:** test this out!_
            0. Can then clone the repo _**TODO:** do through Git (Bash) or PyCharm?_
        0. Install PyCharm Pro (eval)
            0. Open the project
            0. [Configure PyCharm to use Docker](https://www.jetbrains.com/help/pycharm/using-docker-compose-as-a-remote-interpreter.html)
            0. Configure PyCharm to connect to the database
                0. View > Tool Windows > Database
                0. "+" > Data Source > PostgreSQL
                0. Name
                0. General:
                    0. Host = 0.0.0.0
                    0. Database = postgres
                    0. User = postgres
                    0. Password = `POSTGRES_PASSWORD` from `docker-compose.yml`
                    0. Will _probably_ have to click to "Download missing driver" (JDBC)
                    0. Test connection _**TODO:** will this work without running `docker-compose up`?_
                0. Schemas
                    0. Check current database and check **postgres**
                    0. Expand **postgres** and ensure Current schema (public) is checked
                    0. Probably doesn't hurt to check public (Current schema) too
    0. What I did to bootstrap the project
        0. Created the GitHub repository
            0. Adding collaborators
            0. Protecting branches
            0. README.md, .gitignore, etc.
        0. [Bootstrapped a Django project in Docker](https://docs.docker.com/compose/django/)
        0. [Added the PostgreSQL client to the app image](https://hub.docker.com/_/django/)
        0. Added JetBrains files to .gitignore (Google "pycharm gitignore")
        0. Completed [Part 1 of the Django tutorial](https://docs.djangoproject.com/en/2.1/intro/tutorial01/)
            0. This creates a very simple "Hello World" app (adjust for this workshop / project at hand)
        0. _**At this point** the app is bootstrapped and can be pushed up to the repo for collaboration_
    0. Start working on tickets
    0. Working the Process / Building the Product
    0. Refining the Process
    0. Refining the Product
    0. Defining the Vision / Deciding on Version 1.0
0. Securing It
0. Taking It to Market
0. Extending, Supporting, and Maintaining It
0. Growing It
0. Selling It and Retiring (or Not)

