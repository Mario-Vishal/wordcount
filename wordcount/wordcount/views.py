from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
	return render(request,'home.html')



def count(request):
	text=request.GET['fulltext']
	wordlist=text.split()
	worddict={}
	for w in wordlist:
		if w in worddict:
			#Increase 
			worddict[w]+=1
		else:
			#add to the dictionary
			worddict[w]=1
	swords=sorted(worddict.items(),key=operator.itemgetter(1),reverse=True)
	return render(request,'count.html',{'text':text,'count':len(wordlist),'list':swords})

def about(request):
	return render(request,'about.html')