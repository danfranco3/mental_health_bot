# Team 7 Mental Health Bot: Dr. Pablo!

This is our entry for the 2023 UPdate Hackathon promoted by Critical Techworks.

Built with flutter and Python, this bot uses tensorflow as the main library for training and hard-coded intents to assist on correctly answering the user's queries.

This bot is very scalable, as it is built with an API (constructed with flask in Python) and operates through a REST API model.

The API only has one endpoint, /question, through which users can query the bot.

It also has a simple but pleasant-looking interface built with flutter, which is a great addition to the usability of this bot, since the app can be ported to web, Android and iOS.

Dr. Pablo has been tested in Chrome and iOS and perfomed well on both platforms.

## Libraries

To compile this bot you must have installed:

Tensorflow >= 2.11.0

Numpy >= 2.4

Nltk

flask and flask_cors

## Usage

First, you need to run the application.py file and check the IP address on the terminal. Then, go to main.dart inside the lib folder, and check whether the IP inside the _getResponse method is the same as the shown by the API.

Then you can run the app itself, after correctly installing and running flutter doctor to make sure everything is okay :), by start debugging through vscode and selecting your platform of choice.

Have fun!
