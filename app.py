import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheet से कनेक्ट (सिर्फ पढ़ने के लिए)
scope = ["https://spreadsheets.google.com/feeds"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
gc = gspread.authorize(creds)

# शीट ओपन करो
sheet = gc.open("YouTube_Videos").sheet1

# डैशबोर्ड
st.title("📊 YouTube Upload Status")
st.write("### Pending Videos")
pending_videos = [row for row in sheet.get_all_records() if row["Status"] == "Pending"]
st.table(pending_videos)

st.write("### Uploaded Videos")
uploaded_videos = [row for row in sheet.get_all_records() if row["Status"] == "Uploaded"]
st.table(uploaded_videos)
