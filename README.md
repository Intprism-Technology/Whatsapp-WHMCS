# Introduction
## Features
- [OK] API Kirim Pesan ke Nomor
- [OK] Auto Response / BOT
- [OK] WHMCS Billing Alert
    - Invoice Terbit
    - Invoice Paid
    - Invoice DueDate
    - Last Notification 1day Before Terminate

# Requirements
- NodeJS V18
- Python V3
- Pip Python

# Install
- Install NodeJS 
    ```
    https://nodejs.org/en/download/
    ```
- Install Python3 PIP & dependency (Ubuntu)
    ```
    apt install python3-pip
    pip install mysql-connector-python
    ```
- Clone repository and Install Library
    ```
    git clone git@github.com:Intprism-Technology/Whatsapp-WHMCS.git
    cd Whatsapp-WHMCS
    npm install
    ```
- Konfigurasi DB MySQL
    ```
    nano whmcs/config.py
    ```
    edit baris berikut
    ```
    host_db = ''
    name_db = ''
    user_db = ''
    pass_db = ''
    ```
- Konfigurasi template pesan notifikasi WHMCS
    ```
    nano whmcs/template_message.py
    ```
    template variabel
    ```
    # Nama Depan: {firstName}
    # Nama Belakang: {lastName}
    # Nomor HP: {phone}
    # Nomor Invoice: {invoiceNumber}
    # Due Date: {duedate}
    # Total Tagihan: {duetotal}

    invoice_unpaid = "Halo, *{firstName} {lastName}*"
    invoice_paid = "Halo, *{firstName} {lastName}*"
    invoice_duedate = "Halo, *{firstName} {lastName}*"
    invoice_comingTerminate = "Halo, *{firstName} {lastName}*"
    ```
- Login Whatsapp
    sebagai contoh, instalasi di path /var/www/Whatsapp-WHMCS
    ```
    /usr/local/bin/node /var/www/Whatsapp-WHMCS/index.js
    ```
    - scan qr hingga muncul success pairing
    - exit program / CTRL + C
# Run Service
- Whatsapp BOT & API
    - edit cron
    ```
    @reboot sleep 5 && /usr/local/bin/node /var/www/Whatsapp-WHMCS/index.js &
    ```
    - jalankan service ulang 
    ```
    /usr/local/bin/node /var/www/Whatsapp-WHMCS/index.js &
    ```
- Service Kirim Invoice WHMCS Notifikasi (tiap hari, jam 8 pagi) dan notifikasi invoice paid (tiap 5menit)
    ```
    */5 * * * * cd /var/www/Whatsapp-WHMCS/whmcs && /usr/bin/python3 invoice_paid.py
    0 8 * * * cd /var/www/Whatsapp-WHMCS/whmcs && /usr/bin/python3 invoice_unpaid.py
    0 8 * * * cd /var/www/Whatsapp-WHMCS/whmcs && /usr/bin/python3 invoice_duedate.py
    0 8 * * * cd /var/www/Whatsapp-WHMCS/whmcs && /usr/bin/python3 invoice_comingTerminate.py
    ```
# Endpoint
- API Endpoint
    ```
    <ip>:8080/api/send
    ```
    Type: POST

    Variable:
    ```
    phone (required)
    message (required)
    ```
# Request Update
Warga Diskusiwebhosting bisa request langsung melalui thread ))

    https://www.diskusiwebhosting.com/threads/whatsapp-api-dan-notifikasi-whmcs.38061/


# Support
- - - - - - - - - - - - - - - -
BCA : 3151176150

BCA Digital: 001339859866

Jago : 506512637291

Paypal: info@intprism.com
- - - - - - - - - - - - - - - -
