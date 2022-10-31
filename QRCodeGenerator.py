import ssl
import json
import qrcode
import smtplib
import openpyxl
from os import system
from email.message import EmailMessage

system('cls')
print('==> {:.2f} %'.format(0))


def tstamp_to_id(tstamp):
    date, time = tstamp.split(" ")
    date = date.split("-")
    time = time.split(":")
    date.pop(0)
    date.extend(time)
    return "".join(date)


excel_path = "participante.xlsx"
with open("apppassword.txt", "r") as apppass:
    app_pass = apppass.readline().strip()

# Define email sender and receiver
email_sender = 'merali.med@gmail.com'
email_password = app_pass
# Set the subject and body of the email (event name for exp)
subject = 'The Purge has began!'

# To open the workbook workbook object is created
wb_obj = openpyxl.load_workbook(excel_path)
# Get workbook active sheet object from the active attribute
sheet = wb_obj.active

json_data = {}

for row_id in range(2, sheet.max_row+1):
    id_cell = sheet.cell(row=row_id, column=1).value
    prtc_id = tstamp_to_id(str(id_cell))
    prtc_first_name = sheet.cell(row=row_id, column=2).value
    prtc_last_name = sheet.cell(row=row_id, column=3).value
    prtc_email = sheet.cell(row=row_id, column=4).value
    json_data[prtc_id] = [prtc_first_name,
                          prtc_last_name, prtc_email, id_cell, []]

    # Data to be encoded
    # data = 'QR Code using make() function'
    data = f"{prtc_id}-{prtc_first_name}-{prtc_last_name}"

    # Encoding data using make() function
    img = qrcode.make(data)
    # TODO: check if the folder exist
    # Saving as an image file
    img.save(f'Generated QR code/id-{row_id-1}.png')

    body = f"""
    Good evening {prtc_first_name} {prtc_last_name}
    we hope that all is good
    
    that's a test of the auto emails script
    in the next email you will receive your QR code
    
    
    Best regards,
    GDG
    """
    email_receiver = prtc_email
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)
    with open(f"Generated QR code\id-{row_id-1}.png", 'rb') as fp:
        img_data = fp.read()
    em.add_attachment(img_data, maintype='image', subtype='png')

    # Sending the email:
    # Add SSL (layer of security)
    context = ssl.create_default_context()
    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

    system('cls')
    print('==> {:.2f} %'.format((row_id)*100/sheet.max_row))

# TODO: check if the file exist
with open("participantes_data.json", "w") as prtc_data_file:
    prtc_data_file.write(json.dumps(json_data, indent=4))

print('>> All is Done Here xD')
