
class Emoji(object):
    positive_emojis = ["star",
                       "star2",
                       "stars",
                       "cookie"]

    def __init__(self):
        i = 0

    def is_positive(self, emoji):
        if emoji in self.positive_emojis:
            return True
        else:
            return False
