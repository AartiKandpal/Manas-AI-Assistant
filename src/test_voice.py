from audio.listener import Listener

listener = Listener()

while True:

    text = listener.listen()

    if text:

        print("Recognized:", text)