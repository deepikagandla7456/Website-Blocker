# [Website Blocker](https://github.com/deepikagandla7456/Website-Blocker)  
[![GitHub license](https://img.shields.io/github/license/deepikagandla7456/Website-Blocker)](LICENSE) 
[![GitHub issues](https://img.shields.io/github/issues/deepikagandla7456/Website-Blocker)]() 
[![GitHub contributors](https://img.shields.io/github/contributors/deepikagandla7456/Website-Blocker)]() 
[![GitHub last-commit](https://img.shields.io/github/last-commit/deepikagandla7456/Website-Blocker)]()  

<img title="Website Blocker Logo" align='right' src="![Image](https://github.com/user-attachments/assets/ad43d6e0-9e26-4df6-baad-83682fb805e0)" alt="Website Blocker Logo" width="120"/>

Boost your productivity with the **Website Blocker**!  
This simple Python tool helps you block distracting websites like Facebook, Instagram etc., during your focus hours. Whether you're studying, working, or just trying to stay off social media, this tool ensures you stay on track.

---

<p align="center">
Make the most of your time. Stay productive with Website Blocker.
</p>
<p align="center"><i>Block distractions and Unlock focus.</i></p>



---

##  About

Website Blocker is a Python script that helps users avoid distractions by blocking specific websites (e.g., Facebook, Instagram) during a selected time (e.g., 7 AM to 10 AM).  
It works by modifying the system’s `hosts` file to redirect those websites to `127.0.0.1`, making them inaccessible during that period.

---

##  Limitations & Future Work

-  Requires admin/root privileges to edit system files.
-  Only works on local machines (Windows by default).
-  Time range is fixed in code (can be modified manually).

### Future Work

- Add GUI for selecting websites and blocking hours.
- Make cross-platform support for Mac/Linux easier.
- Notification before blocking/unblocking.
- Option to log blocked attempts.

---

##  Features

-  Set specific hours to block websites.
-  Improves focus and productivity.
-  Customizable website list and time range.
-  Automatically unblocks sites after the set time.

---

##  Requirements

- Python 3.x
- OS: Windows (you can change path for Linux/Mac)

---

##  Setup and Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/deepikagandla7456/Website-Blocker.git
   cd Website-Blocker
2. Run the Script
   ```bash
   python app.py
   ```
   Make sure to run it as Administrator on Windows or use ```sudo``` on Mac/Linux.
 ## Usage
- This script continuously checks the system time.

- If current time is between 7 AM and 10 AM, it blocks the sites listed in ```website_list```

- Outside that time range, it unblocks those websites.

- You can change time and sites by editing the values in ```app.py```
## Screenshots 

**Before Blocking the Site**
![Image](https://github.com/user-attachments/assets/56b75d4b-3398-4cc7-951e-3ccff1cd5ec0)
  
***Websites like Facebook and Instagram open normally before the script starts running.***

**During Blocked Hours**
 
***When the script runs between 7 AM and 10 AM, the listed websites are blocked and show an error message when accessed.***

**After Blocked Hours**
![Image](https://github.com/user-attachments/assets/56b75d4b-3398-4cc7-951e-3ccff1cd5ec0)
 
***Once the blocking time ends, the websites are unblocked and accessible again as usual.***

   
## License

This project is licensed under the [Apache License 2.0](LICENSE) - see the [LICENSE](LICENSE) file for details.


