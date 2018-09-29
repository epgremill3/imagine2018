# Bootstrapping a Professional Software Project

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
- _I may come back later and undo the model, etc. that I created, but for now..._
- Added some issues to the GitHub repo:
    - Created three milestones (Phase 1, 2, and 3)
    - Added 11 issues for the functionality we'll want to add in Phase 1
    - Didn't get to modifying labels yet
- Experimented with protecting master. It was easy - just go into settings, click on Branches, then check the boxes you want...
- Signed up for a free tier AWS account. Had to enter a credit card number so don't recommend they do it too, but will show and tell...
- Setting up a web app in Elastic Beanstalk
    - Tried setting up a Docker app but couldn't quickly get it to work, so...
    - [Create an access key for the Administrator IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey)
    - _Did the following in the Docker web container (can always downw/up to undo it)_
    - [Install EB CLI](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install.html)
    - [Configure the Python project for Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/python-development-environment.html#python-common-configuring)
        - Region 1 (US East N. Virginia)
        - Entered access key ID and secret
        - Application name: imagine2018
        - Docker platform version: Docker 18.06.1-ce (default)
        - Said no to CodeCommit
        - Said yes to SSH
            - Keypair name: imagine2018-aws-eb
            - Used a blank passphrase
    - [Configure the Django Application for Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html#python-django-configure-for-eb)
        - Added /.ebextensions/django.config
        - Created `imagine2018-staging-01` environment with `eb create`
        - Added the CNAME (from `eb status`) to `imagine2018/settings.py`
        - Copied the `Dockerrun.aws.json` file from the downloaded sample app to the root project directory and modified
        - Tried again with `eb deploy`
        - Found out that if you're using Git EB only deploys committed files, so you either have to stage changed/added files and do `eb deploy --staged` or commit then do `eb deploy`...!
        - Had problems with `Dockerrun.aws.json` and `Dockerfile` so read about [single container docker deployments in EG](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_docker_image.html)
        - ...
    - Try to get to the RDS DB too: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.RDS.html
- That was taking a while so per [this page](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html) I set up an admin group and user
    - Custom password: ItsASecret! and don't require reset...

## TODO

- Add some basic functionality
    - At the point of adding admin users to the app: https://docs.djangoproject.com/en/2.1/intro/tutorial02/#introducing-the-django-admin
    - Continue learning how to use the Django authentication / user framework: https://docs.djangoproject.com/en/2.1/topics/auth/
    - Might want to try to debug something first to make sure it works?
- Add some basic tests
- Debug via PyCharm: https://www.jetbrains.com/help/pycharm/using-docker-compose-as-a-remote-interpreter.html#debug
- In your "free" AWS account:
    - Deploy to ECS: https://aws.amazon.com/getting-started/tutorials/deploy-docker-containers/
    - Create a Docker Registry: https://docs.aws.amazon.com/AmazonECR/latest/userguide/ECR_GetStarted.html
    - Build an image and push it to the Docker Registry (_is this still free?_)
    - Deploy to RDS: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.PostgreSQL.html
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
