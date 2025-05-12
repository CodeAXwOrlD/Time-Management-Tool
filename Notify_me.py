import os
from plyer import notification
from os import getcwd

def Alert(Text):
    icon_path = os.path.join(getcwd(), "file (3).png")

    notification.notify(
        title="Time Management Assistant Ai",
        message=Text,
        app_icon=icon_path,
        timeout=10  # duration in seconds
    )