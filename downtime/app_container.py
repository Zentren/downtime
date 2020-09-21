from dependency_injector import containers, providers

from downtime.json_period_repository import JsonPeriodRepository
from downtime.sdl_audio_player import SDLAudioPlayer
from downtime.profile_runner import ProfileRunner


class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    period_repository = providers.Singleton(
        JsonPeriodRepository,
        path=config.settings.profile_path
    )

    audio_player = providers.Singleton(SDLAudioPlayer)

    profile_runner = providers.Singleton(
        ProfileRunner,
        period_repository,
        audio_player
    )


container = Container()
container.config.from_ini('downtime.ini')
