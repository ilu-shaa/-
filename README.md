It is necessary to install: 
Django==5.0.6
PyMySQL==1.1.1
sympy==1.12.1

If you are already in the inner environment:
$ py manage.py runserver

if the project is launched from a device without an internal environment, then you should:
1) pip install pipenv
2) pipenv install
3) pipenv shell
4)  pip3 install django (if necessary)
5)  pipenv run manage.py runserver
