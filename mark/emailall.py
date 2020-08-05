#!/usr/bin/env python
# email everyone in the csv
# their marks - this depends on the exact format of the csv file!
# KM 2013,16
import smtplib
import time
From = "km@ecs.soton.ac.uk"
Date = time.ctime(time.time())
Subject = "comp2207 coursework marks"


# INSERT the code from filereader in here
# but modify the To if its not the first field
##########################################

for line in file("all2207.csv"):
    fields = line.split(',')
    To = fields[0] + "@ecs.soton.ac.uk"
    msg = "your comp2207 coursework1 marks are: (A B C total/10) \n" + line
    msg += "\nThese are subject to possible moderation but likely to remain the same \n"
    msg += "\it was an interesting read!\n Kirk \n"
    print msg
###########################################
    mMessage = ('From: %s\nTo: %s\nDate: %s\nSubject: %s\n%s\n' % (From, To, Date, Subject, msg))

    print 'connecting to server'
    s = smtplib.SMTP('smtp.ecs.soton.ac.uk')

    rCode = s.sendmail(From, To, mMessage)

    s.quit()

    if rCode:
        print '-----error sending email to ' + To
    else:
        print '-----email sent ok to ' + To
