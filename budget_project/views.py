from django.shortcuts import render


def home_view(request):
    context = {
        'message': 'what up.'
    }
    return render(request, 'generic/home.html', context)
