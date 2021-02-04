# Set up venv: $ py -3.7 -m venv virtualenv
# Install django and selenium: $ pip install "django" "selenium"
# Start with creating the app by : $ django-admin startproject <projectname> .
# add the app to INSTALLED_APPS in settings.py
# Try running the app with: $ python manage.py runserver
# git init your repository
# create .gitignore
# ready for first commit: $ git add .
# to unstage: git rm -r --cached <filename>
# git commit
# hook repo to github
# start a new app in the top level dir with: $ python manage.py startapp <appname>
# git status & git diff --staged // remember to always see what you are about to commit
# git commit -m "Pass a nice message here"
# from now on our development cycle will look like this:
    - Write a functional test (user story)
    - Try to figure out what to write to make that test pass, and then start writing a unittest for it.
    - Once you have both functional test and unittest failing, you start writing minimal production code that will try to resolve the error that you are currently facing from the unittest. You might bounce around 2 & 3 because there is more than one thing failing in the unittest - that's good, don't try to fix everything at once, fix one error at a time.
    - Now rerun the functional test to see if it passes.

    > the idea here is for the functional test to drive the high level development and the unittest the explicit implementation.

![image info](./images/tdd.png)

# passed unittest is a nice point to commit
# if the changes made are in tracked files just do : $ git commit -am "First unittest passed"
# don't test constants in unittests
# don't refactor without tests
# database migrations
# unittest best practice - each test should test one thing only
# always redirect after POST
# nice list of code smells -> https://blog.codinghorror.com/code-smells/
# have a todo list - its good for you
# $ python manage.py test <app_name> or <package_name>

- ensure test isolation and managing global state - Different tests shouldn’t affect one another. This means we need to reset any permanent state at the end of each test. Django’s test runner helps us do this by creating a test database, which it wipes clean in between each tes

- avoid voodoo sleeps

- don't rely on selenium implicit waits

