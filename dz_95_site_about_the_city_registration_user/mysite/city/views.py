from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from city.models import Posts


# Create your views here.
def index(request):
    posts = Posts.objects.all()
    context = {
        'title': 'Главная',
        'posts': posts,
    }
    return render(request, 'city/index.html', context=context)


def show_post(request, id):
    post = get_object_or_404(Posts, id=id)
    post.views += 1
    post.save(update_fields=['views'])
    return render(request, 'city/show_post.html', {'post': post})
