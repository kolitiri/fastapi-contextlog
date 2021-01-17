# Description

A simple example on how to integrate the **[contextlogger](https://pypi.org/project/contextlogger/)** package in a **[FastApi](https://fastapi.tiangolo.com/)** app for contextual and structured logging.

It builds on top of the basic example that is provided in the **[FastApi](https://fastapi.tiangolo.com/)** documentation, so hopefully it looks familiar.



# Requirements

To run this example as is, you will need pipenv installed on your machine.
```
pip install pipenv
```

Alternatively you can pip install the following packages globally or in a virtual env (better)
```
pip install fastapi
pip install uvicorn[standard]
pip install contextlogger
```


# Usage

If you installed pipenv:
```
cd fastapi-contextlog/

pipenv install
pipenv run uvicorn my_app.main:app
```

If you pip installed the packages globally:
```
cd fastapi-contextlog/

uvicorn my_app.main:app
```


# Docs
1. FastApi [documentation](https://fastapi.tiangolo.com/)
2. contextlogger [documentation](https://pypi.org/project/contextlogger/)


# License
This project is licensed under the terms of the MIT license.


# Authors
Christos Liontos