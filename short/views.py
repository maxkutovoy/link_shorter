from django.shortcuts import render, redirect, get_object_or_404
from django.utils.crypto import get_random_string

from .models import Link
from .forms import LincForm


def get_random_slug():
    while True:
        random_slug = get_random_string(length=6)
        if not Link.objects.filter(slug=random_slug):
            return random_slug


def index(request):
    slug = ''
    error = ''
    if request.method == 'POST':
        form = LincForm(request.POST)
        if form.is_valid():
            url = request.POST['full_link']
            link = Link.objects.filter(full_link=url)
            if not link:
                slug = get_random_slug()
                Link.objects.create(full_link=url, slug=slug)
            else:
                slug = link.last().slug
        else:
            error = 'Неверный URL'

    form = LincForm()

    data = {
        'form': form,
        'slug': slug,
        'error': error
    }
    return render(request, 'short/index.html', data)


def short_url_redirect(request, link_slug):

    link = get_object_or_404(Link, slug=link_slug)

    return redirect(link.full_link)
