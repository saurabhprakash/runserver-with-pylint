# runserver-with-pylint
Run Django Runserver with Pylint

### Purpose: 
> runserver-with-pylint integrates pylint with django runserver, Each time python file is saved(and recompiled) on django codebase this would check PEP-8 conventions on codebase using pylint. This makes easier and faster fixes of pep8 issues while development. It also enforces PEP-8 conventions to be followed as per set standards. Whenever score goes below set standards runserver will exit till the set standards are met.

### How it works
* In you root directory of codebase where manage.py is present add the "pylintrc" file, This file can be modified as per requirements
* In one of you django apps, add "runserver_with_pylint.py" file on location "[your app name]/management/commands/runserver_with_pylint.py", make sure this app is present in installed apps.
* In above mentioned file(runserver_with_pylint.py), set your required standards by modifying these set of variables: ERROR_COUNT, CONVENTION_COUNT, WARNINGS, CODEBASE, THRESHOLD_LINT_SCORE
* To use this run you django server as "python manage.py runserver_with_pylint" instead of "python manage.py runserver"

### Dependencies
* pylint-django (0.7.2)
* pylint (1.5.0)
