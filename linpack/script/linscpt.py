f = open('lin_xeon64.txt', 'r')
csv = open('linpack.csv' , 'w')


for i in range(23):
	f.readline()

while True:
	a = f.readline().split()
	if a == []:
		break
	csv.write(a[4] + ',')
	
