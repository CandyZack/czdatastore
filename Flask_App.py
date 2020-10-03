# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
import pickle

try:
    pickle_in = open('datastore.pickle','rb')
    Dict = pickle.load(pickle_in)
except:
    Dict={}

app = Flask(__name__)


#SET
@app.route('/set/<string:key>:<string:value>',methods=['GET'])
def set_value(key,value):
    global Dict
    msg = str(key) + ':' + str(value) + " stored successfully"
    Dict[key] = value

    #Serialization
    pickle_out = open('datastore.pickle','wb')
    pickle.dump(Dict,pickle_out)
    pickle_out.close()

    return jsonify({'success': 1 , 'result': value,
                    'message': msg })

#GET
@app.route('/get/<string:key>',methods=['GET'])
def get_value(key):
    global Dict

    #Deserialize
    try:
        pickle_in = open('datastore.pickle','rb')
        Dict = pickle.load(pickle_in)
    except:
        Dict = {}
    if key in Dict:
        value = Dict[key]
        return jsonify({'success': 1 , 'result': value,
                    'message': 'Keys exists in DataStore' })
    else:
        return jsonify({'success': 0 , 'result': '',
                    'message': 'Keys does not exist in DataStore' })

#RESET
@app.route('/reset/<string:password>',methods=['GET'])
def reset_value(password):
    global Dict
    if password!='iron':
        return jsonify({'success': 0 , 'result': '',
                    'message': 'Incorrect Password' })
    Dict = {}

    #Serialization
    pickle_out = open('datastore.pickle','wb')
    pickle.dump(Dict,pickle_out)
    pickle_out.close()


    return jsonify({'success': 1 , 'result': '',
                    'message': 'DataStore deleted' })


if __name__ == '__main__':
    app.run(debug=True, threaded=False)
