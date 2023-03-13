import config
import datetime
import requests
import template_message

currentDate = datetime.datetime.now()
currentDate = currentDate.year

access = config.db.cursor()
access.execute("SELECT * FROM tblinvoices WHERE status = 'Unpaid' AND duedate = CURDATE()")
resultInvoice = access.fetchall()
for x in resultInvoice:
    sql = "SELECT * FROM tblclients WHERE id = %s"
    access.execute(sql, (x[1],))
    resultUser = access.fetchall()
    for user in resultUser:
        firstName = user[2]
        lastName = user[3]
        phone = user[12].replace('.', '').replace('-', '')
        invoiceNumber = x[2]
        if invoiceNumber == "":
            invoiceNumber = x[0]
        messageToSend = template_message.invoice_duedate.format(firstName = firstName,lastName = lastName,phone = phone, invoiceNumber = invoiceNumber, duedate = str(x[4]), duetotal= x[13])
        url = 'http://127.0.0.1:8080/api/send'
        data = {'phone': phone, 'message': messageToSend}
        sendMessage = requests.post(url, json = data)

        print(sendMessage.text)