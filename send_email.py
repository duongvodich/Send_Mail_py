from http import client
import smtplib


email = 'duongtuyen.art@gmail.com'
password = 'lfdfqxcjkxyvmvpk'
send_to = input('Vui lòng nhập email cần gửi đến: ')
message = input('Nhập content cần gửi đi: ')

#gửi email
#SMTP of gmail
client = smtplib.SMTP('smtp.gmail.com', 587)
client.starttls()
client.login(email, password)

client.sendmail(email, send_to, message)
print('Message send to '+ send_to)
client.quit()