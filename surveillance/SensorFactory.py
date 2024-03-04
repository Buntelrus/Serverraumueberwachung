from surveillance.Subject import Subscription, SubscriptionArguments


class SensorFactory:
    idCount: int = 0

    def subscribe(self, subscription: Subscription):
        self.subscriptions.append(subscription)

    def unsubscribe(self, subscription: Subscription):
        self.subscriptions.remove(subscription)

    def notify(self, payload: SubscriptionArguments):
        for subscription in self.subscriptions:
            subscription(payload)
