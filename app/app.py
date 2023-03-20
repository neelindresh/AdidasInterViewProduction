from flask_api import FlaskAPI
from config import config
from script import model_loader,preprocess
import flask
import json
import argparse
app=FlaskAPI(__name__)

model_load=model_loader.Model(config.MODEL_NAME,config.VERSION_NUMBER)
@app.route("/",methods=["GET","POST"])
def index():
    
    if flask.request.method=="POST":
        data=flask.request.data
        
        
        data=preprocess.preprocess_data(data)
        predictions=model_load.predict(data)
        return {
            "predictions": list([str(i) for i in predictions])
        }

    return {}

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='A test program.')

    parser.add_argument("--host", help="get host system from user", default="0.0.0.0")
    parser.add_argument("-p", "--port", help="get port form user", default=5005)

    args = parser.parse_args()

    app.run(host=args.host,port=args.port)