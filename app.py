from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>HealthConnect Telemedicine Platform</h1>

    <h3>Services</h3>

    <ul>
        <li>Patient Registration</li>
        <li>Doctor Dashboard</li>
        <li>Appointment Scheduling</li>
    </ul>
    """

@app.route('/doctor')
def doctor():
    return """
    <h2>Doctor Dashboard</h2>

    <ul>
        <li>Patient Records</li>
        <li>Appointments</li>
        <li>Consultations</li>
    </ul>
    """

@app.route('/appointment')
def appointment():
    return """
    <h2>Appointment Scheduling</h2>

    <form>
        Patient Name:<br>
        <input type='text'><br><br>

        Appointment Date:<br>
        <input type='date'><br><br>

        <button>Book Appointment</button>
    </form>
    """

if __name__ == '__main__':
    app.run()
