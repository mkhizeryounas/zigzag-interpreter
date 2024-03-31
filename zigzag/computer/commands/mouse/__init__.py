import pyautogui


class Mouse:
    def __init__(self, computer):
        self.computer = computer

    def move(self, x, y):
        screenWidth, screenHeight = pyautogui.size()
        x = max(0, min(x * screenWidth, screenWidth))
        y = max(0, min(y * screenHeight, screenHeight))
        pyautogui.moveTo(x, y, duration=0.25)

    def click(self):
        pyautogui.click()

    def double_click(self):
        pyautogui.doubleClick()

    def right_click(self):
        pyautogui.rightClick()
