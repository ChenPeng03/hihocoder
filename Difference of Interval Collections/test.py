input_list = []

while True:
    line = raw_input()
    if line:
        input_list.append(line)
    else:
        break
i = int(input_list[0][0])
j = int(input_list[0][-1])
a_tmp = map(int, input_list[1].split(  ))
b_tmp = map(int, input_list[2].split(  ))

a = set()
b = set()
for k in range(i):
    for i in range(a_tmp[k*2],a_tmp[k*2 + 1] + 1):
        a.add(i)
for l in range(j):
    for i in range(b_tmp[l*2],b_tmp[l*2 + 1] + 1):
        b.add(i)
res = []
for i in range(min(min(a),min(b)),max(max(a),max(b)) + 1):
    if i not in b and i in a:
        res.append(i)
print res
