from flask import render_template, session, redirect, url_for
from .. import db
from . import main

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/manage_request')
def manage_request():
    # تأكد من تسجيل دخول المستخدم
    if 'email' not in session:
        return redirect(url_for('main.login'))
    return render_template('manage_request.html')

@main.route('/eda')
def eda():
    # تأكد من تسجيل دخول المستخدم
    if 'email' not in session:
        return redirect(url_for('main.login'))
    return render_template('eda.html')

@main.route('/metrics_page')
def metrics_page():
    # تأكد من تسجيل دخول المستخدم
    if 'email' not in session:
        return redirect(url_for('main.login'))
    return render_template('metrics_page.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    # تنفيذ منطق تسجيل الدخول هنا
    return render_template('login.html')

@main.route('/signup', methods=['GET', 'POST'])
def signup():
    # تنفيذ منطق إنشاء الحساب هنا
    return render_template('signup.html')

@main.route('/logout')
def logout():
    # مسح بيانات الجلسة
    session.pop('email', None)
    return redirect(url_for('main.home'))