import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model



from flask import Flask, Response, jsonify

app = Flask(__name__)

max_length = 150
truc_type = 'post'
padding_type = 'post'


model = load_model("model.h5")
tokenizer = open("tokenizer.pickle", "rb")
tokenizer = pickle.load(tokenizer)


def get_offensiveness(data):
    sentence = [""]
    sentence[0] = data
    sequences = tokenizer.texts_to_sequences(sentence)
    padded = pad_sequences(sequences, maxlen=max_length,
                           padding=padding_type, truncating=truc_type)
    return model.predict(padded)

@app.route('/predict/<string:offensive_text>', methods=['GET'])
def region(offensive_text):
    print(offensive_text)
    pred = get_offensiveness(offensive_text)[0][0]
    response = {}
    if pred > 0.75:
        response['status'] = "success"
        response['value'] = str(pred)
        response['isOffensive'] = True
    else:
        response['status'] = "success"
        response['value'] = str(pred)
        response['isOffensive'] = False
    
    return jsonify(response)
        



app.run(host='0.0.0.0', port=80)