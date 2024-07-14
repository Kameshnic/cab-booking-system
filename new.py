from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
import zuber_queries as query
from customer import Customer
from kivy.uix.popup import Popup
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.textfield import MDTextField
from driver import Driver
from kivy.uix.button import Button
from kivy.metrics import dp
from kivy.event import EventDispatcher
from kivy.garden.mapview import MapView


Window.size = (650, 650)


class Start(Screen):
    pass
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock
from kivy.animation import Animation

class SplashScreen(Screen):
    def __init__(self, **kwargs):
        super(SplashScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=50)
        self.image = Image(source='Mahindra_Thar_Photoshoot_At_Perupalem_Beach_West_Godavari_DistrictAPIndia__Djdavid.webp', size_hint=(1, 0.6))
        self.label = Label(text="Welcome To SSN CAB , Enjoy Your Journey !...", font_size='20sp', color=(1, 1, 1, 1))
        self.progress_bar = ProgressBar(max=1000, value=0, size_hint=(1, 0.1))

        self.layout.add_widget(self.image)
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.progress_bar)
        self.add_widget(self.layout)

        self.loading_animation = Animation(value=1000, duration=10)
        self.loading_animation.bind(on_complete=self.switch_to_main)
        self.loading_animation.start(self.progress_bar)

    def switch_to_main(self, *args):
        self.manager.current = 'continue'

class Hii(Screen):
    pass
class Continue(Screen):
    pass

class Mainpage(Screen):
    pass
################################
class Roptionpage(Screen):
    pass

class Doptionpage(Screen):
    pass
##########################3
class Rlogin(Screen):
    def validate_fields(self):
        username = self.ids.username_field.text.strip()
        password = self.ids.password_field.text.strip()
        mobile_number = self.ids.mobile_field.text.strip()
        id=1
        
        if not all([username, password, mobile_number]):
            self.clear_fields()
            self.show_popup("Please fill in all fields.")
        else:
            # Implement your login logic here
            result = query.authenticateCustomer(mobile_number, password)
            if len(result) == 0:
                self.show_popup("Incorrect password")
                self.clear_fields()
            else:
                # Sign in successful, proceed with next steps
                
                result=result[0]
                global currentCustomer
                currentCustomer = Customer(result[0], result[1], result[4], result[2])
                self.show_success_popup("logged in successfully!")
                self.clear_fields()
                self.clear_fields()
                self.manager.current='rider'
                # Add your logic here for successful sign in

    def show_popup(self, message):
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text=message))
        popup = Popup(title='Error', content=content, size_hint=(None, None), size=(300, 200))
        popup.open()

    def show_success_popup(self, message):
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text=message))
        popup = Popup(title='Success', content=content, size_hint=(None, None), size=(300, 200))
        popup.open()

    def clear_fields(self):
        self.ids.username_field.text = ''
        self.ids.password_field.text = ''
        self.ids.mobile_field.text = ''    

    
    pass
class Rsignin(Screen):
    def validate_fields(self):
        username = self.ids.username_field.text.strip()
        password = self.ids.password_field.text.strip()
        confirm_password = self.ids.confirmpassword.text.strip()
        user_type = self.ids.type_field.text.strip()
        currentbooking=None
        mobile_number = self.ids.mobile_field.text.strip()

        if not all([username, password, confirm_password, user_type, mobile_number]):
            self.show_popup("Please fill in all fields.")
        elif password != confirm_password:
            self.show_popup("Passwords do not match.")
            self.clear_fields()
        else:
            # If all fields are filled and passwords match, proceed with signup
            # query.insertCustomer(username, password, user_type, mobile_number)
            query.insertCustomer(username, password,currentbooking, mobile_number)
            self.clear_fields() 
            self.clear_fields()
            self.manager.current='riderlogin'
             # Clear fields after successful signup
            # You can add code here to move to login page or do something else

    def show_popup(self, message):
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text=message))
        popup = Popup(title='Error', content=content, size_hint=(None, None), size=(300, 200))
        popup.open()

    def clear_fields(self):
        self.ids.username_field.text = ''
        self.ids.password_field.text = ''
        self.ids.confirmpassword.text = ''
        self.ids.type_field.text = ''
        self.ids.mobile_field.text = ''

