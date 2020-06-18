import requests
from bs4 import BeautifulSoup
import smtplib as s


url = 'https://www.mohfw.gov.in/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

conformed = soup.find(id='site-dashboard').get_text()
print(conformed.strip())

ob=s.SMTP("smtp.gmail.com", 587)


listOfaddress = [reciver email, reciver email]



ob.starttls()

ob.login(sender email, password)


subject="TODAY'S COVID-19 CASES"
body = f"""{conformed}
link - https://www.mohfw.gov.in/
"""

message="subject:{}\n\n{}".format(subject, body)

listOfaddress = [reciver email, reciver email]

ob.sendmail(sender email, listOfaddress,message)


print("send successfully...")
ob.quit()

