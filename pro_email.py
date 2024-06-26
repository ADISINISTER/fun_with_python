import smtplib as s

ob = s.SMTP('smtp.gmail.com', 587)
ob.ehlo()
ob.starttls()

ob.login('sujeetkyt102@gmail.com', 'gplljfmltgypxsvm') # password generated from app password of email

subject = "test python"
body = "I Love Python"

massage = "subject:{}\n\n{}".format(subject, body)
listadd = ['sujeetk102@gmail.com']

ob.sendmail('sujeetkyt102@gmail.com', listadd, massage)
print("Mail sent")

ob.quit()
