import collections
line = int(raw_input())
in_f = []
maximum = float('-inf')
minimum = float('inf')
recent = 0
dic = collections.OrderedDict()
if line == 0:
    pass
else:


    for i in range(line):

        in_f.append(raw_input().split( ))


    for item in in_f:
        if item[0] == 'P':
            dic[item[1]] = int(item[2])
            recent = int(item[2])
            maximum = max(int(item[2]),maximum)
            minimum = min(int(item[2]),minimum)
        if item[0] == 'Q':
            print (str(maximum) +" "+ str(minimum) +' '+ str(recent))
        if item[0] == 'R':
            while int(dic.items()[0][0]) <= int(item[1]):

                dic.popitem(False)
            if dic:
                maximum = max(dic.values())
                minimum = min(dic.values())
                recent = dic.items()[-1][1]
            else:
                maximum = float("-inf")
                minimum = float('inf')
                recent = 0
