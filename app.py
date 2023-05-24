from flask import Flask, render_template, request
import pickle
app=Flask(__name__)
with open('assets/svm_pred.pkl', 'rb') as f:
    model_svm=pickle.load(f)


# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/graphs")
def data():
    return render_template("graphs.html")

@app.route('/Predictor', methods=['GET', 'POST'])
def Predictor():

    if request.method=='POST':
        ph=float(request.form.get('ph'))
        Hardness=float(request.form.get('Hardness'))
        Solids=float(request.form.get('Solids'))
        Chloramines=float(request.form.get('Chloramines'))
        Sulfate=float(request.form.get('Sulfate'))
        Conductivity=float(request.form.get('Conductivity'))
        Organic_carbon=float(request.form.get('Organic_carbon'))
        Trihalomethanes=float(request.form.get('Trihalomethanes'))
        Turbidity=float(request.form.get('Turbidity'))
        user_input=(ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity)
        print(user_input)
        model_output=model_svm.predict([user_input])
        return render_template('Predictor.html', output=f'Class {model_output[0]}')
        
    else:
        return render_template('Predictor.html')
if __name__=='__main__':
    app.run()