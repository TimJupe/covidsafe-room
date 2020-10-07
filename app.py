# Import Flask Render Template
from flask import Flask, render_template, request
import pandas as pd
import json


app = Flask(__name__)

# Reading Each JSON File With Data for Each Building
acacia_rooms = '{' \
               '"AC1":26,' \
               '"AC1MAX":25,' \
               '"AC2":26,' \
               '"AC2MAX":25,' \
               '"AC3":23,' \
               '"AC3MAX":26,' \
               '"AC4":12,' \
               '"AC4MAX":26,' \
               '"AC5":17,' \
               '"AC5MAX":25' \
               '}'
# with open('data/acacia_data.json') as ar:
acacia_dict = json.loads(acacia_rooms)
print(acacia_dict)
# acacia_rooms.to_json (r'C:\Users\zelli\PycharmProjects\COVIDSafeRoom\data\acacia_data.json')
# admin_rooms = pd.read_csv(r"C:\Users\zelli\PycharmProjects\COVIDSafeRoom\data\admin_data.csv")
# banksia_rooms = pd.read_csv(r"C:\Users\zelli\PycharmProjects\COVIDSafeRoom\data\banksia_data.csv")
# bluegum_rooms = pd.read_csv(r"C:\Users\zelli\PycharmProjects\COVIDSafeRoom\data\bluegum_data.csv")
# boronia_rooms = pd.read_csv(r"C:\Users\zelli\PycharmProjects\COVIDSafeRoom\data\boronia_data.csv")
# caledonia_rooms = pd.read_csv(r"C:\Users\zelli\PycharmProjects\COVIDSafeRoom\data\caledonia_data.csv")
# chapel_rooms = pd.read_csv(r"C:\Users\zelli\PycharmProjects\COVIDSafeRoom\data\chapel_data.csv")
# danthonia_rooms = pd.read_csv(r"C:\Users\zelli\PycharmProjects\COVIDSafeRoom\data\danthonia_data.csv")
# gravelia_rooms = pd.read_csv(r"C:\Users\zelli\PycharmProjects\COVIDSafeRoom\data\gravelia_data.csv")
# lomandra_rooms = pd.read_csv(r"C:\Users\zelli\PycharmProjects\COVIDSafeRoom\data\lomandra_data.csv")
# mallee_rooms = pd.read_csv(r"C:\Users\zelli\PycharmProjects\COVIDSafeRoom\data\mallee_data.csv")
# redgum_rooms = pd.read_csv(r"C:\Users\zelli\PycharmProjects\COVIDSafeRoom\data\redgum_data.csv")
# sandlewood_rooms = pd.read_csv(r"C:\Users\zelli\PycharmProjects\COVIDSafeRoom\data\sandlewood_data.csv")
# wattle_rooms = pd.read_csv(r"C:\Users\zelli\PycharmProjects\COVIDSafeRoom\data\wattle_data.csv")
# print(acacia_rooms['acacia'][0]['AC1'])

# Transferring JSON Data to Individual Dictionaries
# acacia_dict = json.loads(acacia_rooms)
# admin_dict = json.loads(admin_rooms)
# banksia_dict = json.loads(banksia_rooms)
# bluegum_dict = json.loads(bluegum_rooms)
# boronia_dict = json.loads(boronia_rooms)
# caledonia_dict = json.loads(caledonia_rooms)
# chapel_dict = json.loads(chapel_rooms)
# danthonia_dict = json.loads(danthonia_rooms)
# gravelia_dict = json.loads(gravelia_rooms)
# lomandra_dict = json.loads(lomandra_rooms)
# mallee_dict = json.loads(mallee_rooms)
# redgum_dict = json.loads(redgum_rooms)
# sandlewood_dict = json.loads(sandlewood_rooms)
# wattle_dict = json.loads(wattle_rooms)


# Application Routes for Each Page/Building
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/acacia', methods=['GET', 'POST'])
def acacia():
    return render_template('acacia.html', acacia_dict=acacia_dict)


@app.route('/admin')
def admin():
    return render_template('admin.html')


@app.route('/banksia')
def banksia():
    return render_template('banksia.html')


@app.route('/bluegum')
def bluegum():
    return render_template('bluegum.html')


@app.route('/boronia')
def boronia():
    return render_template('boronia.html')


@app.route('/caledonia')
def caledonia():
    return render_template('caledonia.html')


@app.route('/chapel')
def chapel():
    return render_template('chapel.html')


@app.route('/danthonia')
def danthonia():
    return render_template('danthonia.html')


@app.route('/gravelia')
def gravelia():
    return render_template('gravelia.html')


@app.route('/lomandra')
def lomandra():
    return render_template('lomandra.html')


@app.route('/malleelow')
def malleelow():
    return render_template('malleelow.html')


@app.route('/malleeup')
def malleeup():
    return render_template('malleeup.html')


@app.route('/redgum')
def redgum():
    return render_template('redgum.html')


@app.route('/sandlewood')
def sandlewood():
    return render_template('sandlewood.html')


@app.route('/wattle')
def wattle():
    return render_template('wattle.html')
