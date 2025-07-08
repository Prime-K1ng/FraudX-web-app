from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        inputs = [float(request.form[f'input{i}']) for i in range(1, 31)]
        data = np.array([inputs])
        prediction = model.predict(data)[0]

        result = "⚠️ Fraudulent Transaction" if prediction == 1 else "✅ Legitimate Transaction"
        return render_template('result.html', prediction=result)

    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
