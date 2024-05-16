import sys
import os


inf = open("GSM6538384_HeLa_mito_0U_Hia5.bed", 'r')

out_full = open("GSM6538384_HeLa_mito_0U_Hia5_full.mtrx", 'w')
out_hund = open("GSM6538384_HeLa_mito_0U_Hia5_hund.mtrx", 'w')



arr = []
for i in range(16568):
	arr.append(str(i))
out_full.write("%s\n" % ';'.join(arr))


arr = []
for i in range(0,16600,100):
	arr.append(str(i))
out_hund.write("%s\n" % ';'.join(arr))


k = 0
while True:
	print(k)
	
	read = inf.readline()
	if read == "":
		break

	line = read.split("	")

	box = line[11].split(",")

	arr = []
	for i in range(16568):
		if str(i) in box:
			arr.append(str(1))
		else:
			arr.append(str(0))


	out_full.write("%s;%s\n" % (k,';'.join(arr)))


	arr = []
	for i in range(0,16600,100):
		arr.append(0)
	for i in box:
		arr[int(i)//100]+=1
	for i in range(len(arr)):
		arr[i]=str(arr[i])


	out_hund.write("%s;%s\n" % (k,';'.join(arr)))

	k+=1


#for i in range(5):

	# if ">" in read:
	# 	genome = inf.readline()
	# 	if "AGCCCTACTAATTAC" in genome:
		#out.write(read)
		#out.write(genome)



# # while True:
# for i in range(5):
# 	read = inf.readline()
# 	if read == "":
# 		break
# 	# if ">" in read:
# 	# 	genome = inf.readline()
# 	# 	if "AGCCCTACTAATTAC" in genome:
# 		#out.write(read)
# 		#out.write(genome
# 	out.write(read)



# while True:
# #for i in range(5):
# 	read = inf.readline()
# 	if read == "":
# 		break
# 	# if ">" in read:
# 	# 	genome = inf.readline()
# 	# 	if "AGCCCTACTAATTAC" in genome:
# 		#out.write(read)
# 		#out.write(genome)
# 	line = read.split("	")
# 	print(line[0])
# 	out.write("%s\n" % '	'.join(line[:11]))




