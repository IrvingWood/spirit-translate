from ulauncher.api.client.EventListener import EventListener


class PreferencesListener(EventListener):
    app_id = ''
    app_secrit = ''
    def on_event(self, event, extension):
        print(event.preferences['appId'])
        print(event.preferences['appSecrit'])