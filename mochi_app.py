import streamlit as st
st.write('App starting')

from streamlit_gsheets import GSheetsConnection
import datetime as dt
from datetime import datetime
import time
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
import matplotlib.pyplot as plt

st.write('imports good')



# Connect to Google Sheets
# conn = st.connection("gsheets", type=GSheetsConnection)

# Read existing data
# existing_data = conn.read(worksheet="Sheet1")


with st.form("my_form"):
    st.title("Mood of the Queue")
    st.write("This app is running from a .py file.")

    ## User selects a mood from the dropdown 
    mood_list = ['Extremely happy', 'Happy', 'So-so', 'Frustrated', 'Extremely frustrated']
    mood_choice = st.selectbox(
        "What is your current mood?",
        mood_list
    )

    ## User can add a short note 
    mood_comment = st.text_input("Add a comment - let us know the reasons behind your current mood. Or type N/A for no comment")


    submitted = st.form_submit_button("Submit")

    ## Upon submit, leverage gsheets API to append to connected gsheet. Then generate the chart showing mood counts for today 
    if submitted:

        ## Grab submission timestamp and convert to string bc json doesnt like datetime
        timestamp_datetime = dt.datetime.now()
        timestamp_datetime = timestamp_datetime.strftime('%Y-%m-%d %X')



        ## create row with mood, comment, and timestamp to be uploaded to sheet 
        new_row = [mood_choice, mood_comment, timestamp_datetime]



        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = Credentials.from_service_account_file('credentials.json', scopes = scope)
        client = gspread.authorize(creds)
        
        sh = client.open('MoodEntryLog').worksheet('Log')  
        sh.append_row(new_row)


        st.success("Your feedback has been submitted - thank you!")

        
        
        st.write("Today's mood chart:")

        ## Grab all of the entries from the sheet, then convert to df 
        entries = sh.get_all_records()
        df = pd.DataFrame(entries)


        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        today = datetime.now().date()

        ## distribution of mood entries, filter for today 
        mood_dist = df.loc[df['Timestamp'].dt.date == today]['Mood'].value_counts()


        fig, ax = plt.subplots()
        mood_dist.plot(kind='bar')
        ax.set_xlabel("Mood")
        ax.set_ylabel("Counts")
        ax.set_title("Today's moods")

        st.pyplot(fig)
                


