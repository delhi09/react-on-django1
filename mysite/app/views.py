import json

from django.contrib.auth.models import User
from django.shortcuts import render


def index(request):
    context = {
        "users": json.dumps(list(User.objects.all().values("id", "username", "email")))
    }
    return render(request, "app/index.html", context)
