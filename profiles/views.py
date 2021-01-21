from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apiary.models import Apiary_details
from hives.models import hive_details
from django.contrib import messages
# Create your views here.


@login_required
def profile(request):
    user = request.user
    apiaries_number = Apiary_details.objects.filter(user=user).count()
    hives_number = hive_details.objects.filter(user=user).count()
    context = {
        'user': user,
        'apiaries_number': apiaries_number,
        'hives_number': hives_number,
    }
    return render(request, 'profiles/user_profile.html', context)
