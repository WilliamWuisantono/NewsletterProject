from flask import Flask, request, render_template
import pyodbc

app = Flask(__name__)

# Database connection config
server = 'dbudevops2024.database.windows.net'
database = 'NewsletterDB'
username = 'WilliamDBU'
password = 'DBUdevops2024'
driver = '{ODBC Driver 17 for SQL Server}'

connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit-form', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    frequency = request.form['frequency']

    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Subscribers (Name, Email, Frequency) VALUES (?, ?, ?)",
            (name, email, frequency)
        )
        conn.commit()
        conn.close()
        return 'Subscription successful!'
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
