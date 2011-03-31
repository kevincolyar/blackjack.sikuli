from player import Player

Settings.ObserveScanRate = 2 # Times per second

#ui_controller = UiController()
#ui_controller.set_hit_image("")
#ui_controller.set_stand_image("")

player = Player("Bot")
player.set_hand_region(selectRegion("Select Bot Region"))
player.start_observing()

dealer = Player("Dealer")
dealer.set_hand_region(selectRegion("Select Dealer Region"))
dealer.start_observing()
