from django.shortcuts import render

# Create your views here.

from models import HeaderImage
def index(request):
    asd = HeaderImage.objects.all()
    context = {'asd': asd}
    template = 'base.html'
    return render(request, template, context)
