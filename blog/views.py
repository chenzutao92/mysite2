from django.shortcuts import render
from .models import Block


def index(request):
    blocks = Block.objects.all()
    return render(request, 'index.html', {'blocks': blocks})

