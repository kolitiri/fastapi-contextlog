# Description

A simple example on how to integrate the contextlogger package in a Fastapi app for contextual and structured logging.

It builds on top of the basic example that is provided in the **FastApi** documentation [here](https://fastapi.tiangolo.com/).

If you are interested in the **contextlogger** package you can find it [here](https://pypi.org/project/contextlogger/).


# Requirements

To run this example as is, you will need pipenv installed on your machine.
```
pip install pipenv
```

Alternatively you can pip install the following packages globally or in a virtual env (better)
1. fastapi
2. uvicorn[standard]
3. contextlogger


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