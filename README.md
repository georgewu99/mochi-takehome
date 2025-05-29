# mochi-takehome
Github repo for Mochi take home assignment

Mood of the Queue app:
This app takes in user input (dropdown for mood, text for comment) and stores it along with timestamp in a connected Google sheet. It then visualizes the day's mood trend in a bar chart.

Link to gsheet: 
- https://docs.google.com/spreadsheets/d/1acBjau_dhsdjqS8DmY7JGhksRjqwmYsLvZud33RKMU8/edit?usp=sharing

My credentials.json file is in .gitignore

Below are some of the resources I utilized: 
- https://docs.gspread.org/en/v6.1.4/user-guide.html#getting-all-values-from-a-row-or-a-column
- https://discuss.streamlit.io/t/inserting-data-via-streamlit-form-to-google-sheets/38149/13
- https://docs.streamlit.io/develop/api-reference/widgets
- https://docs.streamlit.io/develop/tutorials/databases/public-gsheet
- https://docs.streamlit.io/develop/api-reference/charts/st.pyplot
- https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html


I used google-auth instead of oauth2client since the latter is deprecated:
- https://pypi.org/project/oauth2client/

Let me know if you encounter any issues with accessing the sheet, running the script, and/or the APIs and connection to the sheet. I know it can be really finnicky getting all the connectors and authorizations established 
