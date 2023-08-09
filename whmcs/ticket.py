import config
import datetime
import requests
import template_message

# New Ticket
access = config.db.cursor()
access.execute("SELECT * FROM tbltickets WHERE date >= date_sub(now(), interval 5 minute); ")
resultNewTicket = access.fetchall()
for x in resultNewTicket:
    sql = "SELECT * FROM tblclients WHERE id = %s"
    access.execute(sql, (x[3],))
    resultUser = access.fetchall()
    for user in resultUser:
        firstName = user[2]
        lastName = user[3]
        phone = user[12].replace('.', '').replace('-', '')
        ticketID = x[1]
        ticketTitle = x[12]
        messageToSend = template_message.new_ticket.format(firstName = firstName,lastName = lastName,phone = phone, ticketID = ticketID, ticketTitle = ticketTitle)
        url = 'http://127.0.0.1:8080/api/send'
        data = {'phone': phone, 'message': messageToSend}
        sendMessage = requests.post(url, json = data)

        print(sendMessage.text)

# Reply ticket
access = config.db.cursor()
access.execute("SELECT * FROM `tblticketreplies` WHERE admin != '' AND date >= date_sub(now(), interval 5 minute)")
resultReplyTicket = access.fetchall()
for x in resultReplyTicket:
    #get ticket by id
    sql = "SELECT * FROM tbltickets WHERE id = %s"
    access.execute(sql, (x[1],))
    getTicket = access.fetchall()
    #getUser by ticket
    sql = "SELECT * FROM tblclients WHERE id = %s"
    access.execute(sql, (getTicket[0][3],))
    resultUser = access.fetchall()
    for user in resultUser:
        firstName = user[2]
        lastName = user[3]
        phone = user[12].replace('.', '').replace('-', '')
        #get ticket id
        messageToSend = template_message.reply_ticket.format(firstName = firstName,lastName = lastName,phone = phone, ticketID = getTicket[0][1], ticketTitle = getTicket[0][12])
        url = 'http://127.0.0.1:8080/api/send'
        data = {'phone': phone, 'message': messageToSend}
        sendMessage = requests.post(url, json = data)

        print(sendMessage.text)
