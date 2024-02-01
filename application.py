from flask import Flask, jsonify, request
from flask_cors import CORS
import sys
from chatbot import predict_class, get_response
import json
app = Flask(__name__)
CORS(app)
intents = json.loads(open('intent.json', 'r').read())
# questions = [
#     {
#         'question': 'What is the worlds best tv show?',
#         'user': [
#             {
#                 'name': 'Walter',
#                 'age': 54
#             }
#         ]
#     },
#     {
#         'question': 'How to get good grades in Computer Science?',
#         'user': [
#             {
#                 'name': 'Marcus',
#                 'age': 20
#             }
#         ]
#     }
# ]

def answer_pablo(msg):
    ints = predict_class(msg)
    print(ints, file=sys.stderr)
    res = get_response(ints, intents)
    return res

@app.route('/')
def home() : 
    return 'Hey from our RestfulAPI!'


@app.route('/question', methods = ['POST'])
def ask_question() :
    print(request, file=sys.stderr)
    request_data = request.json
    print(request_data, file=sys.stderr)
    answer = {
        'Content-Type': 'application/json',
        'response' : answer_pablo(request_data['text']),
    }

    return jsonify(answer)

app.run(port = 8003)

# @app.route('/question/<string:name>')
# def get_question(name) :
#     for question in questions : 
#         if question['name'] == name :
#             return jsonify(question)
        
#     return jsonify({'mesage': 'question not found!'})


# @app.route('/question')
# def get_all_questions() : 
#     return jsonify({'questions': questions})


# @app.route('/question/<string:name>/user', methods = ['POST'])
# def create_question_user(name) :
#     request_data = request.get_json() 

#     for question in questions :
#         if question['name'] == name :
#             new_user = {
#                 'name': request_data['name'],
#                 'age': request_data['age']
#             }

#             question['users'].append(new_user)

#             return jsonify(new_user)
        
#     return jsonify({'message': 'question no found!'})


# @app.route('/question/<string:name>/user')
# def get_question_user(name) :
#     for question in questions :
#         if question['name'] == name :
#             return jsonify(question['user'])
        
#     return jsonify({'message': 'question not found!'})