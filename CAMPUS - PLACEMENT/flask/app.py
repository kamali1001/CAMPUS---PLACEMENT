from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)

model = pickle.load(open('place_predict.pkl', 'rb'))
print(model)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():
    data = [int(x) for x in request.form.values()]
    # print(list(request.form.values()))
    val = model.predict([data])
    res = val[0]*100
    print(res)
    val_str = ''
    if res < 50:
        res = str(res)
        val_str = "You need to prepare well!!"
    
    elif res >49:
        res = str(res)
        val_str = "All the very best, you are doing well!! Your placement chances are" + res + "%"
    
    else:
        val_str = "Something went wrong! Try again later."

    return render_template('index.html', prediction_text = '{}'.format(val_str))

if __name__ == '__main__':
    app.run()