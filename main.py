from replit import web
import flask
from flask import render_template

app=flask.Flask(__name__)
h = {
  "score" : 0,
  "name" : "FIS",
  "colour" : "#874146"
}
away = {
  "score" : 0,
  "name" : "Away",
  "colour" : "#000000"
}

print(h["colour"])

@app.route("/")
def index():
  bgcolour = h["colour"]
  return render_template('obs.html', colour=bgcolour)

#@app.route("/obs")
#def home():
#  name = "test"
  #return render_template('obs.html', name=name)

web.run(app)

