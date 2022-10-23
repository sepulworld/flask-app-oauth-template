import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    # Insert your emails for admins in this list
    ADMINS = ['']
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'
    APP_STATE = 'ApplicationState'
    NONCE = 'SampleNonce'
