from flask import Flask, render_template, jsonify, request
from datetime import datetime, timedelta
import hashlib
import pandas as pd
import matplotlib.pyplot as plt

#creates random sequence for secure data transmission
#url = hashlib.md5("Walnut&Chestnut".encode('utf-8')).hexdigest()
url = 'temp_data'

num_lines = 0

app = Flask(__name__, template_folder="Templates")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/' + url)
def parse_data():
    temperature_data = request.args.get('temp_data')
    temperature_time = datetime.now()
    temperature_time += timedelta(hours=5)
    temperature_time = temperature_time.strftime('%H:%M:%S')
    try:
        with open('flask_test/tempdata.csv', 'a') as f:
            f.write('{},{}\n'.format(temperature_time, temperature_data))
            f.close()
    except:
        return 'Failure'
    else:
        return 'Success'

@app.route('/get_updated_value')
def get_updated_value():
    # Return the updated value to the client
    with open('flask_test/output.txt', 'r') as txt_file:
        last_line = txt_file.readlines()[-1]
        updated_temp = last_line + '°F'
        txt_file.close()



    return jsonify({'value': updated_temp})

@app.route('/temp_graph')
def get_temp_graph():
    df = pd.read_csv('tempdata.csv')
    plt.plot(df['time'].tail(8640), df['temp'].tail(8640))