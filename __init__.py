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

    def handle_Playskyradio():
        url = f"http://192.168.1.45/api/manager/logic/webhook/Terre/?tag=SkyRadio"
        data = requests.get(url)
        print(data.json())
        self.speak_dialog("Please enjoy the music", wait=True)

    def handle_Stopskyradio():
        url = f"http://192.168.1.45/api/manager/logic/webhook/Terre/?tag=StopSkyRadio"
        data = requests.get(url)
        print(data.json())
        self.speak_dialog("No worry, we can always start the radio again", wait=True)
    

    # Route intents to appropriate functions
    def on_intent(intent_request):
        intent_name = intent_request['intent']['name']
        if intent_name == "Playskyradio":
            return handle_Playskyradio()
        elif intent_name == "Stopskyradio":
            return handle_Stopskyradio()
        else:
            return "Sorry my love, I didn't to stop or start skyradio."

def create_skill():
    return SkyRadioSkill()
