import pandas as pd
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow,Flow
from google.auth.transport.requests import Request
import os
import pickle

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# here enter the id of your google sheet
SAMPLE_SPREADSHEET_ID_input = '1-zITMvUdiRHBYY8s80aZH8MIM0OHAivyiOYUhL238Uw'
SAMPLE_RANGE_NAME = 'Reservation!A1:H100'

# https://docs.google.com/spreadsheets/d/1-zITMvUdiRHBYY8s80aZH8MIM0OHAivyiOYUhL238Uw/edit#gid=2103965431


def main():
    global values_input, service
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)  # here enter the name of your downloaded JSON file
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result_input = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID_input, range=SAMPLE_RANGE_NAME, valueRenderOption='FORMULA').execute()
    values_input = result_input.get('values', [])
    # print(values_input[0])
    df = pd.DataFrame(values_input[1:])
    for i,j in df[2].iteritems():
        print(i, j)
main()

# df = pd.DataFrame(values_input[1:], columns=values_input[0])
# df = pd.DataFrame(result_input)
# print(df)