###########################
class Dlogin(Screen):
    def signInDriverPage(self):
        phoneNumber = self.ids.mobile_field.text.strip()
        password = self.ids.password_field.text.strip()
        result = query.authenticateDriver(phoneNumber, password)
        if len(result) == 0:
            self.show_popup("Either password is wrong or user is not signed up as a driver")
        else:
            result = result[0]
            global currentDriver
            currentDriver = Driver(result[0], result[1], result[4], result[2])
            self.show_popup("Signed In successfully")
            self.clear_fields()
            self.manager.current = 'driver'

    def show_popup(self, message):
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text=message))
        popup = Popup(title='Message', content=content, size_hint=(None, None), size=(300, 200))
        popup.open()
    def clear_fields(self):
        self.ids.username_field.text = ''
        self.ids.password_field.text = ''
        self.ids.type_field.text = ''
        self.ids.mobile_field.text = ''    

  

class Dsignin(Screen):
    def signUpDriverPage(self):
        name = self.ids.username_field.text
        password = self.ids.password_field.text
        confirmPassword = self.ids.confirmpassword.text
        phoneNumber = self.ids.mobile_field.text
        brand = self.ids.brand_field.text
        model = self.ids.model_field.text
        registration_number = self.ids.registration_field.text
        capacity = self.ids.capacity_field.text
        price_per_km = self.ids.price_field.text
        currentLocation=self.ids.current_field.text
       

        if not all([name, password, confirmPassword, phoneNumber, brand, model, registration_number, capacity, price_per_km,currentLocation]):
            self.show_popup("Please fill in all fields.")
        elif password != confirmPassword:
            self.clear_fields()
            self.show_popup("Passwords do not match.")
        else:
            currentBooking = None
            query.insertCar(brand, model, registration_number, capacity, price_per_km)
            car_id = query.lastInsertIds()
            query.insertDriver(name, password, currentBooking, phoneNumber, car_id, currentLocation, True)
            self.show_popup("Signed up successfully !!")
            self.clear_fields()
            self.manager.current='driverlogin'

    def show_popup(self, message):
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text=message))
        popup = Popup(title='Message', content=content, size_hint=(None, None), size=(300, 200))
        popup.open()
    def clear_fields(self):
        self.ids.username_field.text = ''
        self.ids.password_field.text = ''
        self.ids.confirmpassword.text = ''
        self.ids.type_field.text = ''
        self.ids.mobile_field.text = '' 
        self.ids.mobile_field.text=''
        self.ids.brand_field.text=''
        self.ids.model_field.text=''
        self.ids.registration_field.text=''
        self.ids.capacity_field.text=''
        self.ids.price_field.text=''
        self.ids.current_field.text=''
##############################
class Riderpage(Screen):
    def printCustomerDetails(self):
        self.manager.current='checkdetails'
        pass

    def updateCustomerPassword(self):
        self.manager.current='changepassword'
        # Your updateCustomerPassword logic goes here
        pass

    def bookATrip(self):
        self.manager.current='map'
        # Your bookATrip logic goes here
        pass

    def cancelCustomerBooking(self):
        self.manager.current='canceltrip'
        # Your cancelCustomerBooking logic goes here
        pass

    def getCustomerBookingHistory(self):
        self.manager.current='bookinghistory'
        # Your getCustomerBookingHistory logic goes here
        pass

    def getCustomerTransactionHistory(self):
        self.manager.current='transactionhistory'
        # Your getCustomerTransactionHistory logic goes here
        pass

    def makeCustomerTransaction(self):
        self.manager.current='maketransaction'
        # Your makeCustomerTransaction logic goes here
        pass

    def signOut(self):
        self.manager.current='signout'

        # Your signOut logic goes here
        pass


class Signoutscreen(Screen):
    def signOut(self):
        currentCustomer.clear()
        self.manager.current = "Mainpage"

        

