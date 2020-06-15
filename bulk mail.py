import smtplib as s

ob=s.SMTP("smtp.gmail.com", 587)

ob.starttls()

ob.login("pshiv8822@gmail.com", "aerospace2807")


subject="sending mail using python"
body="""hi! I am sending an email using python 
           shiv here"""

message="subject:{}\n\n{}".format(subject, body)

listOfaddress = ["pshiv8822@gmail.com", "shiv2802@gmail.com"]

ob.sendmail("pshiv8822@gmail.com", listOfaddress,message)


print("send successfully...")
ob.quit()

