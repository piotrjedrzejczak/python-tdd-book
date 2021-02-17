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

# YAGNI - You ain't gonna need it
- As software developers, we have fun creating things, and sometimes it’s hard to resist the urge to build things just because an idea occurred to us and we might need it. The trouble is that more often than not, no matter how cool the idea was, you won’t end up using it. Instead you have a load of unused code, adding to the complexity of your application. YAGNI is the mantra we use to resist our overenthusiastic creative urges.

# convention of double hashes (##) - used for "meta comments" - explaining how and why the FT is setup in a cerrtain way unlike the normal comments representing the user story


# Some More TDD Philosophy

# Working State to Working State (aka The Testing Goat vs. Refactoring Cat)

    - Our natural urge is often to dive in and fix everything at once…​but if we’re not careful, we’ll end up like Refactoring Cat, in a situation with loads of changes to our code and nothing working. The Testing Goat encourages us to take one step at a time, and go from working state to working state.

# Split work out into small, achievable tasks

    - Sometimes this means starting with "boring" work rather than diving straight in with the fun stuff, but you’ll have to trust that YOLO-you in the parallel universe is probably having a bad time, having broken everything, and struggling to get the app working again.

# YAGNI

    - You ain’t gonna need it! Avoid the temptation to write code that you think might be useful, just because it suggests itself at the time. Chances are, you won’t use it, or you won’t have anticipated your future requirements correctly. See [chapter_outside_in] for one methodology that helps us avoid this trap.

# Genereally you shouldn't test static files, but including small test of few components will help detect if the stylesheets have loaded

# Don't use python to serve static files, let the nginx or apache serve them for you
# Use 'collectstatic' to gather up all your static files from various folders

# red -> green -> refactor!
