'''
This program will create new voide command base on Google Voice Assistant
Author: Danny Nguyen
date: 28 Mar. 2018
'''

import subprocess
import sys

import aiy.assistant.auth_helpers
from aiy.assistant.library.event import EvenType
import aiy.audio
import aiy.voicehat

'''
ping localhost
'''
def ping_ip(ip="127.0.0.1"):
    print("ping result:")
    subprocess.call('ping %s' % ip, shell=True)

def process_event(assistant, event):
    # get voice hat status
    status_ui = ayi.voicehat.get_status_ui()
    
    # ready
    if event.type == EvenType.ON_START_FINISHED:
        status_ui.status("ready")
        if sys.stdout.isatty():
            print("Say Hey Google or Ok, Google to start...")
        
    # listening
    elif event.type == EvenType.ON_CONVERSATION_TURN_STARTED:
        status_ui.status("listening")

    # recorgnizing speed
    elif event.type == EvenType.ON_RECOGNIZE_SPEECH_FINISHED and event.args:
        print("You said:", event.args["text"])
        text = event.args["text"].lower()
        # process command via text
        # goobye
        if "good bye" in text:
            assistant.stop_conversation()
        elif "ping localhost" in text:
            assistant.stop_conversation()
            ping_ip()

    #thinking
    elif event.type == EvenType.ON_END_OF_UTTERANCE:
        status_ui.status("thinking")

    # finish
    elif (  event.type == EvenType.ON_CONVERSATION_TURN_FINISHED
            or event.type == EvenType.ON_CONVERSATION_TURN_TIMEOUT
            or event.type == EvenType.ON_NO_RESPONSE ):
            status_ui.status("ready")

    # error
    elif event.type == EvenType.ON_ASSISTANT_ERROR and event.args and event.args["is_fatal"]:
        sys.exit(1)


def main():
    # Authorize
    credentials = ayi.assistant_helper.get_assistant_credentials()
    with Assistant(credentials) as assistant:
        for event in assistant.start():
            process_event(assistant, event)

    # loop event for process event

if __name__ == '__main__':
    main()