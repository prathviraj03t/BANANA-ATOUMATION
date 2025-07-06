from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
from datetime import datetime

# Google Sheet से कनेक्ट (बिना credentials.json के)
gc = gspread.service_account(filename='credentials.json')  # नोट: हटाना है
sheet = gc.open_by_key("17do6PhvW13XdKyyTMPbFd-b5yrZiNabRqNrbJ4PQXbg").sheet1

# YouTube अपलोड फंक्शन (Selenium से)
def upload_video(video_path, title, description):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.youtube.com/upload")
    time.sleep(30)  # 30 सेकंड में मैन्युअल लॉगिन करो
    driver.find_element("xpath", '//input[@type="file"]').send_keys(video_path)
    time.sleep(5)
    driver.find_element("name", "title").send_keys(title)
    driver.find_element("id", "description").send_keys(description)
    driver.find_element("id", "done-button").click()
    driver.quit()

# मुख्य कोड
records = sheet.get_all_records()
now = datetime.now().strftime("%d %b %I%p")  # e.g., "15 Jul 10AM"

for i, row in enumerate(records, start=2):
    if row["Status"] == "Pending" and row["Upload Time"] == now:
        upload_video(row["Video File"], row["Title"], row["Description"])
        sheet.update_cell(i, 4, "Uploaded")  # स्टेटस अपडेट
