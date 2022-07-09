from __future__ import print_function
import gdown
import pandas as pd
import yagmail
import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]


def main():
    # download file from Google Drive
    url = "https://drive.google.com/uc?id=1NKRKSa5rceRJDgKFvaaEa5RM9sE-osJc"

    output = "MBTI_500.csv"

    if not os.path.exists("MBTI_500.csv"):
        gdown.download(url, output, quiet=False)

    # read data
    csv_df = pd.read_csv("MBTI_500.csv")
    csv_list = csv_df.to_numpy().tolist()
    cleaned_csv_list = [x for x in csv_list if str(x) != "nan"]

    # send data to Google Sheet
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("sheets", "v4", credentials=creds)

        body = {"values": cleaned_csv_list}

        result = (
            service.spreadsheets()
            .values()
            .update(
                spreadsheetId="1ncW3izSMqBbECbOJkXoDpEwLc1bbZAQmjXCTBhPRDu8",
                range="Sheet1",
                valueInputOption="RAW",
                body=body,
            )
            .execute()
        )

        print("{0} cells updated.".format(result.get("updatedCells")))
    except HttpError as err:
        print(err)

    # send notification email
    receiver = "test@gmail.com"
    body = "Check out the updated spreadsheet and let me know what you think."

    yag = yagmail.SMTP("my@gmail.com")
    yag.send(to=receiver, subject="That spreadsheet has been updated", contents=body)

    # delete file
    if os.path.exists("MBTI_500.csv"):
        os.remove("MBTI_500.csv")
    else:
        print("The downloaded file does not exist")


if __name__ == "__main__":
    main()
