from mycroft import MycroftSkill, intent_file_handler


class Launcher(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('launcher.intent')
    def handle_launcher(self, message):
        self.speak_dialog('launcher')


def create_skill():
    return Launcher()

