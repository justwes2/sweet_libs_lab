Sweet Libs Django Trial


  Based on the project at `https://docs.djangoproject.com/en/1.10/intro/tutorial01/` I am working with django for the first time.

  To get django up and running, there are a few things you need to do.  
  1) Install python. WDI students do this during installfest, but you can always go to `python.org` to download the most up to date version (there are some backwards compatiblity issues, and I was running an older version (2.7.10) without issues so far).
  2) Install pip- a python package manager. The way that I got this to work was `sudo easy_install pip` although there are other ways to do it.
  3) Install django. Again, I used `sudo pip install Django` to get around some permissions errors, but you may not need to.
  4) Once you are in the directory you want to turn into a project, run `django-admin startproject projectname` to initialize a file with the root information.
  5) From inside the root project directory, run `python manage.py runserver` to start a development server. Once the server is up, you can navigate on your browser to ` http://localhost:8000/` and you will see the django start page.
  6) Next you will create an app. In django, apps are nested in projects, so an app can be a part of a larger root file. For example, a project may have a blog app, a gallary app, and a store app. Inside the root project directory, run `pythin manage.py startapp appname`. This will generate a subdirectory with a new set of files for that specific app. From here, steps will direct to different file paths were comments will walk through the code.
  7) In `sweetlibs/polls/views.py`
  8) You will have to create `sweetlibs/polls/urls.py` manually.
  9) In `sweetlibs/urls.py`
  10) At this point, you can see your index page text rendering at `http://localhost:8000/polls/`
Use your subject.
Do I need to include it in my HTML with <script> tags? Do I need to brew install anything? Can I deploy it to Heroku?
