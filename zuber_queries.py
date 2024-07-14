###########################################################################################################
from database import Database

database = Database()
from geopy.geocoders import Nominatim
from geopy import distance

def executeAndPrintQuery(query: str):
    database.executeAndPrintQuery(query)

def executeQuery(query: str):
    database.executeQuery(query)

def lastInsertIds() -> int:
    database.nonCommitQuery("SELECT last_insert_id();")
    ret = database.getCursor().fetchall()[0][0]
    database.commit()
    return ret

def selectCustomers():
    database.nonCommitQuery("SELECT * FROM customer;")
    data = database.getCursor().fetchall()
    print("Customers:")
    for record in data:
        print(f"ID: {record[0]}, Name: {record[1]}, Password: {record[2]}, Current Booking: {record[3]}, Phone Number: {record[4]}")

def selectDrivers():
    database.nonCommitQuery("SELECT * FROM driver;")
    data = database.getCursor().fetchall()
    print("Drivers:")
    for record in data:
        print(f"ID: {record[0]}, Name: {record[1]}, Password: {record[2]}, Current Booking: {record[3]}, Phone Number: {record[4]}, Car ID: {record[5]}, Current Location: {record[6]}, Working Status: {record[7]}")

def selectCars():
    database.nonCommitQuery("SELECT * FROM car;")
    data = database.getCursor().fetchall()
    print("Cars:")
    for record in data:
        print(f"ID: {record[0]}, Brand: {record[1]}, Model: {record[2]}, Registration Number: {record[3]}, Capacity: {record[4]}, Price per km: {record[5]}")

def selectBookings():
    database.nonCommitQuery("SELECT * FROM booking;")
    data = database.getCursor().fetchall()
    print("Bookings:")
    for record in data:
        print(f"ID: {record[0]}, Pickup Location: {record[1]}, Destination: {record[2]}, # People: {record[3]}, Pickup Time: {record[4]}, Booking Status: {record[5]}, Transaction ID: {record[6]}, Sharing: {record[7]}, Customer ID: {record[8]}, Driver ID: {record[9]}, Car ID: {record[10]}")

def selectTransactions():
    database.nonCommitQuery("SELECT * FROM transaction;")
    data = database.getCursor().fetchall()
    print("Transactions:")
    for record in data:
        print(f"ID: {record[0]}, Payment Type: {record[1]}, Amount: {record[2]}")


def insertCustomer(name: str, password: str,
                   currentBooking, phoneNumber: str):
    if currentBooking == None:
        database.executeQuery(
            f"INSERT INTO customer VALUES(0, '{name}', '{password}', NULL, '{phoneNumber}');")
    else:
        database.executeQuery(
            f"INSERT INTO customer VALUES(0, '{name}', '{password}', {currentBooking}, '{phoneNumber}');")


def insertCar(brand: str, model: str, registration_number: str, capacity: int, price_per_km: int):
    database.executeQuery(
        f"INSERT INTO car VALUES(0, '{brand}', '{model}', '{registration_number}', {capacity}, {price_per_km});")


def insertDriver(name: str, password: str,
                 currentBooking, phoneNumber: str, car_id: int,
                 currentLocation, workingStatus):
    if workingStatus == True:
        workingStatus = "TRUE"
    else:
        workingStatus = "FALSE"
    database.executeQuery(
        f"INSERT INTO driver VALUES(0, '{name}', '{password}', NULL, '{phoneNumber}', {car_id},'{currentLocation}', {workingStatus});")


def authenticateCustomer(phoneNumber: str, password: str):
    database.nonCommitQuery(
        f"SELECT * FROM customer WHERE phone_number = '{phoneNumber}' AND password = '{password}';")
    ret = database.getCursor().fetchall()
    database.commit()
    return ret        

def updateCustomerPassword(id: int, password: str):
    database.executeQuery(f"UPDATE customer SET password = '{password}' WHERE customer_id = '{id}';")
    database.commit()

def setCustomerCurrentBooking(customerId, bookingId):
    database.executeQuery(f"UPDATE customer SET current_booking = {bookingId} WHERE customer_id = {customerId};")
    database.commit()

def setDriverCurrentBooking(driverId, bookingId):
    database.executeQuery(f"UPDATE driver SET current_booking = {bookingId} WHERE driver_id = {driverId};")
    database.commit()

def customerHasCurrentBooking(customerId):
    database.nonCommitQuery("SELECT * FROM customer;")
    data = database.getCursor().fetchall()
    customer = [record for record in data if record[0] == customerId][0]
    return customer[3] is not None

