import collections
#import heapq

fp=open("trainedlistdata.txt","r")

def find_total_words():
	no_line=0
	global total_words
	for line in fp:
		word_list(line)
		no_line+=1
	return no_line
L=[]
D={}
eliminated_words_list=[]

def word_list(word):
	global L
	L.append(word)


def eliminated_words():
	global eliminated_words_list
	fo=open("excluded.txt","r")
	for stop_words in fo:
		eliminated_words_list.append(stop_words)
	print(eliminated_words_list)
	
	
def word_count():
	global D
	for keys in L:
		word_count=L.count(keys)
		fo.write(keys)
		fo.write(str(word_count)+"\n")
		density=word_count/total_words*100
		if keys not in D:
			D[keys]=density
	
	for x in eliminated_words_list:
		if x in eliminated_words_list:
			fx=open("keys.txt","a")
			fx.write(x)
			del D[x]
	main_array = set(L)
	second_array = (eliminated_words_list)
	difference=main_array.difference(eliminated_words_list)
	ft=open("remaining words.txt","a")
	for j in difference:
		ft.write(j)
	d=collections.Counter(D)
	for k, v in d.most_common(int(top_n_words)):
		print("%s : %0.2f"%(k, v))
	
	#Li=(heapq.nlargest(int(top_n_words), D, key=D.get))	
	#print(Li)
	

def user_input():
	global top_n_words
	top_n_words=input("Enter number of top words   ")

total_words=find_total_words()
fo=open("wordfrequency.txt","a")
user_input()
eliminated_words()
word_count()
fp.close()
		
