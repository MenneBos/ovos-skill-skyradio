from ovos_workshop.skills.ovos import OVOSSkill
from ovos_bus_client.message import Message
import os
import requests

class SkyRadioSkill(OVOSSkill):
    def __init__(self):
        super().__init__("SkyRadioSkill")

    def initialize(self):
        self.add_event('mycroft.skyradio.play', self.handle_play_skyradio)
        self.add_event('mycroft.skyradio.stop', self.handle_stop_skyradio)
        self.register_intent_file('Playskyradio.intent', self.handle_play_skyradio)
        self.register_intent_file('Stopskyradio.intent', self.handle_stop_skyradio)

    def handle_play_skyradio():
        url = f"http://192.168.1.45/api/manager/logic/webhook/Terre/?tag=SkyRadio"
        data = requests.get(url)
        print(data.json())
        #self.speak_dialog("Enjoy the music", wait=True)
        self.speak("Enjoy the music", wait=True)

    def handle_stop_skyradio():
        url = f"http://192.168.1.45/api/manager/logic/webhook/Terre/?tag=StopSkyRadio"
        data = requests.get(url)
        print(data.json())
        #self.speak_dialog("Stopskyradio", wait=True)
        self.speak("No worry, we can always start the radio again", wait=True)

def create_skill():
    return SkyRadioSkill()
