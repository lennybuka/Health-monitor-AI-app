
from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Read data from JSON file
    try:
        with open('health_data.json', 'r') as f:
            data = json.load(f)
        
        heart_rate = data.get('heart_rate', 0)
        blood_oxygen = data.get('blood_oxygen', 0)
        status = data.get('status', 'Unknown')
        
    except FileNotFoundError:
        # Fallback if JSON file doesn't exist
        heart_rate = 0
        blood_oxygen = 0
        status = 'No Data'
    except json.JSONDecodeError:
        # Fallback if JSON is invalid
        heart_rate = 0
        blood_oxygen = 0
        status = 'Invalid Data'

    return render_template('dashboard.html',
                           hr=heart_rate,
                           oxy=blood_oxygen,
                           status=status)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
