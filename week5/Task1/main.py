from flask import Flask, render_template
app = Flask(__name__)

@app.route('/users/')
def users():
    names = ['simon','thomas','lee']
    return render_template('template.html', names=names)

if __name__ == "__main__0":
    app.run(host='0.0.0.0',debug=True)
