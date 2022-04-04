from time import sleep
import pyautogui as pt
import pyperclip as pc

sleep(2)


def move_to_text_input(message):
    position = pt.locateOnScreen('images//image_icon.png', confidence=.4)
    pt.moveTo(position[0:2], duration=.5)
    pt.moveRel(-100, 20, duration=.5)
    pt.doubleClick(interval=.3)

    pt.typewrite(message, interveral=.01)
    pt.typewrite('\n')


# Handles message retrieval
def get_messages():
    position = pt.locateOnScreen('images/smile_icon.png', confidence=.7)
    pt.moveTo(position[0:2], duration=.5)
    pt.moveRel(50, -50, duration=.5)
    pt.click()

    # click on triple dots
    position = pt.locateOnScreen('images/3_dotimage.png', confidence=.6)
    pt.moveTo(position[0:2], duration=.5)
    pt.click()

