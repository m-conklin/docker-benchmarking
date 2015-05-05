import subprocess

csv = open('linpack.csv' , 'w')
csv.close()

for i in range(2):
	subprocess.call(['./runme_xeon64'])

	f = open('lin_xeon64.txt', 'r')
	csv = open('linpack.csv' , 'a')


	for i in range(23):
		f.readline()

	while True:
		a = f.readline().split()
		if a == []:
			break
		csv.write(a[4] + ',')
		
