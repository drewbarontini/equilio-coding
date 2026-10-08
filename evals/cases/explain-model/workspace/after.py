def make_batch(preferences):
    return [person for person, enabled in preferences.items() if enabled]


def send_batch(batch, preferences, provider):
    for person in batch:
        if preferences.get(person, False):
            provider.send(person)
