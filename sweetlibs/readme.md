Sweet Libs Django Trial

Why did you choose this subject?  
  I chose to try Django because I heard it mentioned at a meetup I went to. I did some research and it looks like a rails counterpart that is less opinionated. The scaffolding that rails does makes life easier, but its opinions aren't always the way I want to go. I wanted to find out if django did live in that middle ground.  
How were you first made aware of it?  
  It was mentioned at a meetup and I looked into it.  
What problem does it solve?  
  django is a framework to build apps and projects in python quickly.  
How does it solve the problem (conceptually)?  
  The `manage.py` file allows for a number of functions beyond the standard python library. A user can call `createapp` or `startproject` to quickly generate views and files.  
Why does one use it?  
  One uses django to build back ends in python.  
What are the alternatives?  
  Rails is the most well known alternative.  
What is it similar to, if anything?  
  Again, Rails.  
What is the history of this technology?  
  From wikipedia:  
    "Django was born in the fall of 2003, when the web programmers at the Lawrence Journal-World newspaper, Adrian Holovaty and Simon Willison, began using Python to build applications. It was released publicly under a BSD license in July 2005. The framework was named after guitarist Django Reinhardt. In June 2008, it was announced that a newly formed Django Software Foundation (DSF) would maintain Django in the future."  
Who built it and why?  
  see above  
Who is maintaining it?  
  see above  
What is your opinion on the technology after having built something with it?  
  So far django seems to deliver on its premise of a fast framework to build database driven apps without as much convention.  
What are the biggest conceptual hurdles (if any) you encountered when researching this?  
  The greatest challenge I have encountered is working in python, a language I am unfamiliar with. At this stage, I am modeling code off of tutorials and forums, but the linguistic conventions of python are somewhat enigmatic.  
What resources do you recommend for interested students?  
  `https://docs.djangoproject.com/en/1.10/intro/tutorial01/` has been a good resource for a first time python user.  
What article or forum was most helpful to you in learning this?  
  The step by step was helpful, and there were often links for additional resources for common problems or background knowledge.  
What are 3 interview questions one might be asked about this technology?  
  I have no idea.   `http://insights.dice.com/2014/04/30/interview-questions-pythondjango-developers/` This may be a good place to look.  
Also, please include the instructions necessary to...  

Run your example.  
Do I need to run bower install? Do I need an API key?  
  to get django up and running, there are a few things you need to do.  
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
