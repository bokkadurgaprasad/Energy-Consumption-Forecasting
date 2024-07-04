# Energy Consumption Forecasting Project

This project aims to forecast energy consumption i.e., Electricity Consumption in Andhra Pradesh using machine learning techniques. The predictive model is trained on historical energy consumption data along with weather and economic indicators to provide accurate forecasts for past, present, and future energy usage.

## Overview

The Energy Consumption Forecasting project leverages machine learning to predict energy consumption in Andhra Pradesh. Using historical data, the project aims to provide accurate forecasts for past, present, and future energy usage. This predictive analysis is crucial for efficient energy management, planning, and policy-making. By understanding consumption patterns, stakeholders can make informed decisions to optimize energy distribution and reduce wastage.

## Features

- Machine learning model for energy consumption forecasting
- Web application for real-time energy consumption predictions
- Integration of weather and economic indicators for enhanced accuracy

## Project Structure

```
Energy_Consumption_Forecasting/
│
├── data/
|   └──AP/
|      ├── 2015-2023_data.csv
│      ├── ashish.csv
|      └── finalAPData.csv
│
│   
├── notebooks/
│   └── Energy_Consumption_Forecasting.ipynb
│
├── models/
│   └── energy_consumption_model.pkl
│
├── src/
│   ├── main.py
│   ├── static/
│   |   ├── styles.css
│   |   └── Images/
|   |          ├── bg.jpg
│   |          └── favicon.ico
|   |
│   └── templates/
│       ├── index.html
│       └── prediction_result.html
│
├── screenshots/
│   ├── input-page.png
|   ├── output-future.png
|   ├── output-past.png
|   └── output-present.png
| 
├── Documentation.pdf
|
├── README.md
│
└── requirements.txt
```

## Usage

1. Install dependencies: `pip install -r requirements.txt`
2. Run the Flask web application: `python src/main.py`
3. Access the web application in your browser at `http://localhost:5000`

## Documentation

Refer to the documentation for detailed information about the project, including data preprocessing, model training, web application development, and usage instructions.

