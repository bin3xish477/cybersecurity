from colored import fg, attr, bg

# regular colors
r, e, b, p, o, y, g, w, k = 196, 76, 33, 135, 208, 226, 245, 255, 0

red = lambda s: "%s%s" % (fg(r), s)
green = lambda s: "%s%s" % (fg(e), s)
blue = lambda s: "%s%s" % (fg(b), s)
purple = lambda s: "%s%s" % (fg(p), s)
orange = lambda s: "%s%s" % (fg(o), s)
yellow = lambda s: "%s%s" % (fg(y), s)
grey = lambda s: "%s%s" % (fg(g), s)
black = lambda s: "%s%s" % (fg(k), s)
white = lambda s: "%s%s" % (fg(w), s)

normal = lambda s: "%s%s" % (s, attr(0))
bold = lambda s: "%s%s%s" % (s, attr('bold'), attr('reset'))
bkgrd = lambda s, color: "%s%s%s" % (bg(color), s,  attr('reset'))