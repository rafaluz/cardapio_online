from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


def Index(request):
    return render(request, 'index.html')

@login_required
def Welcome(request):
    return render(request, 'welcome.html')