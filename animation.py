class Animation(object):
    def __init__(self, animType):
        self.animType = animType
        self.frames = []
        self.current_frame = 0
        self.finished = False
        self.speed = 0
        self.dt = 0

    def reset(self):
        self.current_frame = 0
        self.finished = False

    def addFrame(self, frame):
        self.frames.append(frame)

    def update(self, dt):
        if self.animType == "loop":
            self.loop(dt)
        elif self.animType == "once":
            self.once(dt)
        elif self.animType == "static":
            self.current_frame = 0
        return self.frames[self.current_frame]

    def nextFrame(self, dt):
        self.dt += dt
        if self.dt >= (1.0 / self.speed):
            self.current_frame += 1
            self.dt = 0

    def loop(self, dt):
        self.nextFrame(dt)
        if self.current_frame == len(self.frames):
            self.current_frame = 0

    def once(self, dt):
        if not self.finished:
            self.nextFrame(dt)
            if self.current_frame == len(self.frames) - 1:
                self.finished = True




