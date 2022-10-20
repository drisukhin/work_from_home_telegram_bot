import os
import datetime
from creds import credentials
from datetime import date
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from creds.items import Items

class SaveDates:

    @staticmethod
    def dates_saver(telegram_message):
        today = date.today()
        d3 = today.strftime("%B")
        d4 = today.strftime("%Y")

        day = (telegram_message[0:2])
        month = (telegram_message[2:4])
        year = (telegram_message[4:8])

        mess = str(day + "." + month + "." + year)

        with open(Items.FILE_REPORT_PATH % (d3 + d4), 'a', encoding="utf-8") as file:
            file.write('\n')
            for line in mess:
                file.write(line)
            file.close()

        day = (telegram_message[0:2])
        month = (telegram_message[2:4])
        year = (telegram_message[4:8])

        YEAR = year
        MONTH = month
        DAY = day

        """Shows basic usage of the Google Calendar API.
        Prints the start and name of the next 10 events on the user's calendar.
        """
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('creds/token.json'):
            creds = Credentials.from_authorized_user_file('creds/token.json', credentials.SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('creds/client_secret_139324555620.com.json',credentials.SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('creds/token.json', 'w') as token:
                token.write(creds.to_json())

        try:
            service = build('calendar', 'v3', credentials=creds)

            # Call the Calendar API
            now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
            print('Getting the upcoming 10 events')
            events_result = service.events().list(calendarId=Items.EMAIL_DMITRIY, timeMin=now,
                                                  maxResults=10, singleEvents=True,
                                                  orderBy='startTime').execute()
            events = events_result.get('items', [])

            event_day = {
                'summary': 'Dmitriy Work From Home',
                'start': {
                    'dateTime': '%s-%s-%sT08:00:00' % (YEAR, MONTH, DAY),
                    'timeZone': 'Asia/Jerusalem',
                },
                'end': {
                    'dateTime': '%s-%s-%sT18:00:00' % (YEAR, MONTH, DAY),
                    'timeZone': 'Asia/Jerusalem',
                },
                'attendees': [
                    # {'email': Items.EMAIL_MARK},
                    # {'email': Items.EMAIL_ANNA},
                    # {'email': Items.EMAIL_YULIYA},
                    # {"email": Items.EMAIL_DARIA},
                    # {"email": Items.EMAIL_AVSHALOM}
                ]
            }

            event = service.events().insert(calendarId=Items.EMAIL_DMITRIY, body=event_day,
                                            sendNotifications=True).execute()

        except:
            assert False