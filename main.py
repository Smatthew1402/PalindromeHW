from collections import deque


class PalinChecker:
    def __init__(self):
        pass

    def isdrome(self, wordin):
        word = str(wordin)
        isdrome = True
        rightqueue = deque([])
        rightqueue = self.fillqueue(word.lower(), rightqueue)
        leftqueue = deque([])
        for num in range(int(len(rightqueue)/2)):
            leftqueue.append(rightqueue.popleft())
        leftqueue.reverse()
        if len(word) % 2 == 1:
            rightqueue.popleft()
        for num in range(len(rightqueue)):
            if isdrome:
                isdrome = (rightqueue.popleft() == leftqueue.popleft())
        return isdrome

    def fillqueue(self, word, queue):
        for letter in word:
            queue.append(letter)
        return queue


if __name__ == '__main__':
    pc = PalinChecker()
    print("Commencing Positive Tests:\n")
    print("1. racecar  , True: ", pc.isdrome('racecar'))
    print("2. kayak    , True:", pc.isdrome('kayak'))
    print("3. deified  , True:", pc.isdrome('deified'))
    print("4. rotator  , True:", pc.isdrome('rotator'))
    print("5. repaper  , True:", pc.isdrome('repaper'))
    print("6. deed     , True:", pc.isdrome('deed'))
    print("7. peep     , True:", pc.isdrome('peep'))
    print("8. wow      , True:", pc.isdrome('wow'))
    print("9. noon     , True:", pc.isdrome('noon'))
    print("10. civic   , True:", pc.isdrome('civic'))
    print("\nPositive tests complete, ------------------------- \nCommencing Negative Tests:\n ")
    print("1. racecars , False:", pc.isdrome('racecars'))
    print("2. kayaks   , False:", pc.isdrome('kayaks'))
    print("3. defies   , False:", pc.isdrome('defies'))
    print("4. rotators , False:", pc.isdrome('rotators'))
    print("5. depaper  , False:", pc.isdrome('depaper'))
    print("6. deeds    , False:", pc.isdrome('deeds'))
    print("7. peeps    , False:", pc.isdrome('peeps'))
    print("8. vow      , False:", pc.isdrome('vow'))
    print("9. moon     , False:", pc.isdrome('moon'))
    print("10. civics  , False:", pc.isdrome('civics'))
    print("\nNon-Conventional checks:\n")
    print("12322,     False:", pc.isdrome("12322"))
    print("12321,     True: ", pc.isdrome("12321"))
    print("1111111,   True: ", pc.isdrome('1111111'))
    print("123456789, False:", pc.isdrome('123456789'))
    print("123221,    False:", pc.isdrome("123221"))
    print("Nonetype,  False:", pc.isdrome(None))
