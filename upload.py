from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# 1. Chrome सेटअप (हेडलेस मोड)
options = Options()
options.add_argument("--headless")  # बिना GUI के चलेगा
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=options)

# 2. YouTube पर जाओ और मैन्युअल लॉगिन का इंतज़ार करो
print("⚠️ 5 मिनट का टाइम है लॉगिन करने के लिए!")
driver.get("https://accounts.google.com")
time.sleep(300)  # 5 मिनट (इस दौरान मैन्युअल लॉगिन करो)

# 3. वीडियो अपलोड करो
driver.get("https://youtube.com/upload")
driver.find_element("xpath", '//input[@type="file"]').send_keys("video.mp4")
print("🎥 वीडियो अपलोड हो गया!")
time.sleep(10)  # अपलोड पूरा होने का इंतज़ार
driver.quit()
