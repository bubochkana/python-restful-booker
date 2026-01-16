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
3. Check the permission  are properly assigned - the result should be -rwxr-xr-x):
   -  ls -l .git/hooks/pre-commit
4. Install hook dependencies:
   - poetry run pre-commit install --install-hooks