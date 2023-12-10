from django.shortcuts import render, get_object_or_404

from .models import Good


def index(request):
    goods = Good.objects.all().order_by('?')
    context = {
        "goods": goods
    }
    template = "goods/index.html"
    return render(request, template, context)


def good_info(request, pk):
    good = get_object_or_404(Good, id=pk)
    context = {
        "good": good
    }
    template = "goods/good_info.html"
    return render(request, template, context)
