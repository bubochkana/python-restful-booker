1. Install Python
2. Install Git
3. Install PyCharm
4. Download the project from git https://github.com/bubochkana/python-restful-booker
5. Install all dependencies with poetry
6. Execute chmod +x .git/hooks/pre-commit
7. Check the permission  are properly assigned -  ls -l .git/hooks/pre-commit (the result should be -rwxr-xr-x)
8. Install poetry - poetry install --with dev
9. Install hook dependencies - poetry run pre-commit install --install-hooks