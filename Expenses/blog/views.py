from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')
def bill(request):
    return render(request, 'blog/bill.html')
def view(request):
    return render(request, 'blog/view.html')