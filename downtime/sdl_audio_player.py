from sdl2.sdlmixer import Mix_OpenAudio, MIX_DEFAULT_FREQUENCY, MIX_DEFAULT_FORMAT, Mix_Init, MIX_INIT_OGG, Mix_LoadMUS, Mix_HaltMusic, Mix_FreeMusic, Mix_PlayMusic

from downtime.audio_player import AudioPlayer


Mix_OpenAudio(MIX_DEFAULT_FREQUENCY, MIX_DEFAULT_FORMAT, 2, 4096)
Mix_Init(MIX_INIT_OGG)


class SDLAudioPlayer(AudioPlayer):

    def __init__(self):
        self.audio = None
        self.path = None

    def play(self, path: str, repeat: bool = False):
        if self.audio is None:
            self.audio = Mix_LoadMUS(path.encode('utf-8'))
        elif self.path != path:
            Mix_FreeMusic(self.audio)
            self.audio = Mix_LoadMUS(path.encode('utf-8'))
        self.path = path
        Mix_PlayMusic(self.audio, -1 if repeat else 0)

    def stop(self):
        Mix_HaltMusic()
