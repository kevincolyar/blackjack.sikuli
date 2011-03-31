from region_observer import RegionObserver
import time

class Player:

  def __init__(self, name):
    self.name = name

  def set_hand_region(self, r):
    self.hand_region = r
    self.hand_region_observer = RegionObserver(r)

  def start_observing(self):
    self.hand_region_observer.start(self.hand_changed)

  def stop_observing(self):
    self.hand_region_observer.stop_observing()

  def hand_changed(self, event):
    print event
    event.match.highlight()
    time.sleep(1)
    event.match.highlight()
