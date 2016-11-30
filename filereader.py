#!/usr/bin/env python
# test parsing to just print it all
for line in file("all2207.csv"):
    fields = line.split(',')
    To = fields[0] + "@ecs.soton.ac.uk"
    msg = "your comp2207 coursework1 marks are: (A B C total/10) \n" + line
    msg += "\nThese are subject to possible moderation but likely to remain the same \n"
    print To
    print msg
