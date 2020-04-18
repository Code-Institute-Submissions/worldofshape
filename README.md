# Welcome to the **"World of Shape"**

![alt text](https://github.com/MrBrunotte/worldofshape/blob/master/static/images/landingpage.png "World of Shape")

[![Build Status](https://travis-ci.org/MrBrunotte/worldofshape.svg?branch=master)](https://travis-ci.org/MrBrunotte/worldofshape)

**World of Shape - Your journey starts now!**


## **Testing**

### Travis CI - platform

### What is CI - Continuous Integration?

I have used the practice of CI (Continuous Integration), which is the the practice of merging in small code changes frequently - rather than merging in a large change at the end of a development cycle. The goal is to build healthier software by developing and testing in smaller increments. 
As a continuous integration platform, Travis CI supports your development process by automatically building and testing code changes, providing immediate feedback on the success of the change. Travis CI can also automate other parts of your development process by managing deployments and notifications.

### CI Builds and Automation: Building, Testing, Deploying

When you run a build, Travis CI clones your GitHub repository into a brand-new virtual environment, and carries out a series of tasks to build and test your code. If one or more of those tasks fail, the build is considered **broken**. If none of the tasks fail, the build is considered **passed** and Travis CI can deploy your code to a web server or application host.

## AUTOMATED TESTING 

### Coverage

I have used the package 'coverage' to see how effective my testing is. 
I installed the covarage package with 'pip install coverage' and then I ran 'Coverage' and created a covhtml file.

run with:   coverage run --source='users' manage.py test && coverage report && coverage html
            Go to the htmlcov file and run the index file to get the report.
and:        python manage.py test users
    
**"coverage run --source='users' manage.py test && coverage report && coverage html"**


[Automated testing results](static/img/automated_testing_results.PNG)

## SETTING UP URLs

Steps to set up url patterns and getting it to work!

**Testimonials example**
1)  Create html page - set Codeblock and DOCTYPE
2) Go to Project urls (WorldofShape) and set urlpattern: path('testimonials/', home_views.contact, name='testimonials'),
3) Go to Home/Views: def testimonials(request):
    """ Contact view takes us to our contactpage """
    return render(request, 'home/testimonials.html')
4) Set urlpattern in Home: path('testimonials/', views.testimonials,
         name='testimonials'),  # from contact view
