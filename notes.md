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

# do the user input validation at db layer - its the safest option, unless there is a very good reason to do it elsewhere

# One of the reasons that the "three strikes and refactor" rule exists is that, if you wait until you have three use cases, each might be slightly different, and it gives you a better view for what the common functionality is. If you refactor too early, you may find that the third use case doesn’t quite fit with your refactored code…​

# checkout django-crispy-forms or django-floppyforms


# Thin views
If you find yourself looking at complex views, and having to write a lot of tests for them, it’s time to start thinking about whether that logic could be moved elsewhere: possibly to a form, like we’ve done here.

Another possible place would be a custom method on the model class. And—​once the complexity of the app demands it—​out of Django-specific files and into your own classes and functions, that capture your core business logic.

# Each test should test one thing
The heuristic is to be suspicious if there’s more than one assertion in a test. Sometimes two assertions are closely related, so they belong together. But often your first draft of a test ends up testing multiple behaviours, and it’s worth rewriting it as several tests. Helper functions can keep them from getting too bloated.

# some testing alternatives
- nose https://nose.readthedocs.io/en/latest/
- green https://github.com/CleanCut/green
- pytest https://docs.pytest.org/en/stable/

# js testing pitfalls

fixtures, execution order and global state
One of the difficulties with JavaScript in general, and testing in particular, is in understanding the order of execution of our code (i.e., what happens when). When does our code in list.js run, and when does each of our tests run? And how does that interact with global state, that is, the DOM of our web page, and the fixtures that we’ve already seen are supposed to be cleaned up after each test?