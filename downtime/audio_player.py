class AudioPlayer:

    def play(self, path: str, repeat: bool = False):
        raise NotImplementedError

    def stop(self):
        raise NotImplementedError
