import os

import aiy.cloudspeech
import aiy.voicehat
import aiy.audio

def main():
    # get void recognize
    recognizer = aiy.cloudspeech.get_recognizer()
    recognizer.expect_phrase("turn on the light")
    recognizer.expect_phrase("turn off the light")
    recognizer.expect_phrase("blink")
    recognizer.expect_phrase("repeat after me")

    # get voicehat button
    button = aiy.voicehat.get_button()
    # get led light
    led = aiy.voicehat.get_led()
    # start record
    aiy.audio.get_recorder().start()

    #loop recognize voice command
    while True:
        print("Press the button and speak")
        button.wait_for_press()
        print("Listening...")
        # get command from user
        text = recognizer.recognize()
        # process command via text
        if text is None:
            print("I didn't hear anything.")
        else:
            print("You said: ", text)
            if "turn on the light" in text:
                led.set_state(aiy.voicehat.LED.ON)
            elif "turn off the light" in text:
                led.set_state(aiy.voicehat.LED.OFF)
            elif "blink" in text:
                led.set_state(aiy.voicehat.LED.BLINK)
            elif "repeat after me" in text:
                aiy.audio.say(text.replace("repeat after me", "", 1))
            elif "good bye" in text:
                os._exit(0)


if __name__ == '__main__':
    main()