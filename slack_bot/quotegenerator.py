import random


class QuoteGenerator(object):
    quoteList = ["Tonight ladies and gentlemen, I will eat this rubber tire to the music The Flight of the Bumblebee",
                 "If I ruled the world, clothing would be edible!",
                 "WOCKA WOCKA",
                 "Oh, I tell ya, Camilla, great plumbers are born, not made! I'm the prince of plungers, fair maiden!",
                 "Sure, if you want to do it the easy way!",
                 "Are we lucky or what?",
                 "I'm getting taller. This is cool; I may have a future in the NBA",
                 "There's not a word yet for old friends who've just met",
                 "Wow! We're in a sewer! Gee... nothing can touch the magic of Disney...",
                 "Walt Disney's Laundry-Land! Lordy, it's a dream come true.",
                 "Maybe we could sell the show if we wrote in more special effects...like exploding socks!",
                 "What foolishness would you like to see?",
                 "I shall now defuse this highly explosive bomb while simultaneously, and at the same time, "
                 "reciting from the works of Percy Bysshe Shelley.",]

    def __init__(self):
        super(QuoteGenerator, self).__init__()

    def random(self):
        index = random.randint(0, len(self.quoteList)-1)
        return self.quoteList[index]