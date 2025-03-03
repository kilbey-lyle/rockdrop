from django.shortcuts import render


def profile(request):
    """ Display the user's profile. """

    context = {}
    
    return render(request, 'profiles/profiles.html', context)