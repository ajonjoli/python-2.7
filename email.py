import smtplib

content = 'example email stuff here'
mail = smtplib.SMTP('smtp.gmail.com',587)	#conection, port
mail.ehlo()
mail.starttls()
mail.login('fromemail','password')

mail.sendmail('fromemail','receiver',content)

mail.close()
