import sys
import os


inf = open("GSM6538384_HeLa_mito_0U_Hia5_footprints.tsv", 'r')

out = open("GSM6538384_HeLa_mito_0U_Hia5_footprints_TEST.tsv", 'w')


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









while True:
#for i in range(5):
	read = inf.readline()
	if read == "":
		break
	# if ">" in read:
	# 	genome = inf.readline()
	# 	if "AGCCCTACTAATTAC" in genome:
		#out.write(read)
		#out.write(genome)
	line = read.split("	")
	print(line[0])
	out.write("%s\n" % '	'.join(line[:1000]))
