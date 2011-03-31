class RegionObserver:

  def __init__(self, region):
    self.region = region

  def start(self, delegate):
    self.region.onChange(50, delegate)
    self.region.observe(background=True)

  def stop(self):
    self.region.stopObserving()

