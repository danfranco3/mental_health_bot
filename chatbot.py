import json
import random
import pickle
import numpy as np
import nltk
from textblob import TextBlob
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('wordnet')

from tensorflow.keras.models import load_model

lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intent.json', 'r').read())
coping_strategies = json.loads(open('coping_strategies.json', 'r').read())

words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbotmodel.h5')

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    serntece_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words


def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0]* len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    bagofwords = bag_of_words(sentence)
    res = model.predict(np.array([bagofwords]))[0]
    ERROR_THRESHOLD = 0.01
    results = [[i,r] for i, r in enumerate(res) if r> ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    print(results)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list



def get_response(intents_list, intents_json):
    result = ""
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if tag == "suggestions":
            for s in i['suggestions']:
                tag2 = ""
                try:
                    tag2 = intents_list[1]['intent']
                    if tag2 == s['tag']:
                        coping_strategy = random.choice(s['coping_strategies'])
                        result = "Sure! Here's something you might find helpful for that:"  + coping_strategy
                        return result
                except IndexError:
                    try:
                        coping_strategy = random.choice(s['coping_strategies'])
                        result = "Here's something you might find helpful: " + coping_strategy
                        return result
                    except KeyError:
                        continue
        if i['tag'] == tag:
            sentiment = TextBlob(tag).sentiment.polarity
            if sentiment > 0:
                result = random.choice(i['positive_responses'])
            elif sentiment < 0:
                result = random.choice(i['negative_responses'])
            else:
                result = random.choice(i['neutral_responses'])
    return result


# while True:
#     message = input('')
#     ints = predict_class(message)
#     res = get_response(ints, intents)
#     print(res)
