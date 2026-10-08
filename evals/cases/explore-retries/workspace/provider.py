"""Local simulator; its behavior is not a real provider's contract."""


class ProviderTimeout(Exception):
    pass


class Provider:
    def __init__(self, outcomes):
        self.outcomes = list(outcomes)
        self.accepted = []
        self.calls = []

    def send(self, event_id):
        self.calls.append(event_id)
        outcome = self.outcomes.pop(0) if self.outcomes else "accept"
        if outcome == "timeout_before_accept":
            raise ProviderTimeout("Timed out before acceptance")
        self.accepted.append(event_id)
        if outcome == "timeout_after_accept":
            raise ProviderTimeout("Timed out after acceptance")
        if outcome != "accept":
            raise ValueError(f"Unknown outcome: {outcome}")
        return event_id
