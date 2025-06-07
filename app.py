import time
from datetime import datetime as dt

host_path = "C:\\Windows\\System32\\drivers\\etc\\hosts"  # Adjust path for Mac/Linux if needed
redirect = "127.0.0.1"
website_list = ["facebook.com", "www.facebook.com", "instagram.com", "www.instagram.com"]

while True:
    # Set blocking hours (e.g., 7 AM to 10 AM)
    if dt(dt.now().year, dt.now().month, dt.now().day, 7) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 10):
        with open(host_path, "r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
        print("All listed websites are blocked!")
    else:
        with open(host_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Websites are unblocked! Have fun!")
    time.sleep(5)
