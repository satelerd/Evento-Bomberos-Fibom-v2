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
        "project_id": "ethereal-yen-314221",
        "private_key_id": "87d1a013b6dae57df82a207d9e32f26fc456082a",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCTCGytydKgldNL\nUuuO+PtIQiuY6o10PmUYcamdyyt8pA+/zcmjHRtm/helt5XhZ9DdgXe05z6+KNoE\ng57hI3zlSGTtPT6bM/7dHlwJBJs1gF+4bfyxguZhisDEFCRMpEskLxu5HM4TfsU/\nUHZL1VDHxrsjLw+9kzKK3Gw/p5gJE7q77oA5AKAl8EDg5DDK/jFHMUtEETO7H3Vb\nFaf1HGNTHiXBDLLlG63tdbiDiOjQfQrPvK0dgeSlwduYnztZWCPvBRywbb2WTaWM\ncJeNvrvxlSr2vfaYCIAzOBhUxkM2BfEZXMkulLK1rNCSuXqXuZhRTZ0VY3X38BkW\nX9puCjodAgMBAAECggEAFua0RMJfee80NLKC6ac6vme+EiiQZUd1qB/GD0OOr7B/\nGn0jV7JoKvvPM5rbb7sjk2i/vC/bfDNxN8xHciI8qRrES5ZjOrnXy9mXdLkgsq3e\n2uNYvU5Z813xBelsOPrLEGT9ALFtoKg5cVHnRwr/9Mntqn6BSWIUuH+6JZUFT35k\nYRnWD1FaZYpwrPyD0UOhmlpGCtLCh9WHsRID2S6y0k7UrfAXZ7xRfGCv4w75LrbI\nUbP3dAmbslAu2vjZdOtTKQ+vkjZGlgoruT6igP4wdexsRViNqeFhSqEa1nWy4m53\nW1/ZPJH+P17tVmCk8FJ2hd2SXc89a13UqLUu7ydLaQKBgQDPOBD4pqC6TyIEA2jw\nGeB6Q36eetDAexLOTIvzeJ2DgzbEJFQuQhg3JUCOnqH4spd1oVXp/Y3evKiUq5gK\ngjRDt4QWlf/+8qFSJpwqDiOLlxl4g88xUviHTJftmcNBi/t9XkxSEodWWA8plda7\nGn/IskpSu8rGfJsDK+nP0cOiWQKBgQC1pUcW2bUq0LJbZpIpN5p5QGecIzVxtjUh\nIFBQVa9IapmHubr5OIQriK8902aFcEnVzDDziilCiOFFfhRtkZUxeCSF4IAFENXk\n0590ZfOrL/78qD4TjJlek74BZhMXoVEsgQ7IPfwMX5e6eqap0l8Wqv3xWppqnLmb\nmTJUtdz1ZQKBgQCkPWP2MNujz6S+WZWK+HebcHOjWOSsKuA08ybZyvfNjOqTe9fc\n8jYPP09zuvfWDndNnJpj47vWluFnNLpFWf3izkm7PRiyEc0bN87+5kX2FcTyaEaI\naaLiWirw/7Zq9XBXZa5IPrdWEGW0KDcSBWbSw7105bNKruiOEvg256OPwQKBgEDK\nQyETZltvNS8E1v18p8y3/DzlEhsNMsYuEHeXGH5sB3cx+E8MqZgdmOQkk1zlQHDR\n9GPp0+23hSKUZhTu6JhMkjpuaTtlVeXY1fdephtZc0oLeJjgfZQOfqdhEU5Ma/fD\n0NH7yftf3W7WcLwCHYioVQvRlWKRpGKrshglBjtBAoGAWJ485AV6CvrUohsLctzj\nswGLVe10j5rZYicy3F/VXF/shA7o44As7EVGoJs9d9rTxsvGM+2Gtl9K481jKjYh\n0LgZHmR//AE6Eo8FZhMlb2d/zmDP/8A+moOnbA91uii5oACg0trm5JVS3seE536/\nyyrvxuUNBLqVNnMkhJPh2LY=\n-----END PRIVATE KEY-----\n",
        "client_email": "service-fibon@ethereal-yen-314221.iam.gserviceaccount.com",
        "client_id": "116065369919362938975",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/service-fibon%40ethereal-yen-314221.iam.gserviceaccount.com",
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
