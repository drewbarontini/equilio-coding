def handle(event, seen, notify, log):
    log(event)
    notify(event)
    return 200
