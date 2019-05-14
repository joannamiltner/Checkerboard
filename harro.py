from flask import Flask, render_template
app = Flask(__name__)


@app.route('/checkcheck')
def checkcheck():
    print("*"*80)
    print("oooooo how's that checkerboard doin gurl?")
    return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True)
