import re
fp=open("traindata.txt","r")
for word in fp:
	L=word.split()
	print(L)
fo=open("trainedlistdata.txt","a")
for words in L:
	print(words.split(","))
	fo.write(words+"\n")
print("trained")
fp.close()
