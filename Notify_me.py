import os
from plyer import notification
from os import getcwd

def Alert(Text):
    icon_path = os.path.join(getcwd(), "file (3).png")

    # Correcting potential typo in the notification message
    corrected_text = Text.replace("ths", "this")

    notification.notify(
        title="Time Management Assistant Ai",
        message=corrected_text,
        app_icon=icon_path,
        timeout=10  # duration in seconds
    )