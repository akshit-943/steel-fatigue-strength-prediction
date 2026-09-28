# steel-fatigue-strength-prediction
Machine learning project for predicting steel rotating-bending fatigue strength using metallurgical and heat-treatment parameters.


# Steel Rotating-Bending Fatigue Strength Prediction

## About the Project

This is a machine learning project where I tried to predict the rotating-bending fatigue strength of steel at 10⁷ cycles.

The dataset contains different chemical composition and heat-treatment parameters of steel. I used these parameters to train regression models and compare their performance.

## What I did

- Cleaned and explored the dataset
- Split the data into training and testing sets
- Built a Linear Regression model as a baseline
- Built a Random Forest Regressor
- Compared the performance of both models
- Used feature importance to identify the important parameters
- Reduced the Random Forest model to the top 10 features
- Saved the trained model using Joblib
- Built a simple Streamlit application for prediction

## Results

### Linear Regression
- R²: 0.9750
- MAE: 24.87 MPa
- RMSE: 32.16 MPa

### Random Forest
- R²: 0.9855
- MAE: 18.99 MPa
- RMSE: 24.45 MPa

### Random Forest using Top 10 Features
- R²: 0.9824
- MAE: 20.83 MPa
- RMSE: 26.99 MPa

Random Forest performed better than Linear Regression on the test set.

## Streamlit App

I also created a simple Streamlit application where users can enter selected steel composition and heat-treatment parameters and get a predicted fatigue strength.

## Tools Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook

## Project Files

- `SteelFatigue.ipynb` - Data analysis, preprocessing and model training
- `app.py` - Streamlit application
- `fatigue_model_10.pkl` - Trained Random Forest model

## Note

The prediction is based on the dataset used for training and should not be considered as a universal material design limit.
