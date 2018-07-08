from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request,'home.html')

def count(request):
    ft = request.GET['fulltext']
    wordlist = ft.split()
    wordcountdict = {}
    for word in wordlist:
        if word in wordcountdict:
            wordcountdict[word] += 1
        else:
            wordcountdict[word] = 1
    sortedwords = sorted(wordcountdict.items(), key = operator.itemgetter(1), reverse=True)
    return render(request,'count.html',{'fulltext':ft, 'count':len(wordlist),'wordcountdict':sortedwords})


def about(request):
    return render(request,'about.html',{'key':"This is a Django About"})
