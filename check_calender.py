import os.path
from datetime import datetime, timedelta, timezone

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# uv pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
# <= install the google calendar API

# Specify the requested API permissions
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]


def google_calender():
    creds = None

    # User has to login if it has no valid authentication.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    service = build("calendar", "v3", credentials=creds)
    return service


# Call the calendar API
def get_study_subjects():
    try:
        service = google_calender()

        # Japan timezone
        JST = timezone(timedelta(hours=9))

        now_jst = datetime.now(JST)

        today_start_jst = now_jst.replace(
            hour=0,
            minute=0,
            second=0,
            microsecond=0
        )

        today_end_jst = now_jst.replace(
            hour=23,
            minute=59,
            second=59,
            microsecond=999999
        )

        time_min = today_start_jst.isoformat()
        time_max = today_end_jst.isoformat()

        event_result = service.events().list(
            calendarId="primary",
            timeMin=time_min,
            timeMax=time_max,
            singleEvents=True,
            orderBy="startTime"
        ).execute()

        events = event_result.get("items", [])

        subjects = []

        for event in events:
            title = event.get("summary", "")

            # Get only events whose title starts with "Study:"
            if title.lower().startswith("study:"):
                subject = title.split(":", 1)[1].strip()

                if subject:
                    subjects.append(subject)

        return subjects

    except HttpError as error:
        print(f"Google Calendar API Error: {error}")
        return []

    except Exception as error:
        print(f"Error: {error}")
        return []


# if __name__ == "__main__":
#     subjects = get_study_subjects()

#     for subject in subjects:
#         print(subject)