def driverHasCurrentBooking(driverId):
    database.nonCommitQuery("SELECT * FROM driver;")
    data = database.getCursor().fetchall()
    driver = [record for record in data if record[0] == driverId][0]
    return driver[3] is not None

def cancelCustomerBooking(customerId):
    database.nonCommitQuery("SELECT * FROM customer;")
    data = database.getCursor().fetchall()
    customer = [record for record in data if record[0] == customerId][0]
    database.executeQuery(f"UPDATE booking SET booking_status = 'Canceled' WHERE booking_id = {customer[3]};")


def getCustomerBookingHistory(customerId):
    database.nonCommitQuery(f"SELECT * FROM booking WHERE customer_id = {customerId} ORDER BY booking_id DESC;")
    data = database.getCursor().fetchall()
    print("Customer Booking History:")
    customer = [record for record in data if record[8] == customerId]
    if customer:
        print(customer)
        return customer[0]
    else:
        return None

    

def getCurrentBooking(customerId):
    database.nonCommitQuery(f"SELECT * FROM customer WHERE customer_id = {customerId};")
    customer = database.getCursor().fetchall()[0]
    currentBookingId = customer[3]
    database.nonCommitQuery(f"SELECT * FROM booking WHERE booking_id = {currentBookingId};")
    currentBooking = database.getCursor().fetchall()[0]
    carId = currentBooking[10]
    database.nonCommitQuery(f"SELECT * FROM car WHERE car_id = {carId};")
    car = database.getCursor().fetchall()[0]
    return currentBooking, car

def getLocationCoordinates(location: str):
    location = location.lower().replace(" ", "")
    hash_table = {
        'a': (0, 0), 'b': (0, 1), 'c': (0, 2),
        'd': (1, 0), 'e': (1, 1), 'f': (1, 2),
        'g': (2, 0), 'h': (2, 1), 'i': (2, 2),
        'j': (3, 0), 'k': (3, 1), 'l': (3, 2),
        'm': (4, 0), 'n': (4, 1), 'o': (4, 2),
        'p': (5, 0), 'q': (5, 1), 'r': (5, 2),
        's': (6, 0), 't': (6, 1), 'u': (6, 2),
        'v': (7, 0), 'w': (7, 1), 'x': (7, 2),
        'y': (8, 0), 'z': (8, 1), '0': (8, 2),
        '1': (9, 0), '2': (9, 1), '3': (9, 2),
        '4': (10, 0), '5': (10, 1), '6': (10, 2),
        '7': (11, 0), '8': (11, 1), '9': (11, 2),
    }
    x = 0
    y = 0
    for char in location:
        if char in hash_table:
            x += hash_table[char][0]
            y += hash_table[char][1]
    return x, y

def distances(location1,location2):
    print(location1,location2)
    geocoder=Nominatim(user_agent="i know python")
    coordinates1=geocoder.geocode(location1)
    coordinates2=geocoder.geocode(location2)

    lat1,long1=(coordinates1.latitude),(coordinates1.longitude)
    lat2,long2=(coordinates2.latitude),(coordinates2.longitude)

    place1=(lat1,long1)
    place2=(lat2,long2)
    print(distance.distance(place1,place2))

    return (distance.distance(place1,place2))

def getNearestDriver(pickupLocation: str, numberOfPeople: int, sharing: bool):
    database.nonCommitQuery("SELECT * FROM driver;")
    driverData = database.getCursor().fetchall()[-4:]
    database.nonCommitQuery("SELECT * FROM car;")
    carData = database.getCursor().fetchall()
    if len(driverData) == 0:
        return None
    nearestDriverId = driverData[0][0]
    nearestDistance = distances(pickupLocation,driverData[0][6])
    flag = False
    for driver in driverData:
        if driver[7]:  # if driver is working
            carId = driver[5]
            car = [record for record in carData if record[0] == carId][0]
            if car[4] >= numberOfPeople:  # if capacity >= numberOfPeople
                currentDistance = distances(pickupLocation, driver[6])
                if nearestDistance >= currentDistance:
                    flag = True
                    nearestDriverId = driver[0]
                    nearestDistance = currentDistance
    if flag:
        return nearestDriverId
    else:
        return None

def makeBooking(pickupLocation, destination, numberOfPeople, pickupTime, bookingStatus, sharing, customerId, driverId):
    database.nonCommitQuery("SELECT * FROM driver;")
    driverData = database.getCursor().fetchall()
    driver = [record for record in driverData if record[0] == driverId][0]
    carId = driver[5]
    database.executeQuery(
        f"INSERT INTO booking VALUES(0,'{pickupLocation}', '{destination}', {numberOfPeople}, '{pickupTime}', '{bookingStatus}', NULL, {sharing}, {customerId}, {driverId}, {carId});")
    bookingId = lastInsertIds()
    setCustomerCurrentBooking(customerId, bookingId)
    setDriverCurrentBooking(driverId, bookingId)

