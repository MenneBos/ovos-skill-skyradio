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
        self.play_audio("/home/ovos/.venvs/ovos/lib/python3.11/site-packages/skill_ovos_melody/soundbytes/As_You_Wish.mp3", False) 

def create_skill():
    return SkyRadioSkill()
