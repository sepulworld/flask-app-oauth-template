#!/bin/bash
exec gunicorn --worker-tmp-dir /dev/shm --preload -w 3 --timeout 200 -b :5000 --access-logfile - --error-logfile - {{ cookiecutter.app }}:app
