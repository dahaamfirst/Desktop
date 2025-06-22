# تأكد من أن لديك مسارات معرّفة مثل
@app.route('/manage_request')
def manage_request():
    return render_template('manage_request.html')

@app.route('/eda')
def eda():
    return render_template('eda.html')

@app.route('/metrics_page')
def metrics_page():
    return render_template('metrics_page.html')