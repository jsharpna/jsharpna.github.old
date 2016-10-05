from random import uniform
from sortedcontainers import SortedList

x = [uniform(0,1) for i in xrange(20000)]
val = x[4500]
%time x.index(val)

rev_dict = dict(zip(x, range(20000)))
%time rev_dict[val]

rev_bis = SortedList((v,i) for (i,v) in enumerate(x))
%time rev_bis.bisect((val,))




