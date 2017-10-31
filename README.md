# runserver-with-pylint
Run Django Runserver with Pylint

### Purpose: 
> runserver-with-pylint integrates pylint with django runserver, Each time python file is saved(and recompiled) on django codebase this would check PEP-8 conventions on codebase using pylint. This makes easier and faster fixes of pep8 issues while development. It also enforces PEP-8 conventions to be followed as per set standards. Whenever score goes below set standards runserver will exit till the set standards are met.

### How it works
* Use ./install.sh to install the runserver hook (All settings are present in this file)
* ERROR_COUNT, CONVENTION_COUNT, WARNINGS, CODEBASE, THRESHOLD_LINT_SCORE : These counts/score needs to be modified based on requirement.
* The script creates a file "manage_pylint.py" inside the CODEBASE directory and creates an __init__.py in order for pylint to run. (These could be added to gitignore)
* To use this run you django server as "python manage_pylint.py runserver" instead of "python manage.py runserver"

### TODO
* Copy and append requirements.txt to the project's
* Add the new added files to .gitignore (append project's existing gitignore)
* Hook to capture data to a central reporting location
* Install.sh throws error but doesn't check for it and displays "patched" message at the end. Error handling should be added
