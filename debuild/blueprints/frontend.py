#

from jinja2 import TemplateNotFound
from flask import Blueprint


frontend = Blueprint('frontend', __name__, template_folder='templates')