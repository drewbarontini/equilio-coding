def queue_digest(preferences):
    return [person for person, enabled in preferences.items() if enabled]


def send_digest(recipients, preferences, deliver):
    for person in recipients:
        deliver(person)
