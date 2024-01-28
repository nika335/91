from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def midlad(request):
    if request.method == 'POST':
        noun = request.POST.get('noun')
        verb = request.POST.get('verb')
        adjective = request.POST.get('adjective')
        adverb = request.POST.get('adverb')
        return render(request, 'madlib.html', {'noun':noun, 'verb':verb, 'adjective':adjective, 'adverb':adverb })
    else:
        return render(request, 'index.html')
