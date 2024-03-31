import pyautogui


class Keyboard:
    def __init__(self, computer):
        self.computer = computer

    def perform_action(self, keys):
        special_keys = ["ctrl", "command", "shift", "alt"]
        for key in keys:
            if key in special_keys:
                pyautogui.keyDown(key)
            else:
                pyautogui.press(key)

        # Release modifier keys
        for key in keys:
            if key in special_keys:
                pyautogui.keyUp(key)

    def type_text(self, text):
        pyautogui.typewrite(text)
