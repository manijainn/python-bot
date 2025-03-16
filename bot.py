from dotenv import load_dotenv
import os
import pyautogui
import time
import pyperclip
from openai import OpenAI

load_dotenv()

openaiapikey = os.getenv('OPENAIAPIKEY')

def is_last_message_from_sender(chat_log,sender_name = "naruto"):
    messages = chat_log.strip().split("/2025] ")
    print(messages)

    if sender_name in messages:
        return True
    return False
    # for message in reversed(messages):
    #     parts = message.split(": ", 2)

    #     if len(parts) >= 3:
    #         timestamp, sender, content = parts

    #         if sender.strip() == sender_name:
    #             return True
    #         else:
    #             return False
    
    # return False

# Small delay to switch windows before execution
time.sleep(3)

# Step 1: Click on the icon
pyautogui.click(1180, 1052) # browser
time.sleep(2)  # Wait for the window to open

while True:
    # Step 2: Click and drag to select text
    pyautogui.moveTo(1818, 203)    
    pyautogui.mouseDown()
    pyautogui.moveTo(760, 901, duration=1)  # Smooth drag
    pyautogui.mouseUp()

    # Step 3: Copy to clipboard
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(699, 198)
    time.sleep(2)  # Wait for the text to copy

    # Step 4: Retrieve copied text
    chat_history = pyperclip.paste()
    print("Copied Text:", chat_history)

    if(is_last_message_from_sender(chat_history,"Gudiya")):

        client = OpenAI(
        api_key=openaiapikey
        )

        completion = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=[
            {"role": "system", "content": "You are a person named Manisha who speak in hindi as well as english. You are from india and you are a coder. You analize chat history and respond like Manisha. Output should be the next chat response as Manisha (text messages only)."},
            {"role": "user", "content": chat_history}
        ]
        )

        response = completion.choices[0].message.content
        # print(response)
        pyperclip.copy(response)

        # Small delay to switch to the correct window
        time.sleep(2)

        # Step 1: Click on the input field (Adjust coordinates accordingly)
        pyautogui.click(834, 946)  # Change this to where you need to paste
        time.sleep(0.5) 

        # Step 2: Paste copied text
        pyautogui.hotkey('ctrl', 'v')  
        time.sleep(1)  # Give time for the paste action

        # Step 3: Press Enter
        pyautogui.press('enter')