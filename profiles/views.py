from django.shortcuts import render, get_object_or_404
from .models import UserProfile


def profile(request):
    """ Display the user's profile. """

    user = get_object_or_404(UserProfile, user=request.user)
    orders = user.orders.all()


    context = {
        'user' : user,
        'orders' : orders
    }
    
    return render(request, 'profiles/profiles.html', context)