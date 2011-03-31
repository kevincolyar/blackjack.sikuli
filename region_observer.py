class RegionObserver:

  def __init__(self, region):
    self.region = region

  def start(self, delegate):
    #self.region.onChange(50, delegate)
    #self.region.onAppear("A.png", delegate)
    self.region.onAppear("2.png", delegate)
    self.region.observe(background=True)

  def stop(self):
    self.region.stopObserving()

