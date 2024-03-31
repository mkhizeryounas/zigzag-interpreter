from zigzag.computer import Computer
from time import sleep


def main():
    computer = Computer()
    # display.point_to_text("mouse")
    proc = computer.terminal.start_subprocess("slack")
    sleep(0.5)
    computer.keyboard.perform_action(
        [
            "esc",
            "esc",
        ]
    )
    sleep(0.5)
    computer.keyboard.perform_action(["command", "k"])
    sleep(0.5)
    computer.keyboard.type_text("Khizer (Android)")
    sleep(0.5)
    computer.keyboard.perform_action(["enter"])
    sleep(0.5)
    computer.display.point_to_text(f"Message Khizer (Android)")
    sleep(0.5)
    # computer.mouse.click()
    # sleep(0.5)
    computer.keyboard.type_text("Hello! I am a bot. How can I help you?")
    sleep(0.5)
    computer.keyboard.perform_action(["enter"])
    sleep(0.5)
    # computer.terminal.close_subprocess(proc)
    print("Done")
