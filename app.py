from flask import Flask,jsonify,render_template 

app = Flask(__name__) 

@app.route("/",methods=['GET','POST']) 

def index():
    return "Starting Mahcine learning Project"

if __name__=="__main__":
    app.run(debug=True)