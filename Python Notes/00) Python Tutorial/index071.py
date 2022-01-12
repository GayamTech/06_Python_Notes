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



x = datetime.datetime.now()

print(x.strftime("%a"))





y = datetime.datetime.now()

print(y.strftime("%A"))





z = datetime.datetime.now()

print(z.strftime("%w"))







a = datetime.datetime.now()

print(a.strftime("%d"))






b = datetime.datetime.now()

print(b.strftime("%b"))








c = datetime.datetime.now()

print(c.strftime("%B"))








d = datetime.datetime.now()

print(d.strftime("%m"))








e = datetime.datetime.now()

print(e.strftime("%y"))









f = datetime.datetime.now()

print(f.strftime("%Y"))








g = datetime.datetime.now()

print(g.strftime("%H"))









h = datetime.datetime.now()

print(h.strftime("%I"))







i = datetime.datetime.now()

print(i.strftime("%p"))








j = datetime.datetime.now()

print(j.strftime("%M"))











k = datetime.datetime.now()

print(k.strftime("%S"))








l = datetime.datetime.now()

print(l.strftime("%f"))








m = datetime.datetime.now()

print(m.strftime("%j"))









n = datetime.datetime.now()

print(n.strftime("%U"))










o = datetime.datetime(2018, 5, 31)

print(o.strftime("%W"))










p = datetime.datetime.now()

print(p.strftime("%c"))










q = datetime.datetime.now()

print(q.strftime("%C"))









r = datetime.datetime.now()

print(r.strftime("%x"))











s = datetime.datetime.now()

print(s.strftime("%X"))
