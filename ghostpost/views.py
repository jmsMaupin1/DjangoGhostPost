from django.shortcuts import render, reverse, HttpResponseRedirect
from django.db.models import F
from django.http import QueryDict

from ghostpost.models import GhostPost
from ghostpost.forms import GhostPostForm

def post_filter_helper(request):
    posts = None
    order_by = request.GET.get('o', None)
    filter_by = request.GET.get('f', None)

    if filter_by:
        posts = GhostPost.objects.filter(isBoast=(filter_by == "boasts"))
    else:
        posts = GhostPost.objects.order_by('datetime')
    
    if order_by == 'point_total':
        if not posts:
            posts = GhostPost.objects.order_by(F('downvotes') - F('upvotes'))
        else:
            posts = posts.order_by(F('downvotes') - F('upvotes'))
    else:
        if not posts:
            posts = GhostPost.objects.order_by('datetime')
        else:
            posts = posts.order_by('datetime')
    
    return posts


def url_generator(request, suffix):
    base_url = "/?"
    current_url = request.get_full_path
    order_by = request.GET.get('o', '')
    filter_by = request.GET.get('f', '')

    if suffix == 'o':
        if not filter_by:
            return "/?o="
        else:
            return f"/?f={filter_by}&o="
    else:
        if not order_by:
            return "/?f="
        else:
            return f"/?o={order_by}&f="


def index(request):
    post_secret = None
    if request.method == 'POST':
        form = GhostPostForm(request.POST)
        
        if form.is_valid():
            post = form.save()
            post_secret = post.secret_id

    posts = post_filter_helper(request)
    return render(request, 'index.html', {
        'data': posts,
        'form': GhostPostForm(),
        'order_url': url_generator(request, 'o'),
        'filter_url': url_generator(request, 'f'),
        'post_secret': post_secret
    })


def detail_view(request, id):
    post = None
    try:
        post = GhostPost.objects.get(secret_id=id)
    except Exception:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    return render(request, 'post_details.html', {
        'post': post
    })


def delete_post(request, id):
    post = None
    try:
        GhostPost.objects.filter(secret_id=id).delete()
    except Exception:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return HttpResponseRedirect(reverse('homepage'))
    

def vote_up(request, id):
    post = GhostPost.objects.get(id=id)
    post.upvotes += 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))   


def vote_down(request, id):
    post = GhostPost.objects.get(id=id)
    post.upvotes -= 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
