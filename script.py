#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request, jsonify
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
import joblib


# In[2]:


app = Flask(__name__)


# In[3]:


supply_lost_model = joblib.load('supply_lost_model.pkl') #Kavindi
post_production_lost_model = joblib.load('post_production_cost.pkl') # Thamodi


# In[4]:


# Kavindi
@app.route('/predict_supply_lost', methods=['POST'])
def predict_supply():
    try:
        # Get JSON data from the request
        input_data = request.get_json()
        cost = input_data.get('cost')

        # Convert JSON data to DataFrame
        input_df = pd.DataFrame([input_data])


        # Make prediction
        predicted_loss = supply_lost_model.predict(input_df)
        
        #lost_perecentage = (predicted_loss[0] / cost) * 100

        # Prepare the response
        response = {'predicted_loss': predicted_loss[0] } #'lost':lost_perecentage}
        

        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)})


# In[5]:


# Thamodi
@app.route('/predict_production_lost', methods=['POST'])
def predict():
    try:
        # Get JSON data from the request
        input_data = request.get_json()

        # Convert JSON data to DataFrame
        input_df = pd.DataFrame([input_data])

        # Preprocess input data
#         preprocessed_data = preprocessor.transform(input_df)

        # Make prediction
        predicted_loss = post_production_lost_model.predict(input_df)

        # Prepare the response
        response = {'predicted_loss': predicted_loss[0]}

        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)})


# In[ ]:


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
