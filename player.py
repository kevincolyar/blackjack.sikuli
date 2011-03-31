from region_observer import RegionObserver

class Player:

  def __init__(self, name):
    self.name = name
    #self.state_machine = PlayerStateMachine()

  def set_hand_region(self, r):
    self.hand_region_observer = RegionObserver(r)

  def start_observing(self):
    self.hand_region_observer.start(self.hand_changed)

  def stop_observing(self):
    self.hand_region_observer.stop_observing()

  def hand_changed(self, event):
    text = event.region.text()
    if text != '':
      self.count = text
      print self.name + ": "
      print self.count

