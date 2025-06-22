import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.middleware.proxy_fix import ProxyFix

db = SQLAlchemy()

def create_app():
    # إنشاء تطبيق Flask
    app = Flask(__name__)
    
    # إصلاح مشكلة البروكسي
    app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)
    
    # تكوين التطبيق
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
    
    # تكوين قاعدة البيانات - مع معالجة آمنة لسلسلة الاتصال
    database_url = os.environ.get('DATABASE_URL')
    if database_url:
        if database_url.startswith('postgres://'):
            database_url = database_url.replace('postgres://', 'postgresql://', 1)
        app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    else:
        # استخدام قاعدة بيانات SQLite للتطوير إذا لم يتم توفير DATABASE_URL
        basedir = os.path.abspath(os.path.dirname(__file__))
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # تهيئة SQLAlchemy
    db.init_app(app)
    
    # تسجيل النماذج (Blueprints)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    # إنشاء جداول قاعدة البيانات إذا لزم الأمر
    with app.app_context():
        db.create_all()
    
    return app