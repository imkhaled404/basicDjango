# from django.http import HttpResponse
# from django.shortcuts import render
# from django.views import generic
# from .models import Post

# def chair(request):

#     posts = Post.objects.all() 
#     context = {
#         'posts': posts.order_by('-created_on')

#     }

#     return render(request, 'index.html', context)
    

# def faculty(request):

#     posts = Post.objects.all() 
#     context = {
#         'posts': posts.order_by('-created_on')

#     }

#     return render(request, 'index.html', context)