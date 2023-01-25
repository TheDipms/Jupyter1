from datetime import datetime


def create_contact() :
    firstname = input('Enter first name')
    lastname = input('Enter last name')
    phone_number = input('Phone nimber')
    date = datetime.today()
    print(firstname, lastname, phone_number, date)

    my_dict = {
        "Firstname": firstname,
        "Lastname": lastname,
        "Phone Number": phone_number,
        "Date": date  
        }
    return my_dict
