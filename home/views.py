from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

# apply page
def apply(request):
    return render(request, 'home/apply.html')

# nonprofit page
def nonprofit(request):
    return render(request, 'home/nonprofit.html')

# private page
def private(request):
    return render(request, 'home/private.html')
    
def individual(request):
    return render(request, 'home/individual.html')