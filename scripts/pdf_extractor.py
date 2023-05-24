import pandas as pd

# open pdf
# get the fields
# open Chrome browser
# click on bookmark for Google Sheets
# click blank spreadsheet
# click in the title
# type a title based on the current data
# right-click in the first cell
# paste the data
# click the Chrome close button
# click on Slack
# click on the channel
# click in the message input
# type that the data has moved
# click the send button

data = pd.DataFrame.from_dict(report)

data.to_csv("final.csv", index=False)
