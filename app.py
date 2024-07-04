from flask import Flask, render_template, request, redirect, url_for
import joblib
from datetime import datetime
import re

app = Flask(__name__)

# Load the pre-trained energy consumption prediction model
model = joblib.load('model/energy_consumption_model.pkl')

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Define the route to handle prediction requests
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the current date
        current_date = datetime.now().date()
        
        # Get the input data from the form
        date_str = request.form['date']
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        rain = float(request.form['rain'])
        temp = float(request.form['temp'])
        inflation = float(request.form['inflation'])
        holiday = str(request.form['holiday'])
        
        # Convert holiday input to a binary variable
        if holiday == 'yes':
            is_holiday = 1  
        else:
            is_holiday = 0

        day_of_week = date.weekday()
        month = date.month
        year = date.year
        
        # Function to determine the season based on the month
        def get_season(month):
            if month in [10, 11, 12, 1, 2]:
                return 0  # Winter
            elif month in [3, 4, 5, 6]:
                return 1  # Summer
            else:
                return 2  # Rainy
        
        season = get_season(month)
        
        # Make the energy consumption prediction using the model
        predicted_consumption = model.predict([[temp, rain, inflation, day_of_week, month, year, season, is_holiday]])
        consumption = round(predicted_consumption[0], 2)
        
        # Generate an appropriate message based on whether the date is past, future, or today
        if date < current_date:
            message = f"Approximately {consumption} Million Units(MU) of energy were consumed on {date.strftime('%Y-%m-%d')}. Consider this as a reminder of the importance of energy conservation."
        elif date > current_date:
            message = f"Based on current projections, approximately {consumption} Million Units(MU) of energy will be required on {date.strftime('%Y-%m-%d')}. Let's plan ahead and make conscious efforts to conserve energy."
        else:
            message = f"Today, approximately {consumption} Million Units(MU) of energy are projected to be required. This serves as a call to action for us all to utilize energy wisely and adopt energy-saving practices."
        
        # Redirect to the prediction result page with the message
        return redirect(url_for('prediction_result', prediction=message))

# Define the route to display the prediction result
@app.route('/prediction_result/<prediction>')
def prediction_result(prediction):
    # Use regex to find the numerical part of the prediction
    match = re.search(r'\d+(\.\d+)?', prediction)
    if match:
        consumption_value = match.group()
        # Highlight the consumption value in the prediction message
        highlighted_prediction = prediction.replace(consumption_value, f'<span class="consumption">{consumption_value}</span>')
        return render_template('prediction_result.html', prediction=highlighted_prediction)
    else:
        return render_template('prediction_result.html', prediction=prediction)

# Run the Flask app in debug mode
if __name__ == '__main__':
    app.run(debug=True)
