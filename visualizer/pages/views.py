from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request,'about.html')

def dashboard(request):
    return render(request,'dashboard.html')

def index(request):
    return render(request,'index.html')

def arrays(request):
    return render(request,'arrays.html')

def linkedlist(request):
    return render(request,'linkedlist.html')

def stack(request):
    return render(request,'stack.html')

def queue(request):
    return render(request,'queue.html')

def searchtypes(request):
    return render(request,'searching_types.html')

def sorttypes(request):
    return render(request,'sorting_types.html')