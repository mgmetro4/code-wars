# Friend or Foe?  Unit Tests

from main import friend
import codewars_test as Test

Test.describe("Fixed Tests")

Test.assert_equals(friend(["Ryan", "Kieran", "Mark",]), ["Ryan", "Mark"])
Test.assert_equals(friend(["Ryan", "Jimmy", "123", "4", "Cool Man"]), ["Ryan"])
Test.assert_equals(friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]), ["Jimm", "Cari", "aret"])
Test.assert_equals(friend(["Love", "Your", "Face", "1"]), ["Love", "Your", "Face"])
Test.assert_equals(friend(["Hell", "Is", "a", "badd", "word"]), ["Hell", "badd", "word"])
Test.assert_equals(friend(["Issa", "Issac", "Issacs", "ISISS"]), ["Issa"])
Test.assert_equals(friend(["Robot", "Your", "MOMOMOMO"]), ["Your"])
Test.assert_equals(friend(["Your", "BUTT"]), ["Your", "BUTT"])
Test.assert_equals(friend(["Hello", "I", "AM", "Sanjay", "Gupt"]), ["Gupt"])
Test.assert_equals(friend(["This", "IS", "enough", "TEst", "CaSe"]), ["This", "TEst", "CaSe"])
Test.assert_equals(friend([]), [])

Test.describe("Random Tests")

from random import choice, randint

def random_tests():
    from string import ascii_letters as l, digits as d
    abc = l + d
    def random_string(friend=False):
        return "".join(choice(abc) for _ in range(friend and 4 or randint(0, 20)))
    
    def random_input():
        return [random_string(randint(0, 100) % 4 == 0) for _ in range(randint(0, 20))]

    def solution(l):
        return [w for w in l if len(w) == 4]

    for _ in range(100):
        ri = random_input()
        Test.assert_equals(friend(ri), solution(ri))


random_tests()