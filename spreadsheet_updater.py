from __future__ import print_function
import pyautogui
import pandas as pd


def main():
    # go to finder
    pyautogui.click(450, 1150)

    # click Examples folder in sidebar
    pyautogui.click(650, 780)

    # double click MBTI_500.csv
    pyautogui.doubleClick(800, 680)

    # highlight the first 20 entries
    pyautogui.click(415, 180)
    pyautogui.dragTo(415, 505, button='left')

    # right-click and copy the entries
    # open Chrome browser
    # click on bookmark for Google Sheets
    # click blank spreadsheet
    # click in the title
    # type a title based on the current data
    # right-click in the first cell
    # paste the data
    # click the Chrome close button
    url = "https://drive.google.com/uc?id=1NKRKSa5rceRJDgKFvaaEa5RM9sE-osJc"


if __name__ == "__main__":
    main()
