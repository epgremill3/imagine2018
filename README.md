# Bootstrapping a Professional Software Project

Small change... 
This hands-on workshop will introduce participants to products and processes used in medium to large-scale professional software projects. 
Through the lens of a sample web application we'll examine the infrastructure and practices used to build applications with a large team. 
Technologies will include GitHub, Docker, Jenkins, Django, PostgreSQL, and more. 
We'll configure and link these technologies with a sample development workflow then run through the steps to give everyone a feel for the way a professional software project may be run. 
We'll also discuss considerations such as starting small with an eye toward future growth, how to make changes quickly, and what good testing might look like.

## Technologies

- GitHub repo
- Docker container(s)
    - Django web
    - Postgres DB
    - Redis write-through cache?
    - Testing w/ Nightwatch?
- Jenkins build
    - Compile SCSS / SASS and other static content?
    - Run tests
- Bootstrap / HTML 5 / CSS 3 / LESS --or-- SASS --or-- SCSS (?)

## Discussion Points

- SDLC
    - Specify in ticket
    - Code change
    - Code tests
    - Review
    - Merge
    - Deploy
- Security (VPN vs. tunnel)
- Better CI (GitLab)
- Docker vs. Docker Compose
- AWS
- Mobile app vs. HTML 5
- Testing (unit, integration, UI)

## What I did

- Upgrade to Windows 10 Pro
- Install Docker Desktop for Windows
- Install Git for Windows
    - Setup name, email, etc.
- Create the GitHub repository (and clone it locally)
- Install PyCharm (Pro; free eval)
- Bootstrap a Django project in Docker: https://docs.docker.com/compose/django/
    - Add the PostgreSQL client to the app image: https://hub.docker.com/_/django/
- Apply initial migrations
    - Hinted by a warning in the console output on `docker-compose up`
    - Had to get into web container via `docker exec <container_id> bash`
    - Once in ran `./manage.py migrate`
    - Could have also done this through PyCharm: `Tools` > `Run manage.py task...` then enter `migrate`...
- Configured PyCharm to use Docker, etc.: https://www.jetbrains.com/help/pycharm/using-docker-compose-as-a-remote-interpreter.html
- Configured PyCharm to connect to the database
    - First set a password in the db service in `docker-compose.yml`
    - Then updated the password (added) to `settings.py`
    - Then was able to configure DB connection to 0.0.0.0:5432 for user postgres with that password and include public schema
- Added JetBrains files to .gitignore (Google "pycharm gitignore")
- Figure out how to merge and resolve merge conflicts using PyCharm
- Completed Part 1 of the Django tutorial: https://docs.djangoproject.com/en/2.1/intro/tutorial01/
    - This created a very simple "Hello World" app (tutorial was for polls but I adjusted)
- Started working through Part 2 of the Django tutorial: https://docs.djangoproject.com/en/2.1/intro/tutorial02/
    - Detoured to how to use the Django authentication / user framework: https://docs.djangoproject.com/en/2.1/topics/auth/

## TODO

- Add some basic functionality
    - At the point of adding admin users to the app: https://docs.djangoproject.com/en/2.1/intro/tutorial02/#introducing-the-django-admin
    - Continue learning how to use the Django authentication / user framework: https://docs.djangoproject.com/en/2.1/topics/auth/
    - Might want to try to debug something first to make sure it works?
- Add some basic tests
- Debug via PyCharm: https://www.jetbrains.com/help/pycharm/using-docker-compose-as-a-remote-interpreter.html#debug
- Figure out which files in the `./idea` folder, if any, to add to the repo (_seems like they're all machine-specific_)
- Run the containers/app and address messages that come up
    - `The psycopg2 wheel package will be renamed from release 2.8; in order to keep installing from binary please use "pip install psycopg2-binary" instead.`
- Configure web app container for when it runs
    - Automatically restart when files change
    - Apply migrations
- Setup Jenkins to build and run tests for every branch pushed
    - Must have a pull request?
    - Merge master first?
    - Tag merges into master automatically?
- Checkout the Django checklist for production deployments: https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/
- Django URL dispatcher: https://docs.djangoproject.com/en/2.1/topics/http/urls/
- Deploying Django with WSGI: https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
- Set DB password for environments (dev, staging, production)
- Reconfigure the Django app to run under a REAL web server (Apache, WSGI, nginx, ...?)
- Store DB password(s) as secrets and inject via build (CI/CD)
- Set allowed hosts, etc. in Django app
- Set favicon.ico
- Django how to install a DB: https://docs.djangoproject.com/en/2.1/topics/install/#database-installation (important?)
