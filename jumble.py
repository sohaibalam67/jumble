#############################################################################
#
#This program Unjumbles the jubmled word, using a dictionary file.
#Author: Sohaib Alam
#Last Modified: 4 Apr,2017 @ 3:18 AM
#
#############################################################################


import sys
def toString(List):
    return ''.join(List)
 

f = open("dict.txt", "r").read().split('\n')
word=[]
for line in f: #imports all the words of dict into an array
	word.append(line)



def search(word, target): #binary search to find the permutated word in the dict
	start=0
	end=len(word)-1

	while start<=end:
		middle=int((start+end)/2)
		midpoint=word[middle]
		if midpoint > target:
			end = middle - 1
		elif midpoint < target:
			start = middle + 1
		else:
			return print(midpoint)



def permute(a, l, r): #finds all the possible permutations of a word
    if l==r:
        x=toString(a)
        search(word,x)
    else:
        for i in range(l,r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l] 
 
string = input("Enter a string : ")
n = len(string)
a = list(string)
permute(a, 0, n-1)
 