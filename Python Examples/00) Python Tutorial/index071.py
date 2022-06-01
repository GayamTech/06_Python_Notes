#   Directive    Description                                Example

#       %a       Weekday, short version                     Wed
#       %A       Weekday, full version                      Wednesday
#       %w       Weekday as a number 0-6, 0 is Sunday       3
#       %d       Day of month 01-31                         31
#       %b       Month name, short version                  Dec
#       %B       Month name, full version                   December
#       %m       Month as a number 01-12                    12
#       %y       Year, short version, without century       18
#       %Y       Year, full version                         2018
#       %H       Hour 00-23                                 17
#       %I       Hour 00-12                                 05
#       %p       AM/PM                                      PM
#       %M       Minute 00-59                               41
#       %S       Second 00-59                               08
#       %f       Microsecond 000000-999999                  548513
#       %z       UTC offset                                 +0100
#       %Z       Timezone                                   CST
#       %j       Day number of year 001-366                 365
#       %U       Week number of year, Sunday as the first day of week, 00-53                                                          52
#       %W       Week number of year, Monday as the first day of week, 00-53                                                          52
#       %c       Local version of date and time    Mon Dec 31 17:41:00 2018
#       %C       Century                                    20
#       %x       Local version of date                      12/31/18
#       %X       Local version of time                      17:41:00






import datetime



print(" ")



x = datetime.datetime.now()

print(x.strftime("%a"))





print(" ")



y = datetime.datetime.now()

print(y.strftime("%A"))




print(" ")


z = datetime.datetime.now()

print(z.strftime("%w"))




print(" ")




a = datetime.datetime.now()

print(a.strftime("%d"))



print(" ")




b = datetime.datetime.now()

print(b.strftime("%b"))






print(" ")



c = datetime.datetime.now()

print(c.strftime("%B"))






print(" ")



d = datetime.datetime.now()

print(d.strftime("%m"))






print(" ")



e = datetime.datetime.now()

print(e.strftime("%y"))







print(" ")



f = datetime.datetime.now()

print(f.strftime("%Y"))






print(" ")



g = datetime.datetime.now()

print(g.strftime("%H"))






print(" ")




h = datetime.datetime.now()

print(h.strftime("%I"))




print(" ")




i = datetime.datetime.now()

print(i.strftime("%p"))






print(" ")


j = datetime.datetime.now()

print(j.strftime("%M"))









print(" ")


k = datetime.datetime.now()

print(k.strftime("%S"))






print(" ")


l = datetime.datetime.now()

print(l.strftime("%f"))






print(" ")


m = datetime.datetime.now()

print(m.strftime("%j"))







print(" ")


n = datetime.datetime.now()

print(n.strftime("%U"))








print(" ")


o = datetime.datetime(2018, 5, 31)

print(o.strftime("%W"))







print(" ")



p = datetime.datetime.now()

print(p.strftime("%c"))









print(" ")

q = datetime.datetime.now()

print(q.strftime("%C"))







print(" ")


r = datetime.datetime.now()

print(r.strftime("%x"))









print(" ")


s = datetime.datetime.now()

print(s.strftime("%X"))



print(" ")