import tkinter as tk
from tkinter import messagebox
import time
import random
import threading

REMINDER_INTERVAL_MINUTES = 30

STRETCH_TIPS = [
    "Roll your shoulders backward 10 times, then forward 10 times.",
    "Stand up and do 10 slow neck rolls — left and right.",
    "Reach both arms above your head and hold for 15 seconds.",
    "Do 10 standing calf raises to get your blood flowing.",
    "Walk around for 2 minutes — even just around your room!",
    "Stretch your wrists: extend each arm and gently pull your fingers back.",
    "Do a gentle chest opener: clasp hands behind your back and squeeze.",
    "Sit up straight, take 5 deep breaths, and reset your posture.",
    "Stand and touch your toes (or try!) — hold for 10 seconds.",
    "Do 5 slow squats to activate your legs and lower back.",
]

def show_reminder():
    tip = random.choice(STRETCH_TIPS)
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    root.attributes("-topmost", True)  # Bring to front
    messagebox.showinfo(
        title="⏰ Time to Stretch!",
        message=f"You've been sitting for {REMINDER_INTERVAL_MINUTES} minutes.\n\n"
                f"💪 Stretch Tip:\n{tip}\n\n"
                f"Take a 2-minute break — your body will thank you!"
    )
    root.destroy()

def reminder_loop():
    print(f"Stretch Reminder is running!")
    print(f"You will be reminded every {REMINDER_INTERVAL_MINUTES} minutes.")
    print("Keep this terminal open. Press Ctrl+C to stop.\n")

    while True:
        time.sleep(REMINDER_INTERVAL_MINUTES * 60)
        # Run popup in main thread via threading event
        show_reminder()

if __name__ == "__main__":
    # Run the reminder loop in a background thread
    reminder_thread = threading.Thread(target=reminder_loop, daemon=True)
    reminder_thread.start()

    # Keep the main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStretch Reminder stopped. Stay healthy, Mozahid! 💪")
