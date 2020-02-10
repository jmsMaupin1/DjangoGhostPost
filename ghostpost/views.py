from django.shortcuts import render, reverse, HttpResponseRedirect

from ghostpost.models import GhostPost

def index(request):
    posts = GhostPost.objects.all()
    return render(request, 'index.html', {
        'data': posts
    })


def vote_up(request, id):
    return render(request, 'index.html', {'data': GhostPost.objects.all()})

def vote_down(request, id):
    return render(request, 'index.html', {'data': GhostPost.objects.all()})