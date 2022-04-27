# the following is the code to get the data of the firemen that will go to the event
# the data comes from a google sheet and is stored in a json file
# we will need to connnect to the google api to get the sheet data

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import pandas as pd
import qrcode


## CONNECT TO THE GOOGLE SHEET


def get_data():
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive",
    ]

    keys = {
        "type": "service_account",
        # deleted the key for sen
    }

    creds = ServiceAccountCredentials.from_json_keyfile_dict(keys, scope)
    client = gspread.authorize(creds)

    sheet = client.open(
        "Formulario Entrada FIBOM (respuestas)"
    ).sheet1  # Open the spreadhseet

    # print the data
    data = sheet.get_all_records()
    # pprint(data)

    return sheet, data


## DATA MANIPULATION


def use_data(sheet, data):
    # Use the data to create a dataframe
    df = pd.DataFrame(data)
    print("Data: ")
    print(df)
    print()

    # now create a loop to get the data from the dataframe
    for index, row in df.iterrows():
        # check if the row is empty
        if row["Ingrese su nombre completo "] == "":
            continue

        name = row["Ingrese su nombre completo "]
        email = row["Dirección de correo electrónico"]
        rut = row["Ingrese su rut (12345678-9)"]

        # create a str that will be the link to the users page
        # the link should be in the format:
        # http://aws-react-fibom.s3-website-sa-east-1.amazonaws.com/{name}&{email}&{rut}
        link = (
            "http://aws-react-fibom.s3-website-sa-east-1.amazonaws.com/"
            + name
            + "&"
            + email
            + "&"
            + rut
        )

        # add a col to the sheet with the link
        sheet.update_cell(index + 2, 13, link)

        # now convert the link to a QR code
        qr = qrcode.make(link)
        name = name.replace(" ", "_")
        qr.save(
            "C:\\Users\\satel\\OneDrive\\code\\Fibom-4\\fibom-app\\users-data\\qr_codes_"
            + name
            + ".png"
        )
    print("QR codes created")


## RUNNING THE CODE

sheet, data = get_data()
use_data(sheet, data)
