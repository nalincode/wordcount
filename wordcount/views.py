from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,"home.html",{"whatsname":"Nalin"})

def about(request):
    return render(request,"about.html",{"whatsname":"aboutme"})

def count(request):
    fulltext = request.GET['fulltext']
    print(fulltext)
    wordlist = fulltext.split()
    worddict = {}
    for word in wordlist:
        if word in worddict:
            worddict[word]+=1
        else:
            worddict[word] = 1

    sortedword = sorted(worddict.items(),key = operator.itemgetter(1),reverse = True)
    return render(request,"count.html",{'fulltext':fulltext,'count':len(wordlist), 'sortedword':sortedword})
