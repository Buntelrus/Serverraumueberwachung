from typing import Callable, List

SubscriptionArguments = [int, int]
Subscription = Callable[[SubscriptionArguments], None]


class Subject:
    subscriptions: List[Callable] = []

    def subscribe(self, subscription: Subscription):
        self.subscriptions.append(subscription)

    def unsubscribe(self, subscription: Subscription):
        self.subscriptions.remove(subscription)

    def notify(self, payload: SubscriptionArguments):
        for subscription in self.subscriptions:
            subscription(payload)
