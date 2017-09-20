import collections
from collections import defaultdict

doc_1 = ['Adam', 'Eve', 'apple', 'shake']
doc_2 = ['Adam', 'even', 'orange', 'snake']
doc_3 = ['man', 'Eve', 'pineapple', 'fish']


def indexrev(*args):
    d = defaultdict(list)
    i = 1
    if args is not None:
        for arg in args:
            for word in arg:
                d[word].append(i)
            i+=1
    return d


print(indexrev(doc_1, doc_2, doc_3))
                
                
        
