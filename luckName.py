def lucky_four(filename):
	name = []
	surname = []
	surname2 = []
	lucknames = []

	with open(filename,'r',encoding = 'utf-8') as students:
	
		for fullname in students:
			fullname=fullname.split()
			name.append(fullname[0])
			surname.append(fullname[1])
			if len(fullname) == 3:
				surname2.append(fullname[2])
			else:
				surname2.append(' ')

	for index in range(len(name)):
		if name[index][0]==surname[index][0] or surname[index][0]==surname2[index][0] or name[index][0]==surname2[index][0]:
			if surname2[index] != " ":
				lucknames.append(name[index]+" "+surname[index]+" "+surname2[index])
			else:
				lucknames.append(name[index]+" "+surname[index])

	
	with open("lucky-names.txt",'w',encoding = 'utf-8') as lucknamesfile:
		for name in lucknames:
			lucknamesfile.write(name+"\n")


def main():
	lucky_four("names.txt")


main()