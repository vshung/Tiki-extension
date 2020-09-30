from flask import Blueprint


bp = Blueprint('tiki', __name__)
from . import views
