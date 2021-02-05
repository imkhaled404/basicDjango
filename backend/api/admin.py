from django.contrib import admin
from .models import Post 

from django.contrib import admin
from .models import Post
# from .models import facultyModel

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status", "created_on")
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    

admin.site.register(Post, PostAdmin)

# admin.site.register(facultyModel)