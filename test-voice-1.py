'''
This program will create new voide command base on Google Voice Assistant
Author: Danny Nguyen
date: 28 Mar. 2018
'''

import subprocess

'''
ping localhost
'''
def pingIp(ip="127.0.0.1"):
    print("ping result:")
    subprocess.call('ping %s' % ip, shell=True)

def processEvent(assistant, event):
    # get voice hat status
    status = ayi.voicehat.get_status_ui()
    
    # ready
    

    # turn started

    # recorgnizing speed

    # thinking

    # finish

    # error


def main():
    # Authorize
    credentials = ayi.assistant_helper.get_assistant_credentials()
    with Assistant(credentials) as assistant:
        for event in assistant.start():
            processEvent(assistant, event)

    # loop event for process event

if __name__ == '__main__':
    main()