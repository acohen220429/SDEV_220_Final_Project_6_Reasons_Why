from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# assign app w/ instance of Flask
app = Flask(__name__)

# query database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db = SQLAlchemy(app)

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    drName = db.Column(db.String(20), unique=False)
    clinic = db.Column(db.String(40), unique=False)
    description = db.Column(db.String(100))

    def __str__(self):
        details = (
            f"Appointment with: {self.drName} on {self.date.strftime('%m %d, %Y')} at {self.time.strftime('%I:%M %p')}\n"
            f"Location: {self.clinic}"
        )

        # only return description if there is one
        if self.description:
            details += f"\nDescription: {self.description}"

        return details

# format for appointment creation in local db:
# appt1 = Appointment(date=date(2025, 12, 5), time=time(11,0), drName="Dr. Jekyl", clinic="Mental Clarity", description="Intake")

# to see appointments from your local database run from terminal:
# for appt in Appointment.query.all():
#    print(appt)

# homepage
@app.route("/")
def index():
    return "HeadsUp Together by 6 Reasons Why"