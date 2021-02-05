from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = RichTextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class facultyModel(models.Model):
    username = models.CharField(max_length=20, unique=True)
  #  slug = models.SlugField(max_length=200, unique=True, label='Search tag')
    FullName = models.CharField(max_length=200, required= False)
    BanglaName = models.CharField(max_length=200, required= False)
    image = models.ImageField(upload_to='userImages/', blank = True)
 #   author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='posts')
    Designation = models.CharField(max_length=200, required=False)
    Email= models.CharField(max_length=200, required = False )
    phone = models.CharField(max_length=200, required = False )
    Website = models.CharField(max_length=200, required = False )
    otherContact = models.CharField(max_length=200, required = False)
    personalDetails = RichTextField()
    ResearchArea = RichTextField()
    Research_Interest =  RichTextField()
    Academic_Background = RichTextField()
    Selected_Publications = RichTextField()
    Journal_and_Conferences = RichTextField()
    Journal_Papers = RichTextField()
    Conference_Papers = RichTextField()
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)

    def __str__(self):
        return self.title
        
