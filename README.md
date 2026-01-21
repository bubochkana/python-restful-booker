Prerequisites:
1. Python should be installed (python = ">=3.10,<3.13.5")
2. Git should be installed 
3. PyCharm should be installed

Instructions:
1. Clone the project:
   - git clone https://github.com/bubochkana/python-restful-booker
   - cd python-restful-booker
2. Install all dependencies with poetry:
   - poetry install --with dev

Enable pre-commit configuration:
1. Copy pre-commit configuration file to the .git/hooks:
   - Windows: copy /pre-commit/windows/pre-commit .git/hooks
   - macOS/Linux: copy /pre-commit/windows/pre-commit .git/hooks
2. Execute the command to grand the permission to the pre-commit file:
   - chmod +x .git/hooks/pre-commit
3. Check the permission  are properly assigned - the result should be -rwxr-xr-x:
   -  ls -l .git/hooks/pre-commit
4. Install hook dependencies:
   - poetry run pre-commit install --install-hooks

Hints:
1. To install a new lib, execute the command below. This will add colorlog as a dependency to your pyproject.toml file and update your poetry.lock file. :
   - poetry add <lib_name>
2. To run ruff checks execute the command:
   - poetry run ruff check .
3. To run ruff checks and fix the formatting within the check running (indentation, line length, etc.) execute the command:
   - poetry run ruff check . --fix
4. To manually update the poetry.lock file execute the command:
   - poetry lock