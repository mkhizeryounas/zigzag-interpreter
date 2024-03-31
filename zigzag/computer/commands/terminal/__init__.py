from time import sleep
import subprocess
import psutil


class Terminal:
    def __init__(self, computer):
        self.computer = computer

    def start_subprocess(self, app_name, wait_time=3, timeout=60):
        # Open the app
        proc = subprocess.call(["open", "-a", app_name])

        # Check if the app is running
        for _ in range(timeout):
            for proc in psutil.process_iter():
                proc_name = proc.name()
                if app_name.lower() in proc_name.lower():
                    sleep(wait_time)
                    print(f"{proc_name} is ready!")
                    return proc
        print(f"Timeout: {app_name} did not start within {timeout} seconds.")

    def close_subprocess(self, proc):
        proc.terminate()
        print(f"Process {proc.name()} terminated.")
