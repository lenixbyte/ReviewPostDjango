from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Post
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def Review(request, post_id=None):
    if request.method == 'POST':
        formdata = request.POST
        post = Post.objects.get(id=post_id)
        isLiked = int(formdata.get('isLiked'))
        # enter your code here
        post.save()
        return JsonResponse({"likecount":post.likecount,"dislikecount":post.dislikecount},safe=False)
    return JsonResponse({"message":"invalid request"})

def home(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {"posts": posts})
