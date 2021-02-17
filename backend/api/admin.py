from django.contrib import admin
from .models import Post 

from django.contrib import admin
from .models import Post
from .models import faculty

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status", "created_on")
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class facultyAdmin(admin.ModelAdmin):
    list_display = ('ShortName', 'fullname', 'status','created_on')
    list_filter = ("status", "created_on")
    search_fields = ['ShortName', 'fullname']
    

admin.site.register(Post, PostAdmin)

admin.site.register(faculty, facultyAdmin)