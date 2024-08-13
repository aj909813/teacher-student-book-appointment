from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__)
appointments_file = 'data/appointments.json'

# Ensure the data directory and file exist
if not os.path.exists('data'):
    os.makedirs('data')

if not os.path.exists(appointments_file):
    with open(appointments_file, 'w') as f:
        json.dump([], f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/book', methods=['POST'])
def book_appointment():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    role = data.get('role')
    date = data.get('date')
    time = data.get('time')

    appointment = {
        'name': name,
        'email': email,
        'role': role,
        'date': date,
        'time': time
    }

    # Save appointment to the JSON file
    with open(appointments_file, 'r') as f:
        appointments = json.load(f)
    
    appointments.append(appointment)

    with open(appointments_file, 'w') as f:
        json.dump(appointments, f, indent=4)

    return jsonify({"message": "Appointment successfully booked!"})

if __name__ == '__main__':
    app.run(debug=True)

