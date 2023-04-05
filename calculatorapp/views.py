from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request, 'index.html')

def submit(request):
    query = request.GET.get('display')
    try:
        ans = eval(query)
        mydictionary = {
            "query": query,
            "ans": ans,
            "error": False,
        }
        return render(request,'index.html', context=mydictionary)
    except:
        mydictionary = {
            "error": True,
        }
    return render(request, 'index.html', context=mydictionary)