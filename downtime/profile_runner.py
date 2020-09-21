import time

from downtime.period import PeriodRepository
from downtime.audio_player import AudioPlayer


class ProfileRunner:

    def __init__(self, period_repository: PeriodRepository, audio_player: AudioPlayer):
        self.period_repository = period_repository
        self.audio_player = audio_player

    def run(self, profile_name):
        periods = self.period_repository.get_profile_periods(profile_name)
        current = 0
        while True:
            period = periods[current]

            uptime = period.uptime
            print(f'Working for {uptime.seconds} seconds...')
            self.audio_player.play(uptime.audio_path)
            time.sleep(uptime.seconds)

            downtime = period.downtime
            print(f'Breaking for {downtime.seconds} seconds...')
            self.audio_player.play(downtime.audio_path)
            time.sleep(downtime.seconds)

            current = (current + 1) % len(periods)
