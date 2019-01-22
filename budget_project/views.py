"""Views."""
from django.shortcuts import render


def home_view(request):
    """Render the home view."""
    context = {
        'message': 'what up.'
    }
    return render(request, 'generic/home.html', context)