class Maketransactionscreen(Screen):
    def update_transaction_details(self):
        global currentBooking
        currentBooking, car = query.getCurrentBooking(currentCustomer.id)
        distance = query.distances((currentBooking[1]),(currentBooking[2]))
        global amount 
        global amt
        if(waitingtime=="30 minutes"):
            amt=10
        elif(waitingtime=="50 minutes"):
            amt=20
        elif(waitingtime=="1 hour"):
            amt=40
        elif(waitingtime=="more than one hour"):
            amt=50
        else:
            amt=0    



        amount = distance * currentBooking[3]* car[5]
        amount=str(amount)[:-2]
        amount=float(amount)+float(amt)
        amount=str(amount)

        
             
        
        
        global transaction_info
        transaction_info = (f"Transaction for bookingID :: {currentBooking[0]}\n"
                            f"carID :: {car[0]}\n"
                            f"from '{currentBooking[1]}' to '{currentBooking[2]}'\n"
                            f"Total distance taken:: {distance}\n"
                            f"{currentBooking[3]} passengers\n"
                            f"Total amount :: {amount}\n"
                            f"waiting charge::{amt}")
        
                            
        

        self.ids.transaction_info_label.text = transaction_info
        self.ids.transaction_details_box.opacity = 1  # Make details box visible

    def confirm_payment(self):
        payment_option = self.ids.payment_option_input.text
     # Replace with actual amount # Assign booking ID to variable
        query.makeTransaction(currentBooking[0], payment_option, amount)
        confirmation_msg = f"Payment via {payment_option} confirmed."
        self.show_popup(confirmation_msg)
        self.clear_fields()  
        self.manager.current = 'bill'  # Move to "rider" page after successful payment
       # Clear input fields and transaction details

    def show_popup(self, message):
        popup = Popup(title='Payment Confirmation',
                      content=Label(text=message),
                      size_hint=(None, None), size=(400, 200))
        popup.open()

    def go_back(self):
        self.manager.current = "rider"
        self.clear_fields()  # Clear input fields and transaction details

    def clear_fields(self):
        self.ids.transaction_info_label.text = ""  # Clear transaction details
        self.ids.payment_option_input.text = "" 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView


from kivy.uix.spinner import Spinner


class SelectionScreen(Screen):
    def __init__(self, **kwargs):
        super(SelectionScreen, self).__init__(**kwargs)

        # Layout for car selection
        self.layout = BoxLayout(orientation='vertical', spacing=10)

        # Label to display selected car details
        self.selected_car_label = Label(text="Selected Car: None")
        self.layout.add_widget(self.selected_car_label)

        # Spinner for selecting car
        self.car_spinner = Spinner(text='Select Car', values=('Toyota', 'Honda', 'Ford', 'Chevrolet', 'BMW', 'Mercedes', 'Audi', 'Volkswagen', 'Hyundai', 'Nissan'))
        self.layout.add_widget(self.car_spinner)

        # Spinner for selecting color
        self.color_spinner = Spinner(text='Select Color', values=('Red', 'Blue', 'Green', 'Black', 'White', 'Silver', 'Gray', 'Yellow', 'Orange', 'Purple'))
        self.layout.add_widget(self.color_spinner)

        # Spinner for selecting vehicle type
        self.vehicle_type_spinner = Spinner(text='Select Vehicle Type', values=('Electric', 'Petrol', 'Gas'))
        self.layout.add_widget(self.vehicle_type_spinner)

        # Spinner for selecting booking type
        self.booking_type_spinner = Spinner(text='Select Booking Type', values=('Advance Booking', 'Current Booking'))
        self.layout.add_widget(self.booking_type_spinner)

        # Button to confirm selection
        self.confirm_button = Button(text='Confirm Selection', on_press=self.confirm_selection)
        self.layout.add_widget(self.confirm_button)

        self.add_widget(self.layout)

    def confirm_selection(self, instance):
        selected_car = self.car_spinner.text
        selected_color = self.color_spinner.text
        selected_vehicle_type = self.vehicle_type_spinner.text
        selected_booking_type = self.booking_type_spinner.text

        selected_car_details = f"Car: {selected_car}, Color: {selected_color}, Vehicle Type: {selected_vehicle_type}, Booking Type: {selected_booking_type}"
        self.selected_car_label.text = selected_car_details  
  


     

class Mapview(Screen):
    pass
