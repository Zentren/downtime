import json

from downtime.period import Period, PeriodRepository, Session


class JsonPeriodRepository(PeriodRepository):

    def __init__(self, path: str):
        with open(path) as file:
            self.json_profiles = json.load(file)

    def get_profile_names(self):
        return [*self.json_profiles]

    def get_profile_periods(self, profile_name: str):
        json_periods = self.json_profiles[profile_name]['periods']
        return [JsonPeriodRepository._to_period(json_period) for json_period in json_periods]

    @staticmethod
    def _to_period(json_period: dict) -> Period:
        return Period(JsonPeriodRepository._to_session(json_period['uptime']), JsonPeriodRepository._to_session(json_period['downtime']))

    @staticmethod
    def _to_session(json_session: dict) -> Session:
        seconds = json_session['seconds']
        json_audio = json_session['audio']
        audio_path = json_audio['path']
        audio_repeat = json_audio['repeat']
        return Session(seconds, audio_path, audio_repeat)
