from flask import Flask, render_template, jsonify, request, send_file
from datetime import datetime, timedelta
import hashlib
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('agg')

#creates random sequence for secure data transmission
url = hashlib.md5("Walnut&Chestnut".encode('utf-8')).hexdigest()
#url = 'temp_data'

num_lines = 0

app = Flask(__name__, template_folder="Templates")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/' + url)
def parse_data():
    temperature_data = request.args.get('temp_data')
    temperature_time = datetime.now()
    temperature_time += timedelta(hours=5)
    temperature_time = temperature_time.strftime('%l:%M %p')
    try:
        with open('Weather-Station/Server-side/Backend/tempdata.csv', 'a') as f:
            f.write('{},{}\n'.format(temperature_time, temperature_data))
            f.close()
    except:
        return 'Failure'
    else:
        return 'Success'

@app.route('/get_updated_value')
def get_updated_value():
    df = pd.read_csv('Weather-Station/Server-side/Backend/tempdata.csv')
    updated_temp = (df['temp'].tail(1)).to_string(index=False)
    return jsonify({'value': updated_temp})



    return jsonify({'value': updated_temp})

@app.route('/temp_graph')
def get_temp_graph():
    df = pd.read_csv('Weather-Station/Server-side/Backend/tempdata.csv')
    plt.plot(df['time'].tail(8640), df['temp'].tail(8640), color='blue')
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.xticks(df['time'].tail(8640), rotation=90)
    plt.tight_layout()
    plt.locator_params(axis='x', nbins=5)
    plt.ylim([40, 100])
    plt.savefig('Weather-Station/Server-side/Backend/static/temp_fig.png')
    return send_file('static/temp_fig.png', mimetype='image/png')









