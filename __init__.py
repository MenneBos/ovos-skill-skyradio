from ovos_utils import classproperty
from ovos_utils.log import LOG
from ovos_workshop.skills.ovos import OVOSSkill
from ovos_utils.process_utils import RuntimeRequirements
from ovos_bus_client.message import Message

from ovos_utils import classproperty
from ovos_utils.log import LOG
from ovos_workshop.intents import IntentBuilder
from ovos_utils.process_utils import RuntimeRequirements
from ovos_workshop.decorators import intent_handler
from ovos_workshop.skills import OVOSSkill
import os
import requests

DEFAULT_SETTINGS = {
    "log_level": "WARNING"
}

class SkyRadioSkill(OVOSSkill):
    def __init__(self):
        super().__init__("SkyRadioSkill")

    def initialize(self):
        self.settings.merge(DEFAULT_SETTINGS, new_only=True)
        self.settings_change_callback = self.on_settings_changed
        self.add_event('mycroft.skyradio.play', self.handle_play_skyradio)  # add an event in the message.bus, in this case the speak event
        self.add_event('mycroft.skyradio.stop', self.handle_stop_skyradio)
        #self.register_intent_file('Playskyradio.intent', self.handle_play_skyradio)
        #self.register_intent_file('Stopskyradio.intent', self.handle_stop_skyradio)

    @classproperty
    def runtime_requirements(self):
        # if this isn't defined the skill will
        # only load if there is internet
        return RuntimeRequirements(
            internet_before_load=False,
            network_before_load=True,
            gui_before_load=False,
            requires_internet=False,
            requires_network=True,
            requires_gui=False,
            no_internet_fallback=True,
            no_network_fallback=True,
            no_gui_fallback=True,
        )

    DEFAULT_SETTINGS = {
        "log_level": "INFO"
    }

    @property
    def log_level(self):
        """Dynamically get the 'log_level' value from the skill settings file.
        If it doesn't exist, return the default value.
        This will reflect live changes to settings.json files (local or from backend)
        """
        return self.settings.get("log_level", "INFO")

    @intent_handler("Playskyradio.intent")
    def handle_play_skyradio(self, message: Message):
        LOG.info("Play SkyRadio is trigger by an intent")
        url = f"http://192.168.1.45/api/manager/logic/webhook/Terre/?tag=SkyRadio"
        data = requests.get(url)
        print(data.json())
        self.speak_dialog("Playskyradio", wait=True)

    @intent_handler("Stopskyradio.intent")
    def handle_stop_skyradio(self, message: Message):
        LOG.info("Play SkyRadio is stopped by an intent")
        url = f"http://192.168.1.45/api/manager/logic/webhook/Terre/?tag=StopSkyRadio"
        data = requests.get(url)
        print(data.json())
        self.speak_dialog("Stopskyradio", wait=True)
        #self.speak_dialog("No worry, we can always start the radio again", wait=True)

    @intent_handler(IntentBuilder("SkyRadioIntentnt").require("KeyWordSkyRadio"))
    def handle_sky_radio_intent(self, message):
        LOG.info("Sky Radio intent is triggered with KeyWord")
        # wait=True will block the message bus until the dialog is finished
        self.speak_dialog("Playskyradio", wait=True)

    def stop(self) -> bool:
        """Optional action to take when "stop" is requested by the user.
        This method should return True if it stopped something or
        False (or None) otherwise.
        If not relevant to your skill, feel free to remove.
        """
        return False

#def create_skill():
    #return SkyRadioSkill()
