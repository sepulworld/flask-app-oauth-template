# flask-app-oauth-template

Flask app template with oauth scaffolding in place 


## Requirements

* [python3](https://www.python.org/downloads/)
* [Poetry](https://python-poetry.org)
* [Tilt](https://tilt.dev)
* [Docker](https://docker.com)
* [Kubernetes](https://kubernetes.io) - (Minikube, Docker for Mac K8s enabled, Kind, etc)

## Install Python Poetry and Tilt
```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
curl -fsSL https://raw.githubusercontent.com/tilt-dev/tilt/master/scripts/install.sh | bash
```

## Setup new app and start local development (helloworld example app)
```
git clone https://github.com/sepulworld/flask-app-oauth-template.git
cd flask-app-oauth-template
poetry install
poetry shell
cd ..
battenberg -O helloworld install --initial-branch main git@github.com:sepulworld/flask-app-oauth-template.git 
cd helloworld 
tilt up
```

## Create Python Flask app via Battenberg

Will generate application git repo with initial scaffolding and user signup, login interface points

```
./helloworld/
├── CHANGELOG.md
├── DEVELOPMENT.md
├── Dockerfile
├── LICENSE
├── README.md
├── Tiltfile
├── app
│   ├── __init__.py
│   ├── api
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── errors.py
│   │   ├── tokens.py
│   │   └── users.py
│   ├── auth
│   │   ├── __init__.py
│   │   ├── email.py
│   │   ├── forms.py
│   │   └── routes.py
│   ├── email.py
│   ├── errors
│   │   ├── __init__.py
│   │   └── handlers.py
│   ├── main
│   │   ├── __init__.py
│   │   ├── forms.py
│   │   └── routes.py
│   ├── models.py
│   └── templates
│       ├── auth
│       │   ├── login.html
│       │   ├── register.html
│       │   ├── reset_password.html
│       │   └── reset_password_request.html
│       ├── base.html
│       ├── errors
│       │   ├── 404.html
│       │   └── 500.html
│       ├── index.html
│       └── user.html
├── boot.sh
├── config.py
├── local_dev
│   └── local.yaml
├── helloworld.py
└── pyproject.toml
```

### Tilt Local Development

```
tilt up
```

#### Battenbug Upgrades Process 

If you want to sync new changes from flask-app-template to your app
 
```
git branch template main 
git checkout -b template_sync
battenberg upgrade
```

#### What is Battenberg?

https://github.com/zillow/battenberg#battenberg
