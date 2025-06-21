import os
from flask import Flask, render_template
import psycopg2  # لربط PostgreSQL

app = Flask(__name__)

# تكوين قاعدة البيانات - سيتم استبدالها بمتغير البيئة
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '').replace("postgres://", "postgresql://", 1)
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists("app/build/" + path):
        return send_from_directory('app/build', path)
    else:
        return send_from_directory('app/build', 'index.html')
@app.route('/')
def home():
    """الصفحة الرئيسية"""
    try:
        # اختبار اتصال قاعدة البيانات
        conn = psycopg2.connect(app.config['SQLALCHEMY_DATABASE_URI'])
        conn.close()
        db_status = "الاتصال بنجاح"
    except:
        db_status = "فشل الاتصال"
    
    return render_template('index.html', db_status=db_status)

@app.route('/predict', methods=['POST'])
def predict():
    """نموذج التنبؤ"""
    # كود معالجة النموذج هنا
    return "نتيجة التنبؤ"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)