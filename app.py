from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@Preethi33",
    database="internship_db"
)

cursor = db.cursor()

# Route to display form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    course = request.form['course']
    domain = request.form['domain']

    query = """
    INSERT INTO internship_registrations (name, email, phone, course, domain)
    VALUES (%s, %s, %s, %s, %s)
    """

    values = (name, email, phone, course, domain)

    cursor.execute(query, values)
    db.commit()

    return "Registration Successful!"

if __name__ == '__main__':
    app.run(debug=True)