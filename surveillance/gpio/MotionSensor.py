from surveillance.Subject import Subject


class MotionSensor(Subject):
    motionDetected: bool = False

    # only notify when state has changed
    def updateState(self, newState):
        self.notify(newState)

