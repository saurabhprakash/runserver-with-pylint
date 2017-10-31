import os
from string import Template
from shutil import copyfile


template_str = Template('''#!/usr/bin/env python
import os
import sys
from pylint.lint import Run

ERROR_COUNT = $error_count
CONVENTION_COUNT = $convention_count
WARNINGS = $warnings
CODEBASE = '$codebase'
THRESHOLD_LINT_SCORE = $threshold_lint_score

def run_pylint():
    """Runs Pylint on codebase and updates with status of files"""
    results = Run(['--load-plugins=pylint_django', '--rcfile=pylintrc', CODEBASE], exit=False)
    if results.linter.stats['error'] > ERROR_COUNT or results.linter.stats['convention'] > CONVENTION_COUNT or \\
            results.linter.stats['warning'] > WARNINGS or results.linter.stats['global_note'] < THRESHOLD_LINT_SCORE:
        print("Codebase has failed set standards, Please correct above mentioned issues,"
              "Current Score is: %s, Errors: %s, Convention issues: %s, Warnings: %s" % (\\
            results.linter.stats['global_note'], results.linter.stats['error'], results.linter.stats['convention'],
            results.linter.stats['warning']))
        sys.exit(0)
if os.environ.get('RUN_MAIN') != 'true':
    try:
        run_pylint()
    except:
        import traceback
        print(traceback.format_exc())
        sys.exit(0)
''')

ERROR_COUNT = os.environ['ERROR_COUNT']
CONVENTION_COUNT = os.environ['CONVENTION_COUNT']
WARNINGS = os.environ['WARNINGS']
CODEBASE = os.environ['CODEBASE']
THRESHOLD_LINT_SCORE = os.environ['THRESHOLD_LINT_SCORE']

template_str = template_str.substitute(error_count=ERROR_COUNT, convention_count=CONVENTION_COUNT,
    warnings=WARNINGS, codebase=CODEBASE, threshold_lint_score=THRESHOLD_LINT_SCORE)


with open(os.path.join(CODEBASE, "manage.py") , 'r') as manage_file:
    manage_content = manage_file.read()

with open(os.path.join(CODEBASE, "manage_pylint.py"), "w") as text_file:
    text_file.write(template_str + manage_content)

# Touch a __init__.py
open(os.path.join(CODEBASE, "__init__.py"), "a").close()

copyfile("pylintrc", os.path.join(CODEBASE, "pylintrc"))
