import time
from datetime import datetime as dt

#host_file =  "hosts"
host_file =  "/etc/hosts"
redirect_ip = "127.0.0.1"

# blocked webpages
web_list = ["facebook.com", "www.facebook.com"]

# extract time "now"
now_yr = dt.now().year
now_mt = dt.now().month
now_dy = dt.now().day
now_hr = dt.now().hour

# weekend or not
weekno = dt.today().weekday()

# unstoppable loop
while True:

    # work hours during work days
    if all([8 < now_hr and now_hr < 16,weekno < 5]):
        print("working hour...")
        with open(host_file, "r+") as file:
            content = file.read()
            for web in web_list:
                if web not in content:
                    file.write(redirect_ip+" "+web+"\n")
    # after work
    else:
        print("after work...")
        with open(host_file,"r+") as file:
            content = file.readlines()
            # must re-set up the pointer position
            file.seek(0)
            for strline in content:
                if not any(web in strline for web in web_list):
                    file.write(strline)
            file.truncate()
    # update every 5 seconds
    time.sleep(5)
