from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def inherits():
    return render_template('base.html')

@app.route('/inherits1/')
def inherits_one():
    return render_template('inherits1.html')

@app.route('/inherits2/')
def inherits_two():
    return render_template('inherits2.html')

if __name__ == ("__main__"):
    app.run(host='0.0.0.0',debug=True)
