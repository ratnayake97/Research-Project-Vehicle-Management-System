from flask import Flask, jsonify

import pandas as pd
import os
from os import getcwd
import pickle
from flask import Flask, render_template, request
import json

app = Flask(__name__)
directory = getcwd()

# Import the required Pickle files
top_insurance_model = pickle.load(open(os.path.join(directory, 'models/top_insurance.pkl'), 'rb'))
top_average_rating_model = pickle.load(open(os.path.join(directory, 'models/top_average_rating_insurance.pkl'), 'rb'))


def topSellingInsurance(df):
    # json object
    insuranceObj = [
        {
            "rank": 1,
            "Insurance": df['Motor_Insurance'][0],
            "numOfInsurance": str(df['Vehicle_Count'][0])
        },
        {
            "rank": 2,
            "Insurance": df['Motor_Insurance'][1],
            "numOfInsurance": str(df['Vehicle_Count'][1])
        },
        {
            "rank": 3,
            "Insurance": df['Motor_Insurance'][2],
            "numOfInsurance": str(df['Vehicle_Count'][2])
        },
        {
            "rank": 4,
            "Insurance": df['Motor_Insurance'][3],
            "numOfInsurance": str(df['Vehicle_Count'][3])
        },
        {
            "rank": 5,
            "Insurance": df['Motor_Insurance'][4],
            "numOfInsurance": str(df['Vehicle_Count'][4])
        },
        {
            "rank": 6,
            "Insurance": df['Motor_Insurance'][5],
            "numOfInsurance": str(df['Vehicle_Count'][5])
        },
        {
            "rank": 7,
            "Insurance": df['Motor_Insurance'][6],
            "numOfInsurance": str(df['Vehicle_Count'][6])
        },
        {
            "rank": 8,
            "Insurance": df['Motor_Insurance'][7],
            "numOfInsurance": str(df['Vehicle_Count'][7])
        },
        {
            "rank": 9,
            "Insurance": df['Motor_Insurance'][8],
            "numOfInsurance": str(df['Vehicle_Count'][8])
        },
        {
            "rank": 10,
            "Insurance": df['Motor_Insurance'][9],
            "numOfInsurance": str(df['Vehicle_Count'][9])
        }
    ]

    return insuranceObj


def getTopAverageRatingInsurance(df):

    insuranceObj = [
        {
            "rank": 1,
            "Insurance": df['Motor_Insurance'][0],
            "Weight": str(df['weight'][0])
        },
        {
            "rank": 2,
            "Insurance": df['Motor_Insurance'][1],
            "Weight": str(df['weight'][1])
        },
        {
            "rank": 3,
            "Insurance": df['Motor_Insurance'][2],
            "Weight": str(df['weight'][2])
        },
        {
            "rank": 4,
            "Insurance": df['Motor_Insurance'][3],
            "Weight": str(df['weight'][3])
        },
        {
            "rank": 5,
            "Insurance": df['Motor_Insurance'][4],
            "Weight": str(df['weight'][4])
        },
        {
            "rank": 6,
            "Insurance": df['Motor_Insurance'][5],
            "Weight": str(df['weight'][5])
        },
        {
            "rank": 7,
            "Insurance": df['Motor_Insurance'][6],
            "Weight": str(df['weight'][6])
        },
        {
            "rank": 8,
            "Insurance": df['Motor_Insurance'][7],
            "Weight": str(df['weight'][7])
        },
        {
            "rank": 9,
            "Insurance": df['Motor_Insurance'][8],
            "Weight": str(df['weight'][8])
        },
        {
            "rank": 10,
            "Insurance": df['Motor_Insurance'][9],
            "Weight": str(df['weight'][9])
        },
    ]

    return insuranceObj


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


# top selling - get request - return json
@app.route('/getTopSellingInsurance')
def getTopSellingInsurance():
    tim = top_insurance_model.sort_values('Top_Sell_Insurance', ascending=True)[['Motor_Insurance', 'Vehicle_Count']] \
        .head(10).reset_index(
        drop=True)

    insurance = topSellingInsurance(tim)
    return jsonify(insurance)


@app.route('/getTopAverageRatingInsurance')
def getTopRatingInsurance():
    tari = top_average_rating_model.sort_values('average_rate_insurance', ascending=True)[
        ['Motor_Insurance', 'weight']].head(10).reset_index(drop=True)

    insurance = getTopAverageRatingInsurance(tari)
    return jsonify(insurance)


if __name__ == '__main__':
    app.run()