class Bookinghistoryscreen(Screen):
    def printCustomerDetails(self):
        a = query.getCustomerBookingHistory(currentCustomer.id)
        customer_id_label = self.ids.customer_id_label
        customer_id_label.text = "CUSTOMER ID: "    + str(a[0])

        customer_pickup_label = self.ids.customer_pickup_label
        customer_pickup_label.text = "PICKUP POINT: "    + str(a[1])

        customer_destination_label = self.ids.customer_destination_label
        customer_destination_label.text = "DESTINATION: "    + str(a[2])

        number_of_passengers_label = self.ids.number_of_passengers_label
        number_of_passengers_label.text = "NUMBER OF PASSENGERS: "    + str(a[3])

        time_of_booking_label = self.ids.time_of_booking_label
        time_of_booking_label.text = "TIME OF BOOKING: "    + str(a[4])

        booking_status_label = self.ids.booking_status_label
        booking_status_label.text = "BOOKING STATUS: "    + str(a[5])

        transaction_id_label = self.ids.transaction_id_label
        transaction_id_label.text = "TRANSACTION ID: "    + str(a[6])

    def clearDetails(self):
        customer_id_label = self.ids.customer_id_label
        customer_id_label.text = ""

        customer_pickup_label = self.ids.customer_pickup_label
        customer_pickup_label.text = ""

        customer_destination_label = self.ids.customer_destination_label
        customer_destination_label.text = ""

        number_of_passengers_label = self.ids.number_of_passengers_label
        number_of_passengers_label.text = ""

        time_of_booking_label = self.ids.time_of_booking_label
        time_of_booking_label.text = ""

        booking_status_label = self.ids.booking_status_label
        booking_status_label.text = ""

        transaction_id_label = self.ids.transaction_id_label
        transaction_id_label.text = ""    

        self.manager.current='rider'




    
    

class Canceltripscreen(Screen):
    def cancel_trip(self):
        if query.customerHasCurrentBooking(currentCustomer.id):
            query.cancelCustomerBooking(currentCustomer.id)
            self.show_popup("Booking canceled")
        else:
            self.show_popup("No booking in progress")

    def show_popup(self, message):
        popup = Popup(title='Cancellation Confirmation',
                      content=Label(text=message),
                      size_hint=(None, None), size=(400, 200))
        popup.open()

def cancelCustomerBooking():
    if query.customerHasCurrentBooking(currentCustomer.id):
        query.cancelCustomerBooking(currentCustomer.id)
        print("Booking canceled")
    else:
        print("No booking in progress")

class Booktripscreen(Screen):
    def bookATrip(self):
        pickup_location = self.ids.pickup_location_field.text.strip()
        destination = self.ids.destination_field.text.strip()
        passengers = self.ids.passengers_field.text.strip()
        global pickup_time
        pickup_time = self.ids.pickup_time_field.text.strip()
        sharing = self.ids.sharing_field.text.strip()
        global waitingtime
        waitingtime=self.ids.waiting_field.text.strip()
        

        if not pickup_location or not destination or not passengers or not pickup_time or not sharing:
            self.show_error("Please fill in all fields.")
            return None

        try:
            passengers = int(passengers)
            sharing = sharing.lower() == 'true'
        except ValueError:
            self.show_error("Invalid input for passengers or sharing status.")
            self.clear_fields()
            return None

       ## if query.customerHasCurrentBooking(currentCustomer.id):
            #self.show_error("Cannot book a booking before completion/cancellation of existing booking")
           # return None

        driver_id = query.getNearestDriver(pickup_location, passengers, sharing)
        if driver_id is None:
            self.show_error("Cannot find a driver because of traffic")
            self.clear_fields()
            return None

        # Book the trip
        booking_status = "Ongoing"
        query.makeBooking(pickup_location, destination, passengers, pickup_time,
                                                booking_status, sharing, currentCustomer.id, driver_id)
        
        self.clear_fields()
        self.manager.current = "car_selection"

    def show_error(self, message):
        # Print the error message to the terminal for debugging
        print("Error:", message)

        # Display the error message in a popup
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text=message))
        popup = Popup(title='Error', content=content, size_hint=(None, None), size=(300, 200))
        popup.open()

    def show_cookie(self, message):
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text=message))
        popup = Popup(title='Confirmation', content=content, size_hint=(None, None), size=(300, 200))
        popup.open()

    def clear_fields(self):# Clear input fields
        self.ids.pickup_location_field.text=""
        self.ids.destination_field.text=""
        self.ids.passengers_field.text=""
        self.ids.pickup_time_field.text=""
        self.ids.sharing_field.text="" 

class Changepasswordscreen(Screen):
    def validate_and_update_password(self):
        old_password = self.ids.old_password.text
        new_password = self.ids.new_password.text
        confirm_password = self.ids.confirm_password.text
        
        if not (old_password and new_password and confirm_password):
            self.show_popup("Please fill all fields.")
            self.clear_fields() 
            
        elif old_password != currentCustomer.password:
            self.show_popup("Incorrect old password")
            self.clear_fields() 

        elif new_password != confirm_password:
            self.clear_fields() 
            self.show_popup("confirm Passwords not match")
        else:
        # All validations passed, update password using query
            query.updateCustomerPassword(currentCustomer.id, new_password)
            currentCustomer.password = new_password
            self.show_popup("Password updated successfully")
            self.clear_fields() 
            self.manager.current='rider'

        
    def clear_fields(self):# Clear input fields
        self.ids.old_password.text = ""
        self.ids.new_password.text = ""
        self.ids.confirm_password.text = ""
        
        # Show success message
    def show_popup(self, message):
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text=message))
        popup = Popup(title='Message', content=content, size_hint=(None, None), size=(300, 200))
        popup.open()
