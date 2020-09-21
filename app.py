from flask import Flask,render_template, request
import pickle
import numpy as np
app = Flask(__name__)

filename = 'marks_model.pkl'
regressor = pickle.load(open(filename, 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    
    if request.method == 'POST':
        
        hours = float(request.form['hours'])
    
        my_prediction = regressor.predict([[hours]])[0]	    
        
        return render_template('result.html',result=my_prediction)
	
@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)