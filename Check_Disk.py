#-------------------------------------------------------------------------------
# Name:        check_disk_c
# Purpose:
#
# Author:      alberto.frosi
#
# Created:     10/12/2014
# Copyright:   (c) alberto.frosi 2014
# Licence:    Use of this source code is governed by a BSD-style
#-------------------------------------------------------------------------------
#!/usr/bin/env python



import sys
import os
import psutil
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import socket
import time

def main():


    while True:
        psutil.disk_partitions(all=False)
        templ = "%5s%%"
        usage = psutil.disk_usage('C:\\')
        print(templ %(int(usage.percent)))
        if usage.percent > 94:

            sender = 'admin_psutil@fisvi.com'
            receivers = 'alberto.frosi@fisvi.com'

            msg = MIMEMultipart()
            msg['From'] = 'admin_psutil@fisvi.com'
            msg['To'] = 'alberto.frosi@fisvi.com'
            msg['Subject'] = 'Check space Disk C:\ for %s' %socket.gethostname()
            message = 'Attenzione spazio su disco C:\ insufficiente %s'%(templ%(usage.percent))
            msg.attach(MIMEText(message))
            try:
                smtpObj = smtplib.SMTP('fismail.fisvi.it',25)
                smtpObj.sendmail(sender, receivers, msg.as_string())
                print ("Successfully sent email")
                print(socket.gethostname())
            except SMTPException:
                print("Error: unable to send email")
        time.sleep(300)
        continue

if __name__ == '__main__':
    sys.exit(main())

