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
- Bootstrap / HTML 5 / CSS 3 (?)

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

- Install Git for Windows
- Create the GitHub repository (and clone it locally)
- Upgrade to Windows 10 Pro
- Install Docker Desktop for Windows
- Install PyCharm (Pro; free eval)
- Bootstrap a Django project in Docker: https://docs.docker.com/compose/django/
    - Add the PostgreSQL client to the app image: https://hub.docker.com/_/django/

## TODO

- Get going in PyCharm: https://www.jetbrains.com/help/pycharm/using-docker-compose-as-a-remote-interpreter.html
- Run the containers/app and address messages that come up
- Set DB password and access
- Set allowed hosts, etc. in Django app
- Set favicon.ico
