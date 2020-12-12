import pickle
from mypinyin import Pinyin
import random
import sys

def func(a):
    with open('./poemDict.pk', 'rb') as f:
        poem_dict = pickle.load(f)

    enter = a
    for i in range(20):
        test = Pinyin().get_pinyin(enter, tone_marks='marks', splitter=' ')
        tail = test.split()[-1]
        if tail not in poem_dict.keys():
            MODE = 0
            break
        else:
            answer = random.sample(poem_dict[tail], 1)[0]
            answer = answer.replace("\n", "")
            print('%s' % (answer))
            answer = list(answer)
            enter = answer.pop()
            while enter == " "  or enter == "\n" or enter == "。":
                enter=answer.pop()
            MODE = 0

if len(sys.argv) == 1:
    exit()
func(sys.argv[1])
