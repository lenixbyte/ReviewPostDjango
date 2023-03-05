from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Post
from django.views.decorators.csrf import csrf_exempt
import logging

@csrf_exempt
def Review(request, post_id=None):
    if request.method == 'POST':
        formdata = request.POST
        post = Post.objects.get(id=post_id)
        isLiked = int(formdata.get('isLiked'))
        if (isLiked):
            post.likecount += 1
        else:
            post.dislikecount += 1
        post.save()
        return JsonResponse({"likecount":post.likecount,"dislikecount":post.dislikecount},safe=False)
    return JsonResponse({"message":"invalid request"})

def home(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {"posts": posts})
