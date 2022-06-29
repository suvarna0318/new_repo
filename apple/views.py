from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request,'apple/home.html',context={'page':'Home page display',})