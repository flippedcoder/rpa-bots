import datetime
import pyautogui
import pandas as pd

def main():
    # open pdf
    pyautogui.click(610, 1250)

    # click in pdf
    pyautogui.click(355, 320)

    # get the fields
    pyautogui.doubleClick(355, 320)
    pyautogui.dragTo(550, 505, button='left')
    
    # press Cmd + C and copy the name
    pyautogui.hotkey('command', 'c')

    # open Chrome browser
    pyautogui.click(740, 1250)

    # click on bookmark for Google Sheets
    pyautogui.click(310, 115)
    
    # click in the title
    pyautogui.click(180, 155)
    pyautogui.click(180, 155)

    # type a title based on the current data
    pyautogui.write(f'Employee data: {datetime.datetime.now().strftime("%c")}')
    
    # click in the first cell
    pyautogui.click(110, 310)
    
    # press Cmd + V and paste the entries
    pyautogui.hotkey('command', 'v')

    # click on Slack
    pyautogui.click(780, 1250)

    # click on the channel
    pyautogui.moveTo(740, 1250)
    
    # # click in the message input
    # pyautogui.moveTo(740, 1250)

    # # type that the data has moved
    # pyautogui.write('The spreadsheet has been updated so the team should take a look.')

    # # click the send button
    # pyautogui.moveTo(740, 1250)

if __name__ == "__main__":
    main()