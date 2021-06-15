from flask import Flask,render_template

app = Flask(__name__)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/reg')
def reg():
    return render_template('reg.html')

if __name__ == '__main__':
    app.run(debug=True,port='8080')
