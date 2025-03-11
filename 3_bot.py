import pyautogui
import pyperclip
import time
from openai import OpenAI  

client = OpenAI(api_key= "your API key"
    )
def is_last_message_from_sender(chat_log, sender_name= "Medha"):
     # Split the chat log into lines
    lines = chat_log.strip().split("\n")
    
    # Get the last message
    if not lines:
        return False  # No messages found
    
    last_line = lines[-1]  # Get the last message line
    
    # Check if it starts with the sender's name
    return sender_name in last_line

# Wait for 1 second to ensure the screen is ready (optional)
pyautogui.click (960 ,1053)
time.sleep(2)

while True:

    # Drag to select text
    pyautogui.moveTo(740,222)  # Move to start position
    pyautogui.dragTo(1721,944, duration=2, button='left')  # Drag to select text

    # Copy selected text
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)  # Give time for copying
    pyautogui.click(1721,850)

    # Get text from clipboard
    chat_history = pyperclip.paste()

    # Print or use the copied text
    print("Copied Text:", chat_history)

    if is_last_message_from_sender(chat_history):

        completion = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a person name Amardeep that provides clear and concise responses. Do not include the current date, time, or  your  name."},
                    {
                        "role": "user",
                        "content": chat_history     }
        ]
        )

        response = completion.choices[0].message.content   

        pyperclip.copy(response)

        pyautogui.click (909,980 )
        time.sleep(1)

        pyautogui.hotkey('ctrl', 'v')
        time.sleep(2)  
    
        pyautogui.press('enter')
  
