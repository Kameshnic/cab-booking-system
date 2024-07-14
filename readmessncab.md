# Cab Booking System - README

## Overview
The Cab Booking System is a Python application built using the Kivy framework for the graphical user interface (GUI) and MySQL for the database. This system allows users to book cabs, manage bookings, and view booking history. The main components of the system include `new.py` for the application logic, `new.kv` for the UI design, `database.py` for database connections, and `zuber_queries.py` for database queries.

## Project Structure
- **new.py**: Contains the main application logic and integrates the UI and database operations.
- **new.kv**: Defines the user interface using the Kivy language.
- **database.py**: Manages the connection to the MySQL database.
- **zuber_queries.py**: Contains SQL queries to interact with the database.
- **templates/**: Contains HTML templates for the web frontend.
- **app.py**: Flask application file for hosting data.

## Files and Their Roles

### new.py
This is the core file of the Cab Booking System. It includes the application logic and integrates with the UI (`new.kv`) and the database (`zuber_queries.py`). Key functions include:
- **Initialization**: Sets up the Kivy application.
- **Database Integration**: Uses functions from `zuber_queries.py` to fetch and send data to the database.
- **UI Interaction**: Handles user interactions with the UI, such as booking a cab or viewing booking history.

### new.kv
This file defines the graphical user interface of the application. It uses Kivy language to layout buttons, labels, text inputs, and other UI elements. Key components include:
- **Booking Form**: Allows users to input details for booking a cab.
- **Booking History**: Displays the user's past bookings.
- **Buttons and Navigation**: Facilitates navigation between different sections of the application.

### database.py
This file manages the connection to the MySQL database. It includes functions to connect and disconnect from the database, ensuring secure and efficient data operations. Key functions include:
- **Connect**: Establishes a connection to the MySQL database.
- **Disconnect**: Closes the connection to the database.

### zuber_queries.py
This file contains SQL queries to interact with the MySQL database. It imports functions from `database.py` to execute these queries. Key functions include:
- **Fetch Data**: Retrieves data from the database.
- **Insert Data**: Inserts new data into the database.
- **Update Data**: Updates existing data in the database.
- **Delete Data**: Deletes data from the database.

### templates/
This directory contains HTML templates for the web frontend. It includes files like `index.html` and other HTML files required for rendering web pages.

### app.py
This file contains the Flask application for hosting data. It includes routes and views to render HTML templates and interact with the backend.

## How It Works
1. **User Interaction**: The user interacts with the application via the UI defined in `new.kv` or through the web frontend in `templates/`.
2. **Data Handling**: User actions trigger functions in `new.py`, which handle the logic and interact with the database.
3. **Database Queries**: `new.py` calls functions from `zuber_queries.py` to execute SQL queries on the MySQL database.
4. **Database Connection**: `zuber_queries.py` uses `database.py` to connect to the database and perform the required operations.
5. **Display Results**: The results of the database queries are sent back to `new.py`, which then updates the UI to reflect the changes.

## Libraries Used
- **Kivy**: For building the graphical user interface.
- **KivyMD**: For material design components in Kivy.
- **Flask**: For hosting data and building the web frontend.
- **MySQL Connector/Python**: For connecting to the MySQL database.
- **Geocoder**: For geocoding addresses.
- **Google Maps API**: For integrating maps and location services.
- **Geocode API**: For geocoding services.
- **pywhatkit**: For sending messages and other automation tasks.

## Installation

1. **Install Python**: Ensure Python is installed on your system.

2. **Install Dependencies**:
   ```sh
   pip install kivy kivymd flask mysql-connector-python geocoder googlemaps pywhatkit
   ```

3. **Set Up Database**:
   Create a MySQL database named `zuber` and populate it with the necessary tables and data. You can use the SQL scripts provided in the project to set up the database.

4. **Run the Application**:
   - **For Kivy Application**:
     ```sh
     python new.py
     ```
   - **For Flask Application**:
     ```sh
     python app.py
     ```

## Getting Started
To run the Cab Booking System, follow these steps:

1. **Install Dependencies**:
   Ensure you have Python and MySQL installed. Install the required Python packages using:
   ```sh
   pip install kivy kivymd flask mysql-connector-python geocoder googlemaps pywhatkit
   ```

2. **Set Up Database**:
   Create a MySQL database named `zuber` and populate it with the necessary tables and data. You can use the SQL scripts provided in the project to set up the database.

3. **Run the Application**:
   Execute `new.py` to start the Kivy application:
   ```sh
   python new.py
   ```
   Execute `app.py` to start the Flask web application:
   ```sh
   python app.py
   ```

## Contact
For any questions or support, please contact the project maintainer at[kameshnic2885@gmail.com].

---

This README provides a comprehensive overview of the Cab Booking System, including the roles of each file, how the system works, and steps to get started. Ensure to replace placeholder email with an actual contact email.