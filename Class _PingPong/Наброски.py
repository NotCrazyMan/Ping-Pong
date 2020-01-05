def RandPlay():
        s = random.randrange(0,3)
        if s == 0:
            SoundHit1.play()
        if s == 1:
            SoundHit2.play()
        if s == 2:
            SoundHit3.play()
