class Pauser(object):
    def __init__(self, paused=False):
        self.paused = paused
        self.timer = 0
        self.pauseTime = 0
        self.playerPaused = paused
        self.pauseType = None  # (clear, die, ghost)

    def update(self, dt):
        if not self.playerPaused:
            if self.paused:
                self.timer += dt
                if self.timer >= self.pauseTime:
                    self.timer = 0
                    self.paused = False

    def startTimer(self, pauseTime, pauseType=None):
        self.pauseTime = pauseTime
        self.pauseType = pauseType
        self.timer = 0
        self.paused = True

    def player(self):
        self.playerPaused = not self.playerPaused
        if self.playerPaused:
            self.paused = True
        else:
            self.paused = False

    def force(self, pause):
        self.paused = pause
        self.playerPaused = pause
        self.timer = 0
        self.pauseTime = 0

    def settlePause(self, gamecontroller):
        if self.pauseType == "die":
            gamecontroller.resolveDeath()
        elif self.pauseType == "clear":
            gamecontroller.resolveLevelClear()
