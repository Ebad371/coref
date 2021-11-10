#import neuralcoref.neuralcoref
from flask import Flask, jsonify, request
import json
from io import StringIO
import io
import sys
import pickle
import spacy



app = Flask(__name__)
filename = 'finalized_model.sav'

loaded_model = pickle.load(open(filename, 'rb'))


@app.route('/predictCoref',methods=["POST"])
def prediction():
    text = request.json["data"]





    doc = loaded_model(text)  
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout

   
    print(doc._.coref_clusters)

    output = new_stdout.getvalue()

    sys.stdout = old_stdout
    

    print(output)
    
    return {"data":output}


if __name__ == "__main__":
    app.run(debug=False)