# Phoenix Valent
	# ✨✨✨FINAL PROJECT✨✨✨
		# Make test code (rhymes with Grug)

# (◕_◕)    lucky autism creature makes a special cameo appearance!!!
#  ᑌ ᑌ ￣ᑌ

from os import system as s
import sample1
import sample2
import sample3
import sample4
import sample5
from testCode import *


def main():
	for i in [sample1, sample2, sample3, sample4, sample5]:
		print(i)
		testMap = i.Map()
		testMap = testMagic(testMap, i.Map())
		testMap = testIndexing(testMap, i.Map())
		testMap = testDeleting(testMap, i.Map())
		testMap = testKV(testMap)
		testDocstring(testMap)
		print('\n\n')


if __name__ == '__main__':
	s("clear")
	main()