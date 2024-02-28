
class Actor:
    actorCount: int = 0
    def __init__(self):
        Actor.actorCount += 1
        self.actorCount: int = Actor.actorCount
