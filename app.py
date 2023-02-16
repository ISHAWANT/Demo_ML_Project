from flask import Flask,jsonify,render_template 
from housing.logger import logging 
app = Flask(__name__) 

@app.route("/",methods=['GET','POST']) 

def index():
    logging.info('We are testing logging module')
    return "Starting Mahcine learning Project"

if __name__=="__main__":
    app.run(debug=True)