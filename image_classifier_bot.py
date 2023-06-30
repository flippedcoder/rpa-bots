import pyautogui

def main():
    # open Chrome browser
    pyautogui.click(740, 1250)

    # click on bookmark for Cloudinary
    pyautogui.click(330, 115)

    # open the folder with the unlabeled images
    pyautogui.moveTo(450, 455)

    # right-click the image
    pyautogui.rightClick()

    # click the download option
    pyautogui.click()

    # click the original option
    pyautogui.click()

    # click Example_Data folder in download pop-up
    pyautogui.click()

    # Re-name image
    pyautogui.click()
    pyautogui.write('unlabeled_image')

    # click Save in download pop-up
    pyautogui.click()

    # open Terminal
    pyautogui.click()

    # type cd Example_Data
    pyautogui.write('cd Example_Data')

    # press enter
    pyautogui.press()

    # type command to run ML script
    pyautogui.write('python ../Repos/rpa-bots/classify_image.py')

    # press enter
    pyautogui.press()

    # get the image classification from the terminal
    pyautogui.doubleClick()
    pyautogui.hotkey('command', 'c')

    # click in the Example_Data folder
    pyautogui.click()

    # click the image
    pyautogui.click()

    # press enter
    pyautogui.press()

    # rename the image to the classification
    pyautogui.write()

    # click on Chrome
    pyautogui.click()

    # click on cloudinary tab
    pyautogui.click()

    # click the checkmark on the first image
    pyautogui.click()

    # navigate to the delete button
    pyautogui.click()

    # click delete
    pyautogui.click()
    
    # click delete in the confirmation modal
    pyautogui.click()

if __name__ == "__main__":
    main()
