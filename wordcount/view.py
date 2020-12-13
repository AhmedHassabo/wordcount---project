from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html',{'hi':'me'})

def count(request):
    fulltext = request.GET['fulltext']
    #print(fulltext)
    wordslist= fulltext.split()

    worddictionary ={}

    for word in wordslist:
        if word in worddictionary:
            worddictionary[word]+=1
        else:
            worddictionary[word] =1
    list =worddictionary.items()

    return render(request,'count.html',{'fulltext':fulltext,'count': len(wordslist),'worddictionary':list})

def about(request):

    return render(request,'about.html')
