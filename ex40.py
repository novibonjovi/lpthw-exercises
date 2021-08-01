class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
            
        print('-' * 10)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

blue = Song(["Yo, listen up here's a story",
             "About a little guy",
             "That lives in a blue world"])

hallelujah = Song(["Now I've heard there was a secret chord",
                   "That David played, and it pleased the Lord",
                   "But you dont really care for music, do you?"])

lose_yourself_lyrics = ["Look", "If you had", "One shot",
                 "Or one opportunity", "To seize everything you ever wanted",
                 "In one moment", "Would you capture it", "Or just let it slip?"]

loose_yourself = Song(lose_yourself_lyrics)

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

blue.sing_me_a_song()

hallelujah.sing_me_a_song()

loose_yourself.sing_me_a_song()