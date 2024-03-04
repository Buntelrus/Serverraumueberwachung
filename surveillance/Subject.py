from typing import Callable, List
from typing_extensions import Any

# todo: should be a generic
SubscriptionArguments = [Any]
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
