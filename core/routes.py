from core import api
from flask import jsonify
from core.utils import get_horoscope_today, get_horoscope_tomorrow
from flask_restx import Resource, reqparse
from werkzeug.exceptions import BadRequest, NotFound
from datetime import datetime


ns = api.namespace('/', description='Horoscope API')

ZODIAC_SIGNS = {
    "Aries": 'aries',
    "Taurus": 'taurus',
    "Gemini": 'gemini',
    "Cancer": 'cancer',
    "Leo": 'leo',
    "Virgo": 'virgo',
    "Libra": 'libra',
    "Scorpio": 'scorpio',
    "Sagittarius": 'sagittarius',
    "Capricorn": 'capricorn',
    "Aquarius": 'aquarius',
    "Pisces": 'pisces',
}

parser = reqparse.RequestParser()
parser.add_argument('sign', type=str, required=True)

parser_copy = parser.copy()

@ns.route('/get-horoscope/today')
class TodaysHoroscopeAPI(Resource):
    '''Shows daily horoscope of zodiac signs'''
    @ns.doc(parser=parser_copy)
    def get(self):
        args = parser_copy.parse_args()
        zodiac_sign = args.get('sign')
        try:
            zodiac_key = ZODIAC_SIGNS[zodiac_sign.capitalize()]
            horoscope_data = get_horoscope_today(zodiac_key)
            return jsonify(success=True, data=horoscope_data, status=200)
        except KeyError:
            raise NotFound('No such zodiac sign exists')
        except AttributeError:
            raise BadRequest(
                'Something went wrong, please check the URL and the arguments.')

@ns.route('/get-horoscope/tomorrow')
class TomorrowsHoroscopeAPI(Resource):
    '''Shows weekly horoscope of zodiac signs'''
    @ns.doc(parser=parser)
    def get(self):
        args = parser_copy.parse_args()
        zodiac_sign = args.get('sign')
        try:
            zodiac_key = ZODIAC_SIGNS[zodiac_sign.capitalize()]
            horoscope_data = get_horoscope_tomorrow(zodiac_key)
            return jsonify(success=True, data=horoscope_data, status=200)
        except KeyError:
            raise NotFound('No such zodiac sign exists')
        except AttributeError:
            raise BadRequest(
                'Something went wrong, please check the URL and the arguments.')

