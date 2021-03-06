class ImageFinder:

  def find_all_images_in_region(self, image, region):
    r = [] 
    matches = region.findAll(image)

    if matches == None:
      return r

    while matches.hasNext():
      match = matches.next()
      if match != None and match.score > 0.9:
        r.append(match)

    matches.destroy()
    return r

  def find_image_in_region(self, image, region):
    match = region.find(image)
    if match != None:
      return match
    else:
      return []
