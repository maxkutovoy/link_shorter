from django.shortcuts import render
from .models import Link
from .forms import LincForm


def index(request):
    if request.method == 'POST':
        form = LincForm(request.POST)
        if form.is_valid():
            url = request.POST['full_link']
            print(url)

    form = LincForm()

    data = {
        'form': form,
    }
    return render(request, 'short/index.html', data)