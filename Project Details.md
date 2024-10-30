# Website Blocker

## Project Overview
A Python-based website blocker application that restricts access to distracting websites during specified time periods, helping users maintain focus and improve productivity.

## Problem Statement
The project aims to develop a website blocker to prevent access to certain websites during chosen hours, enhancing time management and reducing distractions.

## Abstract
This project uses Python to build a user-friendly website blocking tool. With features like time-based blocking and background operation, this tool helps individuals limit their online distractions effectively.

## Prerequisites and Technology Used
- Code editor (e.g., Notepad, VS Code)
- Python (with necessary packages installed)
- Basic networking knowledge
- Browser

## Workflow
The application runs in the background and checks the current time against specified blocking hours. If the time falls within the blocking period, access to specified websites is restricted.

## Source Code
```python
import time
from datetime import datetime as dt

host_path = "C:\\Windows\\System32\\drivers\\etc\\hosts"  # Adjust path for Mac/Linux if needed
redirect = "127.0.0.1"
website_list = ["facebook.com", "www.facebook.com"]

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
```
Pros:
-Improves focus by blocking distracting sites.
-Increases productivity by reducing online interruptions.
-Helps develop self-discipline by limiting unnecessary browsing.

Cons:
-Requires manual updating to block new websites.
-Only works on the system where it’s implemented.

Conclusion
The Website Blocker is a useful Python tool for users looking to minimize online distractions. While it has limitations, it provides a basic framework for managing web access effectively.
