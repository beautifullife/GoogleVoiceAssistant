'''
This program will create new voide command base on Google Voice Assistant
Author: Danny Nguyen
date: 28 Mar. 2018
'''

import subprocess
import sys

import aiy.assistant.auth_helpers
from aiy.assistant.library import Assistant
from google.assistant.library.event import EventType
import aiy.audio
import aiy.voicehat

'''
ping localhost
'''
def ping_ip(ip="127.0.0.1"):
    print("ping result:")
    subprocess.call('ping %s' % ip, shell=True)

def ifconfig():
    print("Running ifconfig...")
    subprocess.call('ifconfig')

def process_event(assistant, event):
    # get voice hat status
    status_ui = aiy.voicehat.get_status_ui()
    
    # ready
    if event.type == EventType.ON_START_FINISHED:
        status_ui.status("ready")
        if sys.stdout.isatty():
            print("Say Hey Google or Ok, Google to start. Say Goobye to quit.")
        
    # listening
    elif event.type == EventType.ON_CONVERSATION_TURN_STARTED:
        status_ui.status("listening")

    # recorgnizing speed
    elif event.type == EventType.ON_RECOGNIZING_SPEECH_FINISHED and event.args:
        print("You said:", event.args["text"])
        text = event.args["text"].lower()
        # process command via text
        # goobye
        if "good bye" in text:
            assistant.stop_conversation()
	        return False
        elif "ping localhost" in text:
            assistant.stop_conversation()
            ping_ip()
        elif "run config" in text:
            assistant.stop_conversation()
            ifconfig()

    #thinking
    elif event.type == EventType.ON_END_OF_UTTERANCE:
        status_ui.status("thinking")

    # finish
    elif (  event.type == EventType.ON_CONVERSATION_TURN_FINISHED
            or event.type == EventType.ON_CONVERSATION_TURN_TIMEOUT
            or event.type == EventType.ON_NO_RESPONSE ):
            status_ui.status("ready")

    # error
    elif event.type == EventType.ON_ASSISTANT_ERROR and event.args and event.args["is_fatal"]:
        sys.exit(1)

    return True

def main():
    # Authorize
    credentials = aiy.assistant.auth_helpers.get_assistant_credentials()
    with Assistant(credentials) as assistant:
        for event in assistant.start():
            if process_event(assistant, event) is False:
		    break

    # loop event for process event

if __name__ == '__main__':
    main()