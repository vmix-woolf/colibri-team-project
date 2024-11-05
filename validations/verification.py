import re
import calendar

from messages.constants import Constants


def name_validation(name):
    return True if bool(re.match(r'[A-Za-z]{2,20}', name)) else False