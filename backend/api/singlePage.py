# from django.http import HttpResponse
# from django.shortcuts import render
# from django.views import generic
# from .models import Post


# def Why_CSE_at_BUBT(request):

#     posts = Post.objects.all() 
#     context = {
#         'posts': posts.order_by('-created_on')

#     }

#     return render(request, 'index.html', context)

# def Achievements(request):

#     posts = Post.objects.all() 
#     context = {
#         'posts': posts.order_by('-created_on')

#     }

#     return render(request, 'index.html', context)