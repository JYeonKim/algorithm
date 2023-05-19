
input_num = input()

n = int(input_num.split(' ')[0])
m = int(input_num.split(' ')[1])
k = int(input_num.split(' ')[2])

input_num = input()

n_list = []
for n in input_num.split(" "):
    n_list.append(int(n))

n_list.sort(reverse=True)

add_num = 0
switch = 1
for i in range(m):
    if switch == k:
        switch = 1
        add_num += n_list[1]
    else:
        add_num += n_list[0]
        switch += 1

print(add_num)
