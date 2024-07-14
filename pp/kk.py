from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)

# MySQL Configuration
host = 'localhost'
user = 'kamesh'
password = '5970'
database = 'zuber'

# Route for home page with login form
@app.route('/', methods=['GET', 'POST'])
def home(): 
    if request.method == 'POST':
        user_id = request.form['user_id']
        password = request.form['password']
        # Check if user_id and password match some credentials
        if user_id == 'kamesh' and password == '1357' or user_id == 'akisher' and password == '1357' or user_id == 'dinesh' and password == '1357':
            # Redirect to the page with database buttons
            return redirect(url_for('database_buttons'))
    # Render the login form if not authenticated or upon initial visit
    return render_template('login.html')

# Route to display buttons for accessing database tables
@app.route('/database')
def database_buttons():
    return render_template('database_buttons.html')

# Route to display Car table
@app.route('/car')
def display_car():
    # Connect to MySQL database and fetch data
    connection = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = connection.cursor()
    query = "SELECT * FROM car"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('car.html', rows=rows)

# Route to display Transaction table
@app.route('/transaction')
def display_transaction():
    connection = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = connection.cursor()
    query = "SELECT * FROM transaction"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('transaction.html', rows=rows)

# Route to display Customer table
@app.route('/customer')
def display_customer():
    connection = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = connection.cursor()
    query = "SELECT * FROM customer"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('customer.html', rows=rows)

# Route to display Driver table
@app.route('/driver')
def display_driver():
    connection = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = connection.cursor()
    query = "SELECT * FROM driver"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('driver.html', rows=rows)

# Route to display Booking table
@app.route('/booking')
def display_booking():
    connection = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = connection.cursor()
    query = "SELECT * FROM booking"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('booking.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)