import kivy
kivy.require('2.0.0')  # Ensure proper version

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.clock import Clock
import pywhatkit as kit
import time
import os
from fpdf import FPDF
import webbrowser
class Whatsapp(Screen):
    def book_ride(self):
        phone_number = self.ids.phone_number.text
        
        # Simulate booking a ride and getting driver details
        ride_details = transaction_info
        name = currentCustomer.name
        phonenumber = currentCustomer.phoneNumber
        id = currentCustomer.id


        # Create a PDF file with the details
        save_path = "C:\\Users\\dhanu\\OneDrive\\Desktop"  # Path to save the PDF
        file_path = self.create_ride_details_pdf(ride_details, name, phonenumber, save_path)
        
        # Notify the user via WhatsApp
        self.notify_user(phone_number, ride_details, phonenumber, name, file_path)
        

    def create_ride_details_pdf(self, ride_details, name, phone_number, save_path):
        # Create a PDF file with the ride details
        file_name = f"Ride_Details_{time.strftime('%Y%m%d_%H%M%S')}.pdf"
        file_path = os.path.join(save_path, file_name)
        
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=ride_details, ln=True, align='L')
        pdf.cell(200, 10, txt=f"Name: {name}", ln=True, align='L')
        pdf.cell(200, 10, txt=f"Phone Number: {phone_number}", ln=True, align='L')
        
        pdf.output(file_path)
        return file_path
    

    def notify_user(self, phone_number, ride_details, phonenumber, name, file_path):
        try:
            # Send the PDF via WhatsApp
            kit.sendwhats_image(phone_number, file_path, f"Your ride details:\n{ride_details}\nName: {name}\nPhone Number: {phonenumber}", wait_time=5, tab_close=True, close_time=5)
            self.add_to_booking_history(f"Message with ride details sent to {phone_number}")
        except Exception as e:
            self.add_to_booking_history(f"An error occurred: {e}")
    
    def add_to_booking_history(self, message):
        booking_history = self.ids.booking_history
        booking_history.add_widget(Label(text=message, font_size='16sp', size_hint_y=None, height=40))
        booking_history.height += 50
        


class ClearWidgetsEvent(EventDispatcher):
    pass

class Checkdetails(Screen):
    def printCustomerDetails(self):
        # Assuming currentCustomer is defined somewhere
        id_label = self.ids.id_label
        id_label.text = "[Customer ID] :: " + str(currentCustomer.id)

        name_label = self.ids.name_label
        name_label.text = "[Name] :: " + currentCustomer.name

        phone_label = self.ids.phone_label
        phone_label.text = "[Phone number] :: " + currentCustomer.phoneNumber

        password_label = self.ids.password_label
        password_label.text = "[Password] :: " + currentCustomer.password

    def clearDetails(self):
        id_label = self.ids.id_label
        id_label.text = " "

        name_label = self.ids.name_label
        name_label.text = " "

        phone_label = self.ids.phone_label
        phone_label.text = " "

        password_label = self.ids.password_label
        password_label.text = " "
        self.manager.current="rider"


    
##############################################################

class Driverpage(Screen):
    def checkDetails(self):
        self.manager.current = 'dcheckdetails'

    def changePassword(self):
        self.manager.current = 'dchangepassword'

    def completeTrip(self):
        self.manager.current = 'dcompletetrip'

    def tripHistory(self):
        self.manager.current = 'dtriphistory'

    def transactionHistory(self):
        self.manager.current = 'dtransactionhistory'

    def signOut(self):
        self.manager.current = 'dsignout'

