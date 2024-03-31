from zigzag.computer.commands.display import Display
from zigzag.computer.commands.keyboard import Keyboard
from zigzag.computer.commands.terminal import Terminal
from zigzag.computer.commands.mouse import Mouse


class Computer:
    def __init__(self):
        self.display = Display(self)
        self.keyboard = Keyboard(self)
        self.terminal = Terminal(self)
        self.mouse = Mouse(self)

        self.oi_base_url = "https://api.openinterpreter.com/v0"
