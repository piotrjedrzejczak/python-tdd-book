# Set up venv: $ py -3.7 -m venv virtualenv
# Install django and selenium: $ pip install "django" "selenium"
# Start with creating the app by : $ django-admin startproject <projectname> .
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
    - Once you have both functional test and unittest failing, you start writing production code that will pass the unittest. You might bounce around 2 & 3 because there is more than one thing failing in the unittest - that's good, don't try to fix everything at once, fix one error at a time.
    - Now rerun the functional test to see if it passes.

    > the idea here is for the functional test to drive the high level development and the unittest the explicit implementation.


