def make_batch(preferences):
    return [person for person, enabled in preferences.items() if enabled]


def send_batch(batch, preferences, provider):
    for person in batch:
        provider.send(person)
