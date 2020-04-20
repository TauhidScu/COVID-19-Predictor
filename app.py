import pickle
from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about_Covid')
def about_Covid():
    return render_template('about_covid19.html')

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/result', methods = ["POST", "GET"])

def result():
    if request.method == "POST":
        myDict = request.form
        Age = int(myDict['Age'])
        Fever = int(myDict['Fever'])
        DryCough = int(myDict['DryCough'])
        Fatigue = int(myDict['Fatigue'])
        BreathProb = int(myDict['BreathProb'])
        SoreThroat = int(myDict['SoreThroat'])
        TravelHis = int(myDict['TravelHis'])
        symptoms = [Age, Fever, DryCough, Fatigue, BreathProb, SoreThroat, TravelHis]
        model = open('predictorModel.pkl', 'rb')
        model = pickle.load(model)
        Probability = model.predict_proba([symptoms])[0][1]
        return render_template('result.html', Probability = round(Probability*100))

if __name__ == "__main__":
    app.run(debug=True)