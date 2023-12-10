from django.shortcuts import render


def about_us(request):
    context = {}
    template = "about/about_us.html"
    return render(request, template, context)


def about_developers(request):
    context = {}
    template = "about/developers.html"
    return render(request, template, context)
