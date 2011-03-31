class ImageFinder:

  def find_image_in_region(self, image, region):
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
