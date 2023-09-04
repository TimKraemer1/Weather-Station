from flask import Flask, render_template, jsonify
import time
import os

app = Flask(__name__, template_folder='Templates')

last_line = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_updated_value')
def get_updated_value():
    # Return the updated value to the client
    # You can use Flask's jsonify or any other method to send data to the client
    with open('../python_scripts/DataLoggerSystem/tempdata.csv', 'r') as csv_file:
        last_line = csv_file.readlines()[-1].rstrip('\n').split(',')
        updated_temp = last_line[1] + '°F'
        time = last_line[0]
        csv_file.close()

    return jsonify({'value': updated_temp})

if __name__ == '__main__':

    app.run(host='192.168.86.42', port=5000)  # Adjust host and port as needed

