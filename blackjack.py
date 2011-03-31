from player import Player
from image_finder import ImageFinder

Settings.ObserveScanRate = 2 # Times per second

#ui_controller = UiController()
#ui_controller.set_hit_image("")
#ui_controller.set_stand_image("")

player = Player("Bot")
player.set_hand_region(selectRegion("Select Bot Region"))
player.hand_region.setFindFailedResponse(SKIP)
#player.start_observing()

image_finder = ImageFinder()

while True:
  matches = []
  cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
  for c in cards:
    matches += image_finder.find_image_in_region(c + ".png", player.hand_region)

  for match in matches:
    match.highlight()
  wait(1)
  for match in matches:
    match.highlight()

  #matches.destroy()
  #wait(1)

