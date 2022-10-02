f = open('friends.txt','r')

all = f.readlines()

for line in all:
	print(line)

print(len(all))

print(sorted(all))

f.close()

