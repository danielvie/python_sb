

from api.events import subscribe
from api.runners import run_all
import api.workers as workers
from events import Events

def something_changed(reason):
    print(f"something changed because {reason}")

if __name__ == "__main__":
    
    # subscribe('bla', workers.bla)
    # subscribe('ble', workers.ble)
    # subscribe('koka', workers.printn)
    # run_all(5)
    
    events = Events()
    events.on_change += something_changed
    events.on_change += something_changed
    events.on_change += something_changed
    events.on_change += something_changed
    
    events.on_change('bla ble')
    events.on_change('bla bli')

