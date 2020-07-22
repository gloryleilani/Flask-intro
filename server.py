"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return "<!doctype html><html>Hi! <a href='/hello'> This is the hello page. </a> And the rest of this page is the home page.</html>"


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? 
          <input type="text" name="person">
          
          Select a compliement:
          <select name = "compliment">
            <option value="spiffy">Spiffy!</option>
            <option value="coolio">Coolio!</option>
          </select>
          Select an insult:
          <select name = "diss">
            <option value="not spiffy">not spiffy!</option>
            <option value="not coolio">not coolio!</option>
          </select>

          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person") #Get name data from HTTP comm query string

    compliment = request.args.get("compliment") #Get data from HTTP comm query string

    diss = request.args.get("diss") #Get data from HTTP comm query string

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment and Insult</title>
      </head>
      <body>
        Hi, {}! I think you're usually {} but occasionally {}!
      </body>
    </html>
    """.format(player, compliment, diss)


@app.route('/diss')
def diss_person():
    """Insult the person by name."""


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
