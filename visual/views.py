from django.shortcuts import render
from django.http import HttpResponse
from . import sentimentAnalysis,models

# Create your views here.

def index(request):
    return render(request, 'form.html', {})

def getSearchTerm(request):
    print("work")
    if request.method=='POST':
        searchTerm = request.POST['term']
        number = int(request.POST['number'])
        print("searchTerm")
        analysisObj=sentimentAnalysis.Analysis()
        args=analysisObj.fetchTweets(searchTerm,number)
        return render(request,'displayChart.html',context=args)
    else:
        return render(request, 'form.html')
    
    
def showTweets(request):
    positiveList=list(models.positiveTweets.objects.all())
    negativeList=list(models.negativeTweets.objects.all())
    context={'positive':positiveList,'negative':negativeList}
    return render(request,'displayTweets.html',context)

    