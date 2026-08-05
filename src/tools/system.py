import subprocess
from tools.decorator import tool


class SystemTools:

    @staticmethod
    @tool(
        name="open_notepad",
        description="Open Windows Notepad"
    )
    def open_notepad():
        subprocess.Popen("notepad")

    @staticmethod
    @tool(
        name="open_calculator",
        description="Open Windows Calculator"
    )
    def open_calculator():
        subprocess.Popen("calc")

    @staticmethod
    @tool(
        name="open_vscode",
        description="Open Visual Studio Code"
    )
    def open_vscode():
        subprocess.Popen("code")

    @staticmethod
    @tool(
        name="open_chrome",
        description="Open Google Chrome"
    )
    def open_chrome():
        subprocess.Popen(
            r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        )