class Dcheckdetailscreen(Screen):
    def printCustomerDetails(self):
        # Assuming currentDriver is defined somewhere
        id_label = self.ids.id_label
        id_label.text = "[Driver ID] :: " + str(currentDriver.id)

        name_label = self.ids.name_label
        name_label.text = "[Name] :: " + currentDriver.name

        phone_label = self.ids.phone_label
        phone_label.text = "[Phone number] :: " + currentDriver.phoneNumber

        password_label = self.ids.password_label
        password_label.text = "[Password] :: " + currentDriver.password

        current_location_label = self.ids.current_location_label
        current_location_label.text = "[Current Location] :: " + "chennai"
        available_label = self.ids.available_label
        available_label.text = "[Available] :: " + "yes"

    def clearDetails(self):
        id_label = self.ids.id_label
        id_label.text = " "

        name_label = self.ids.name_label
        name_label.text = " "

        phone_label = self.ids.phone_label
        phone_label.text = " "

        password_label = self.ids.password_label
        password_label.text = " "

        current_location_label = self.ids.current_location_label
        current_location_label.text = " "

        available_label = self.ids.available_label
        available_label.text = " "

        self.manager.current = "driver"


class Dchangepasswordscreen(Screen):
    def validate_and_update_password(self):
        old_password = self.ids.old_password.text
        new_password = self.ids.new_password.text
        confirm_password = self.ids.confirm_password.text
        
        if not (old_password and new_password and confirm_password):
            self.show_popup("Please fill all fields.")
            self.clear_fields() 
            
        elif old_password != currentDriver.password:
            self.show_popup("Incorrect old password")
            self.clear_fields() 

        elif new_password != confirm_password:
            self.show_popup("confirm Passwords not match")
        else:
        # All validations passed, update password using query
            query.updateDriverPassword(currentDriver.id, new_password)
            currentDriver.password = new_password
            self.show_popup("Password updated successfully")
            self.clear_fields() 
            self.manager.current='driver'

        
    def clear_fields(self):# Clear input fields
        self.ids.old_password.text = ""
        self.ids.new_password.text = ""
        self.ids.confirm_password.text = ""
        
        # Show success message
    def show_popup(self, message):
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text=message))
        popup = Popup(title='Message', content=content, size_hint=(None, None), size=(300, 200))
        popup.open()

    pass



class Dtriphistoryscreen(Screen):
    def printCustomerDetails(self):
        a=query.getDriverTripHistory(currentDriver.id)
        customer_id_label = self.ids.customer_id_label
        customer_id_label.text = "DRIVER ID: "    + str(a[9])

        customer_pickup_label = self.ids.customer_pickup_label
        customer_pickup_label.text = "PICKUP POINT: "    + str(a[1])

        customer_destination_label = self.ids.customer_destination_label
        customer_destination_label.text = "DESTINATION: "    + str(a[2])

        number_of_passengers_label = self.ids.number_of_passengers_label
        number_of_passengers_label.text = "NUMBER OF PASSENGERS: "    + str(a[3])

        time_of_booking_label = self.ids.time_of_booking_label
        time_of_booking_label.text = "TIME OF BOOKING: "    + str(a[4])

        booking_status_label = self.ids.booking_status_label
        booking_status_label.text = "BOOKING STATUS: "    + str(a[5])

        transaction_id_label = self.ids.transaction_id_label
        transaction_id_label.text = "TRANSACTION ID: "    + str(a[6])

    def clearDetails(self):
        customer_id_label = self.ids.customer_id_label
        customer_id_label.text = ""

        customer_pickup_label = self.ids.customer_pickup_label
        customer_pickup_label.text = ""

        customer_destination_label = self.ids.customer_destination_label
        customer_destination_label.text = ""

        number_of_passengers_label = self.ids.number_of_passengers_label
        number_of_passengers_label.text = ""

        time_of_booking_label = self.ids.time_of_booking_label
        time_of_booking_label.text = ""

        booking_status_label = self.ids.booking_status_label
        booking_status_label.text = ""

        transaction_id_label = self.ids.transaction_id_label
        transaction_id_label.text = ""    

        self.manager.current='driver'



class Dsignoutscreen(Screen):
    def signOut(self):
        currentDriver.clear()
        self.manager.current = "Mainpage"
    

from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView


class CarSelectionScreen(Screen):
    def on_pre_enter(self):
        self.add_cars()

    def add_cars(self):
        grid_layout = self.ids.grid_layout

        # List of car images, replace the paths with your own images
        car_images = ['Dacia Duster - Dynamic (1).jpg', '2020-Mahindra-Thar-front-static.jpg', 'DSC06077.jpeg', 'mobil.jpeg', 'mobil2.jpeg',
                      'wp2506451.jpg','wp2506451.jpg', 'TOYOTA-Hilux-Double-Cab-6495_14.jpg', 'Mahindra_Thar_Photoshoot_At_Perupalem_Beach_West_Godavari_DistrictAPIndia__Djdavid.webp', 'GMC-Sierra-Double-Cab-5179_10.jpg','Audi e-tron GT 2021 UK-6.jpg','797386.jpg']

        for image_path in car_images:
            image = Image(source=image_path, size_hint=(None, None), size=(200, 200))
            grid_layout.add_widget(image)
