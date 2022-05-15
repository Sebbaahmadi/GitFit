from django.shortcuts import render

# Create your views here.
def FullBody(request):
    return render(request,'programs/FullBody.html')

def Legs(request):
    return render(request,'programs/Legs.html')

def strength(request):
    return render(request,'programs/strength.html')
