# Nama Depan: {firstName}
# Nama Belakang: {lastName}
# Nomor HP: {phone}
# Nomor Invoice: {invoiceNumber}
# Due Date: {duedate}
# Total Tagihan: {duetotal}
# Tiket ID: {ticketID}
# Tiket title: {ticketTitle}

invoice_unpaid = "Halo, *{firstName} {lastName}* kami informasikan invoice: *{invoiceNumber}* sudah terbit.\n\nUntuk menghindari layanan ter-suspend, silahkan login ke portal https://client.computing.id dan lakukan pembayaran sesuai nominal *Rp. {duetotal}* sebelum tanggal *{duedate}*, atau anda juga bisa melakukan transfer melalui nomor rekening berikut:\n- - - - - - - - - - - - - - - -\nBANK ACCOUNT: 0000000000\n- - - - - - - - - - - - - - - -\n\nJika anda melakukan pembayaran manual diatas, silahkan balas dengan bukti transfer.\n\nTerimakasih" 
invoice_paid = "Halo, *{firstName} {lastName}* kami informasikan invoice: *{invoiceNumber}* sudah LUNAS, \nJika anda memerlukan bantuan teknis silahkan hubungi kami\n\nTerimakasih" 
invoice_duedate = "Halo, *{firstName} {lastName}* kami informasikan invoice: *{invoiceNumber}* sudah terbit dan dalam waktu tenggang.\n\nUntuk menghindari layanan ter-suspend, silahkan login ke portal https://client.computing.id dan lakukan pembayaran sesuai nominal *Rp. {duetotal}* maksimal tanggal *{duedate}*, atau anda juga bisa melakukan transfer melalui nomor rekening berikut:\n- - - - - - - - - - - - - - - -\nBANK ACCOUNT: 0000000000\n- - - - - - - - - - - - - - - -\n\nJika anda melakukan pembayaran manual diatas, silahkan balas dengan bukti transfer.\n\nTerimakasih" 
invoice_comingTerminate = "Halo, *{firstName} {lastName}* kami informasikan invoice: *{invoiceNumber}* status belum terbayar.\n\nUntuk menghindari layanan terminate, silahkan login ke portal https://client.computing.id dan lakukan pembayaran sesuai nominal *Rp. {duetotal}* maksimal tanggal *hari ini*, atau anda juga bisa melakukan transfer melalui nomor rekening berikut:\n- - - - - - - - - - - - - - - -\nBANK ACCOUNT: 0000000000\n- - - - - - - - - - - - - - - -\n\nJika anda melakukan pembayaran manual diatas, silahkan balas dengan bukti transfer.\n\nTerimakasih" 
new_ticket = "Halo, *{firstName} {lastName}* tiket: *{ticketID}* dengan judul *{ticketTitle}* telah kami terima\nKami akan respon secepat mungkin, silahkan cek tiket anda di portal area\n\nTerimakasih" 
reply_ticket = "Halo, *{firstName} {lastName}* tiket: *{ticketID}* dengan judul *{ticketTitle}* telah kami respon\n Silahkan cek update tiket anda di portal area\n\nTerimakasih" 
