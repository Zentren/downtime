class Session:

    def __init__(self, seconds: int, audio_path: str, audio_repeat: bool):
        self.seconds = seconds
        self.audio_path = audio_path
        self.audio_repeat = audio_repeat


class Period:

    def __init__(self, uptime: Session, downtime: Session):
        self.uptime = uptime
        self.downtime = downtime


class PeriodRepository:

    def get_profile_names(self):
        raise NotImplementedError

    def get_profile_periods(self, profile_name: str):
        raise NotImplementedError
