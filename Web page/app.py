from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__, template_folder='template', static_url_path='/static')

model=pickle.load(open('Web page\model.pkl','rb'))


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[int(x) for x in request.form.values() if x!=" "]
    final=[np.array(int_features)]
    print(int_features)
    print(final)

    # Predict the probability of needing treatment
    prediction = model.predict_proba(final)
    
    # Convert the probability to a percentage
    percentage = prediction[0][1] * 100
    
    if percentage > 50:
        return render_template('index.html', pred='You need treatment.\nPercentage of mental illness is {:.2f}%'.format(percentage))
    else:
        return render_template('index.html', pred='You do not need treatment.\nPercentage of mental illness is {:.2f}%'.format(percentage))

    # # code for calculate probability
    # output='{0:.{1}f}'.format(prediction[0][1], 2)

    # if output>str(0.5):
    #     return render_template('index.html',pred='You need a treatment.\nProbability of mental illness is {}'.format(output))
    # else:
    #     return render_template('index.html',pred='You do not need treatment.\n Probability of mental illness is {}'.format(output))

if __name__ == '__main__':
    app.run(debug=True)
