# There are a number of modules for accessing the internet and processing internet protocols. 
# Two of the simplest are urllib.request for retrieving data from URLs and smtplib for sending mail 

from urllib.request import urlopen
with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
     for line in response:
         line = line.decode('utf-8')         # Decoding the binary data to text
         if 'EST' in line or 'EDT' in line:  # look for Eastern Time
             print(line)


print()
# Note that this example needs a mailserver running on localhost, for example Fake SMTP Server
import smtplib
server = smtplib.SMTP('localhost:2525')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
    """To: jcaesar@example.org
    From: soothsayer@example.org
    
    Beware the Ides of March.
    """)
server.quit()


print()
# Dates are easily constructed and formatted
from datetime import date
now = date.today()
print("Now: ", now)
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

# dates support calendar arithmetic
birthday = date(1986, 6, 30)
age = now - birthday
print(age.days)