import random
import smtplib
class Otp(Screen):
    def send_otp(self):
        name = self.ids.name.text
        email = self.ids.emailid.text

        # Perform email validation
        valid_email = self.email_verification(email)
        if not valid_email:
            return

        global OTP
        OTP = random.randint(100000, 999999)  # Generate a random 6-digit OTP

        try:
            # Configure SMTP server
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()

            # Login to SMTP server
            server.login("priyanshu25122002@gmail.com", "stqqwjqoocucknsx")  # Update with your email and password

            # Send email
            self.sending_otp(server, valid_email)

            # Close server connection
            server.quit()

            # Update status
            self.ids.status.text = "OTP sent successfully"
        except Exception as e:
            self.show_error_popup(f"Error: {str(e)}")

    def email_verification(self, receiver_email):
        email_check1 = ["gmail","hotmail","yahoo","outlook"]
        email_check2 = [".com",".in",".org",".edu",".co.in"]
        count = 0

        for domain in email_check1:
            if domain in receiver_email:
                count += 1
        for site in email_check2:
            if site in receiver_email:
                count += 1

        if "@" not in receiver_email or count != 2:
            self.show_error_popup("Invalid email id")
            return False
        return receiver_email

    def sending_otp(self, server, receiver_email):
        global new_otp
        new_otp = random.randint(100000, 999999)

        body = f"Dear {self.ids.name.text},\n\nYour OTP is {new_otp}."
        subject = "THANK YOU SO MUCH FOR BOOKING OUR CAB! HAVE A SAFE JOURNEY !!!! WE ALWAYS WELCOMES YOU"
        message = f"Subject: {subject}\n\n{body}"

        server.sendmail("priyanshu25122002@gmail.com", receiver_email, message)
        print("OTP has been sent to", receiver_email)

    def validate_otp(self):
        entered_otp = self.ids.otp_field.text.strip()
        if not entered_otp:
            self.show_error_popup("Please enter the OTP.")
        elif str(entered_otp)== str(new_otp):
            self.show_popup("OTP verified successfully!")
            self.ids.name.text=""
            self.ids.emailid.text=""
            self.ids.otp_field.text=""
            self.manager.current='maketransaction'
        else:
            self.show_error_popup("Invalid OTP.")

    def show_error_popup(self, message):
        popup = Popup(title='Error', content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()
        
            

    def show_popup(self, message):
        popup = Popup(title='OTP Verification', content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()
import webbrowser    

class Webpage(Screen):
    def open_google_maps(self):
        # Open Google Maps webpage in the default browser
        webbrowser.open("https://www.google.com/maps")
class Bill(Screen):
    def send_hi(self):
        name = self.ids.name.text
        email = self.ids.emailid.text
        billcontent = "transaction_info"

        # Perform email validation
        valid_email = self.email_verification(email)
        if not valid_email:
            return

        try:
            # Configure SMTP server
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()

            # Login to SMTP server
            server.login("priyanshu25122002@gmail.com", "stqqwjqoocucknsx")  # Update with your email and password

            # Send email
            self.sending_bill(server, valid_email)

            # Close server connection
            server.quit()

            # Update status
            self.ids.status.text = "MAIL SENT SUCCESSFULLY"
        except Exception as e:
            self.show_error_popup(f"Error: {str(e)}")

    def email_verification(self, receiver_email):
        email_check1 = ["gmail", "hotmail", "yahoo", "outlook"]
        email_check2 = [".com", ".in", ".org", ".edu", ".co.in"]
        count = 0

        for domain in email_check1:
            if domain in receiver_email:
                count += 1
        for site in email_check2:
            if site in receiver_email:
                count += 1

        if "@" not in receiver_email or count != 2:
            self.show_error_popup("Invalid email id")
            return False
        return receiver_email

    def sending_bill(self, server, receiver_email):
        body = f"Dear {self.ids.name.text},\n\nThis is your bill for the ride\n\n {transaction_info}!."
        subject = "Thank you for choosing our cab service !!"
        message = f"Subject: {subject}\n\n{body}"

        server.sendmail("priyanshu25122002@gmail.com", receiver_email, message)
        self.clearDetails()
        self.manager.current='review'
        print("Mail has been sent to", receiver_email)

    def clearDetails(self):
        self.ids.name.text = ""
        self.ids.emailid.text = ""
        self.ids.review.text = ""
        self.manager.current = 'review'

    def show_error_popup(self, message):
        popup = Popup(title='Error', content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()

from kivy.uix.slider import Slider
from kivy.uix.textinput import TextInput
import smtplib
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class SendReview(Screen):
    def on_slider_value_change(self, instance, value):
        self.ids.rating_label.text = f'Rating: {int(value)}'

    def send_review(self):
        email = "priyanshu25122002@gmail.com"  # Update with your email address
        password = "stqqwjqoocucknsx"  # Update with your email password

        rating = self.ids.rating_slider.value
        review = self.ids.review_input.text
        receiver_email = self.ids.email_input.text  # Fetch the receiver's email from the TextInput widget

        try:
            # Configure SMTP server
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()

            # Login to SMTP server
            server.login(email, password)

            # Construct email message
            body = f"Rating: {rating}\nReview: {review}"
            subject = "SSN CAB SERVICE REVIEW!!\n THANK YOU FOR YOUR RESPONSE!"
            message = f"Subject: {subject}\n\n{body}"

            # Send email
            server.sendmail(email, receiver_email, message)  # Send email to the receiver's email

            # Close server connection
            server.quit()

            # Show confirmation popup
            popup = Popup(title='Review Sent', content=Label(text='Thank you for your review!'),
                          size_hint=(None, None), size=('400dp', '200dp'))
            popup.open()

            # Clear input fields
            self.ids.rating_slider.value = 0
            self.ids.review_input.text = ""
            self.ids.email_input.text = ""
            self.manager.current='what'

        except Exception as e:
            popup = Popup(title='Error', content=Label(text=f"Error: {str(e)}"),
                          size_hint=(None, None), size=('400dp', '200dp'))
            popup.open()

from kivy.uix.video import Video
from kivy.uix.videoplayer import VideoPlayer

#######################################
class WindowManager(ScreenManager):
    pass



class AwesomeApp(MDApp):
    def build(self):
        # Load the KV file
        kv = Builder.load_file("new1.kv")
        Builder.load_file("main.kv")
        
        wm = WindowManager()
        wm.real_add_widget(Start(name='start'))
        wm.add_widget(Continue(name='continue'))
        wm.add_widget(Otp(name='otp'))
        wm.add_widget(Mainpage(name='Mainpage'))
        wm.add_widget(Roptionpage(name='rideroption'))
        wm.add_widget(Doptionpage(name='driveroption'))
        wm.add_widget(Rlogin(name='riderlogin'))
        wm.add_widget(Rsignin(name='ridersignin'))
        wm.add_widget(Dlogin(name='driverlogin'))
        wm.add_widget(Dsignin(name='driversignin'))
        wm.add_widget(Riderpage(name='rider'))
        wm.add_widget(Driverpage(name='driver'))
        wm.add_widget(Signoutscreen(name='signout'))
        wm.add_widget(Maketransactionscreen(name='maketransaction'))
        wm.add_widget(Bookinghistoryscreen(name='bookinghistory'))
        wm.add_widget(Canceltripscreen(name='canceltrip'))
        wm.add_widget(Booktripscreen(name='booktrip'))
        wm.add_widget(Changepasswordscreen(name='changepassword'))
        wm.add_widget(Checkdetails(name='checkdetails'))
        wm.add_widget(Dcheckdetailscreen(name='dcheckdetails'))
        wm.add_widget(Dchangepasswordscreen(name='dchangepassword'))
        wm.add_widget(Dtriphistoryscreen(name='dtriphistory'))
        wm.add_widget(Dsignoutscreen(name='dsignout'))
        wm.add_widget(Hii(name='map'))
        wm.add_widget(CarSelectionScreen(name='car_Selection'))
        wm.add_widget(SelectionScreen(name='selection'))
        wm.add_widget(Webpage(name='web'))
        wm.add_widget(Bill(name='bill'))
        wm.add_widget(SendReview(name='review'))
        wm.add_widget(SplashScreen(name='team'))
        wm.add_widget(Whatsapp(name='what'))

        return kv


if __name__ == '__main__':
    AwesomeApp().run()
