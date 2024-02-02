from django.shortcuts import render
from django.utils.translation import gettext_lazy as _


def index(request):
    context = {'title': 'TaskWeb - ' + _('Main')}

    return render(request, 'mainApp/main.html', context)


def pages(request, page_link):
    context = {'title': 'TaskWeb - ' + _(page_link.capitalize())}

    return render(request, 'mainApp/main.html', context)


def sub_pages(request, page_link, sub_page_link):
    context = {'title': 'TaskWeb - ' + _(page_link.capitalize())+' - '+_(sub_page_link.capitalize())}

    return render(request, 'mainApp/main.html', context)
