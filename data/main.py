#############################################
##                                         ##
##            MASS_SENDER_GMAIL            ##
##                                         ##
#############################################

#lib
import sys
import json
import getpass
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

#get user id
USER = getpass.getuser()

#open email_data.txt 
with open('data/email_data.txt', 'r') as e:
    email_data = e.read()

#open data.csv
#with open('data/data.csv', 'r') as d:
csv_data = pd.read_csv('data/data.csv')

#open setup.json 
with open('data/setup.json', 'r') as s:
    json_data = json.load(s)

#var
msg = MIMEMultipart()
msg['From'] = json_data['SENDER_INFO']['sender_email'] #var for sender
try: 
    msg['To'] = json_data['EMAIL_INFO']['email'] #To rename info
except:
    msg['To'] = json_data['SENDER_INFO']['sender_email']

msg['Subject'] = json_data['EMAIL_INFO']['subject'] #subject info


#var for login
SENDER = json_data['SENDER_INFO']['sender_email']
PASSWORD = json_data['SENDER_INFO']['sender_email_password']


#message attach
try:
    message = email_data
    msg.attach(MIMEText(message))
except:
    print('error on attach message')

#message add img
try: 
    IMG_PATH = json_data['EMAIL_INFO']['img_path']
    open_img = open(IMG_PATH, 'rb')
    img =  MIMEImage(open_img.read())
    open_img.close()
    msg.attach(img)
except:
    pass


#sender module
i = 0 #conteur I++ pour lecture de la liste csv
def Sender():
    try:               
        TO = csv_data.loc[i]['email']
        
        mailserver = smtplib.SMTP('smtp.gmail.com', 587)
        mailserver.ehlo()
        mailserver.starttls()
        mailserver.ehlo()
        mailserver.login(SENDER, PASSWORD)
        mailserver.sendmail(SENDER, TO, msg.as_string())
        mailserver.quit()
    except:
        pass


print('')
print(' - |',USER,'| - exit[0]')
print("""______________________
┏┓┳┳┓┏┳┓┏┓  ┏┓       
┗┓┃┃┃ ┃ ┃┃  ┗┓┏┓┏┓┏┳┓
┗┛┛ ┗ ┻ ┣┛  ┗┛┣┛┗┻┛┗┗
              ┛   """)
print('Sender :',SENDER)
print('______________________')
print('')
var = input('- Launch : ')
if var == '0':
    sys.exit()
print('')

x = 1
try:
    while (x < 200):
        try: 
                Sender()
                x +=1
                i +=1
                print('Sending email... : ',str(x), end='\r')
        except StopIteration:
            break
except:
    pass

print('------- End / Mail Sent -------')
print('')
