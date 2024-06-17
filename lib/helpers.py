import re
import random
import string
from datetime import datetime

def format_datetime(dt):
    """
    Format a datetime object as a string in the format 'YYYY-MM-DD HH:MM'.
    """
    return dt.strftime('%Y-%m-%d %H:%M')

def parse_datetime(dt_str):
    """
    Parse a datetime string in the format 'YYYY-MM-DD HH:MM' and return a datetime object.
    """
    return datetime.strptime(dt_str, '%Y-%m-%d %H:%M')

def validate_email(email):
    """
    Validate an email address using regular expression.
    """
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(email_regex, email) is not None

def generate_confirmation_code(length=6):
    """
    Generate a random confirmation code of specified length.
    """
    characters = string.ascii_uppercase + string.digits
    confirmation_code = ''.join(random.choice(characters) for _ in range(length))
    return confirmation_code