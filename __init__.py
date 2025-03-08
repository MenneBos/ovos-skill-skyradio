from ovos_workshop.skills.ovos import OVOSSkill
from ovos_bus_client.message import Message
import os
import requests

class SkyRadioSkill(OVOSSkill):
    def __init__(self):
        super().__init__("SkyRadioSkill")

    def initialize(self):
        self.add_event('mycroft.skyradio.play', self.handle_play_skyradio)
        self.register_intent_file('Playskyradio.intent', self.handle_play_skyradio)

    def handle_play_skyradio(self, message: Message):
        url = f"http://192.168.1.45/api/manager/logic/webhook/Terre/?tag=SkyRadio"
        data = requests.get(url)
        print(data.json())

def create_skill():
    return SkyRadioSkill()
