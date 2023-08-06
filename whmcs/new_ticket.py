import config
import datetime
import requests
import template_message

access = config.db.cursor()
access.execute("SELECT * FROM tbltickets WHERE date >= date_sub(now(), interval 5 minute); ")
resultNewTicket = access.fetchall()
for x in resultNewTicket:
    sql = "SELECT * FROM tblclients WHERE email = %s"
    access.execute(sql, (x[7],))
    resultUser = access.fetchall()
    for user in resultUser:
        firstName = user[2]
        lastName = user[3]
        phone = user[12].replace('.', '').replace('-', '')
        ticketID = x[1]
        ticketTitle = x[12]
        messageToSend = template_message.invoice_unpaid.format(firstName = firstName,lastName = lastName,phone = phone, ticketID = ticketID, ticketTitle = ticketTitle)
        url = 'http://127.0.0.1:8080/api/send'
        data = {'phone': phone, 'message': messageToSend}
        sendMessage = requests.post(url, json = data)

        print(sendMessage.text)
