from flask import Flask
from decouple import config
from flask_restx import Api

app = Flask(__name__)
app.config.from_object(config("APP_SETTINGS"))
api = Api(
    app,
    version='1.0',
    title='Horoscope API',
    description='Check your daily horoscope with the API below!',
    license='MIT',
    contact='Meg',
    contact_email='misrani@depaul.edu',
    doc='/',
    prefix='/api/v1'
)

from core import routes	
