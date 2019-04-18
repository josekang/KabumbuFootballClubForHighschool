###########################################################
#### CRAETE THE NECCESSARY IMPORTS FOR THE ENTIRE APP #####
###########################################################

from flask import render_template
from myproject import app

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")

if __name__ == '__main__':
    app.run(debug = True, port = 5000)
