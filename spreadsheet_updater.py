from __future__ import print_function
import datetime
import pyautogui


def main():
    # go to finder
    pyautogui.click(600, 1250)

    # click Examples folder in sidebar
    pyautogui.click(720, 490)

    # double click MBTI_500.csv
    pyautogui.click(x=850, y=450)
    pyautogui.doubleClick(x=820, y=350)

    # highlight the first 20 entries
    pyautogui.doubleClick(470, 201)
    pyautogui.dragTo(550, 505, button='left')

    # press Cmd + C and copy the entries
    pyautogui.hotkey('command', 'c')

    # open Chrome browser
    pyautogui.click(740, 1250)

    # click on bookmark for Google Sheets
    pyautogui.click(310, 115)

    # click in the title
    pyautogui.click(180, 155)

    # type a title based on the current data
    pyautogui.write(f'Employee data: {datetime.datetime.now().strftime("%c")}')

    # click in the first cell
    pyautogui.click(110, 310)

    # press Cmd + V and paste the entries
    pyautogui.hotkey('command', 'v')

if __name__ == "__main__":
    main()
