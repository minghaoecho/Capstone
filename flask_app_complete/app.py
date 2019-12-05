from flask import Flask, render_template, request, g, session
import pandas as pd
import numpy as np
import plotly
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import json
import requests
import pickle
import folium


def recommender(to_predict):


    df = pickle.load(open("recommender_user.p", "rb"))
    asin_name = pickle.load(open("asin_name.p", "rb"))
    asin_dict = dict(zip(asin_name['asin'], asin_name['product_name']))
    count = asin_name[asin_name['product_name'].str.contains(to_predict)].iloc[0,1]
    item_number = list(df[asin_name[asin_name['product_name'].str.contains(to_predict)].iloc[0,0]].sort_values()[1:6].index)

    results =[asin_dict[item] for item in item_number]

    print (results)
    print(count)

    return results,count



# create flask app
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
# secret key to perform certain actions
app.secret_key = 'sdfgsdgfdgfgfdgd'



# create index
@app.route('/')
def index():

     return render_template("index.html",len = 0)



# team information page
@app.route('/team/')
def team():

    return render_template("team.html")




# process when zipcode submitted
@app.route('/process')
def process():
    print (request.args['rawtext'])
    results,count = recommender(request.args['rawtext'])

    print(count)

    print(results)
    return render_template("index.html",len = len(results),results =results,count=str(count))# results=np.round(results,4)





if __name__ == "__main__":
    app.run(debug=True)
