from flask import Flask,jsonify,render_template 
from housing.logger import logging 
from housing.exception import HousingExeption
import os,sys 

app = Flask(__name__) 

@app.route("/",methods=['GET','POST']) 

def index():
    # logging.info('We are testing logging module')
    try:
        raise Exception('We are testing custom exception')
    except Exception as e:
        housing=HousingExeption(e,sys)
        logging.info(housing.error_message)
        logging.info('We are testing logging module')
    return "Starting Mahcine learning Project"

if __name__=="__main__":
    app.run(debug=True)