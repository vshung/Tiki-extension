from flask import Blueprint


bp = Blueprint('hello', __name__)
from app.hello import views
