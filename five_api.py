from flask import Flask, jsonify, request,render_template
from store_cal import process_location_data
import json

app = Flask(__name__)

status = {"status" : "Yes"}

@app.route('/status', methods=['GET'])
def get_books():

    return jsonify(status)

@app.route('/your_location', methods=['POST'])
def process_input():
    location = request.form.get('location')
    print("接收到的地址：", location)
    result = process_location_data(location)
    
    # return result
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run()
