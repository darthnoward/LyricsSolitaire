import re
import pickle
from xpinyin import Pinyin
from collections import defaultdict

def main():
    with open('poem.txt', 'r') as f:
        poems = f.readlines()

    sents = []
    for poem in poems:
        #parts = re.findall(r'[sS]*?[。？！]',poem.strip())
        parts= re.split('。|？|！',poem.strip())#根据句号问号感叹号分割诗句
        for part in parts:
            if len(part) >= 4:
                sents.append(part.strip())
    poem_dict = defaultdict(list)
    a = list(set(sents))    
    for sent in a:
        head = Pinyin().get_pinyin(sent, tone_marks='marks', splitter=' ').split()[0]#将诗句转换为拼音，区第一个元素即只取第一个拼音
        poem_dict[head].append(sent)#将诗句的第一个拼音以及诗句以字典的形式存贮
    with open('poemDict.pk', 'wb') as f:
        pickle.dump(poem_dict, f)

main()
