
subscribers = dict()

def subscribe(event_type: str, fn):
    if not event_type in subscribers:
        subscribers[event_type] = []
    
    subscribers[event_type].append(fn)

def run(event_type: str, data):
    
    if not event_type in subscribers:
        return
    
    for fn in subscribers[event_type]:
        fn(data)

def run_all_events(data):
    
    for event_type in subscribers:
        run(event_type, data)