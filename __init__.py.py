from flask import Blueprint

main = Blueprint('main', __name__)

# استيراد جميع المسارات
from . import routes