def getCustomerTransactionHistory(customerId):
    database.nonCommitQuery(
        f"SELECT transaction.* FROM transaction, booking WHERE booking.customer_id = {customerId} AND booking.transaction_id = transaction.transaction_id;")
    data = database.getCursor().fetchall()
    print("Customer Transaction History:")
    for record in data:
        print(f"ID: {record[0]}, Payment type: {record[1]}, Amount: {record[2]}")

def makeTransaction(bookingId, paymentType, amount):
    print(bookingId,paymentType,amount)
    database.executeQuery(
        f"INSERT INTO transaction VALUES(0, '{paymentType}', {amount});")
    transactionId = lastInsertIds()
    database.executeQuery(
        f"UPDATE booking SET transaction_id = {transactionId}, booking_status = 'Completed' WHERE booking_id = {bookingId};")
    database.nonCommitQuery(
        f"SELECT * FROM booking WHERE booking_id = {bookingId};")
    booking = database.getCursor().fetchall()[0]
    destination = booking[2]
    driverId = booking[9]
    database.executeQuery(
        f"UPDATE driver SET current_location = '{destination}' WHERE driver_id = {driverId};")


def authenticateDriver(phoneNumber: str, password: str):
    database.nonCommitQuery(
        f"SELECT * FROM driver WHERE phone_number = '{phoneNumber}' AND password = '{password}';")
    ret = database.getCursor().fetchall()
    database.commit()
    print(ret)
    return ret


def updateDriverPassword(id: int, password: str):
    database.executeQuery(
        f"UPDATE driver SET password = '{password}' WHERE driver_id = '{id}';")
    database.commit()


def cancelDriverBooking(driverId):
    database.nonCommitQuery("SELECT * FROM driver;")
    data = [record for record in database.getCursor().fetchall()]
    driver = [record for record in data if record[0] == driverId][0]
    database.executeQuery(
        f"UPDATE booking SET booking_status = 'Canceled' WHERE driver_id = {driverId} AND booking_status = 'Ongoing';")


def getDriverTripHistory(driverId):
    database.nonCommitQuery(
        f"SELECT * FROM booking WHERE driver_id = {driverId} ORDER BY booking_id DESC ;")
    data = [record for record in database.getCursor().fetchall()]
    return data[0]


def getDriverTransactionHistory(driverId):
    try:
        database.nonCommitQuery(
            f"SELECT transaction.* FROM transaction, booking WHERE booking.driver_id = {driverId} AND booking.transaction_id = transaction.transaction_id;")
    except mysql.connector.errors.ProgrammingError:
        print("you havent done any transactions!")
    data = [record for record in database.getCursor().fetchall()]
    print(data)


def getCurrentTrip(driverId):
    database.nonCommitQuery(
        f"SELECT * FROM booking WHERE driver_id = {driverId} AND booking_status = 'Ongoing';")
    return database.getCursor().fetchall()


def completeTrip(tripId):
    database.executeQuery(
        f"UPDATE booking SET booking_status = 'Completed' WHERE booking_id = {tripId};")
    database.nonCommitQuery(
        f"SELECT * FROM booking WHERE booking_id = {tripId};")
    booking = [record for record in database.getCursor().fetchall()][0]
    destination = booking[2]
    driverId = booking[9]
    database.executeQuery(
        f"UPDATE driver SET current_location = '{destination}' WHERE driver_id = {driverId};")


def insertTripHistory(tripId, driverId):
    database.executeQuery(
        f"INSERT INTO trip_history VALUES({tripId}, {driverId});")


def makeDriverTransaction(driverId, paymentType, amount):
    database.executeQuery(
        f"INSERT INTO transaction VALUES(0, '{paymentType}', {amount});")
    transactionId = lastInsertIds()
    database.executeQuery(
        f"UPDATE booking SET transaction_id = {transactionId}, booking_status = 'Completed' WHERE driver_id = {driverId} AND booking_status = 'Ongoing';")
if __name__ == "__main__":
    # selectCustomers()
    # print(getNearestDriver("hello 27r8ygbvwnwnvlkm;v, .  ,nmoto", 9, False))
    # getCustomerTransactionHistory(99)
    # print(getCurrentBooking(100))
    makeTransaction(81, "UPI", 69)
    pass
