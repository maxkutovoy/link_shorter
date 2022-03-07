import uuid
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.crypto import get_random_string

from .models import Link
from .forms import LinkForm


def get_random_slug():
    return uuid.uuid4()


def index(request):
    slug = ''
    error = ''
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            url = request.POST['full_link']
            link = Link.objects.filter(full_link=url)
            if not link:
                slug = request.POST['slug'] or get_random_slug()
                Link.objects.create(full_link=url, slug=slug)
            else:
                slug = link.last().slug
        else:
            error = 'Неверный URL'

    form = LinkForm()

    data = {
        'form': form,
        'slug': slug,
        'error': error
    }
    return render(request, 'short/index.html', data)


def short_url_redirect(request, link_slug):
    link = get_object_or_404(Link, slug=link_slug)
    return redirect(link.full_link)
