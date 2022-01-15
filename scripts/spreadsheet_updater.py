import gdown
import numpy as np
import yagmail

# download file from Google Drive
url = 'https://drive.google.com/drive/u/0/folders/11TknJKxqUFIsDArJnZMgNmQatJ90IdD0'

output = 'MBTI_500.csv'

gdown.download(url, output, quiet=False)

# read data

# turn data into a list

# connect to Google Sheet
# credentials = GoogleCredentials.get_application_default()
# service = build('sheets', 'v4', credentials=credentials)

# # add list to the sheet
# list = [["valuea1"], ["valuea2"], ["valuea3"]]
# resource = {
#   "majorDimension": "ROWS",
#   "values": list
# }
# spreadsheetId = "### spreadsheet ID"
# range = "Sheet1!A:A";
# service.spreadsheets().values().append(
#   spreadsheetId=spreadsheetId,
#   range=range,
#   body=resource,
#   valueInputOption="USER_ENTERED"
# ).execute()

# # delete file

# # send notification email
# receiver = "your@gmail.com"
# body = "Hello there from Yagmail"
# filename = "document.pdf"

# yag = yagmail.SMTP("my@gmail.com")
# yag.send(
#     to=receiver,
#     subject="Yagmail test with attachment",
#     contents=body, 
#     attachments=filename,
# )