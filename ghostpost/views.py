from django.shortcuts import render, reverse, HttpResponseRedirect

from ghostpost.models import GhostPost

def index(request):
    posts = GhostPost.objects.all()
    return render(request, 'index.html', {
        'data': posts
    })


def vote_up(request, id):
    post = GhostPost.objects.get(id=id)
    post.upvotes += 1
    post.save()
    return render(request, 'index.html', {'data': GhostPost.objects.all()})

def vote_down(request, id):
    post = GhostPost.objects.get(id=id)
    post.upvotes -= 1
    post.save()
    return render(request, 'index.html', {'data': GhostPost.objects.all()})