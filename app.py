from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('./home.html')

@app.route('/about')
def about():
    return render_template('./about.html')

@app.route('/login')
def login():
    return render_template('./login.html')

@app.route('/signup')
def signup():
    return render_template('./signup.html')

@app.route('/games')
def games():
    return render_template('./games.html')

if __name__ == '__main__':
    app.run(debug=True)