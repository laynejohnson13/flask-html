from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template ('home_css.html')

@app.route('/page2')
def dashboard():
    return render_template('page2_css.html')

if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0', port=80)