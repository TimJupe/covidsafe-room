from flask import Flask, render_template, request
import json

app = Flask(__name__)

# some JSON:
acacia_data = '{ "AC1":24, "AC1Max":25}'

# parse acacia_data from JSON to Python dictionary:
acacia_dict = json.loads(acacia_data)


@app.route('/', methods=['GET', 'POST'])
def index():

    return render_template('index.html', acacia_dict=acacia_dict)
