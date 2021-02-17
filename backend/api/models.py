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


class faculty(models.Model):
     ShortName = models.CharField(max_length=20, unique=True)
   #  slug = models.slugfield(max_length=200, unique=true, label='search tag')
     fullname = models.CharField(max_length=200)
     banglaname = models.CharField(max_length=200)
    # image = models.imagefield(upload_to='userimages/', blank = true)
     #author = models.foreignkey(User, on_delete= models.CASCADE, related_name='faculty')
     designation = models.CharField(max_length=200)
     email= models.CharField(max_length=200)
     phone = models.CharField(max_length=200)
     website = models.CharField(max_length=200)
     othercontact = models.CharField(max_length=200)
     personaldetails = Richtextfield()
     researcharea = Richtextfield()
     research_interest =  Richtextfield()
     academic_background = Richtextfield()
     selected_publications = Richtextfield()
     journal_and_conferences = Richtextfield()
     journal_papers = Richtextfield()
     conference_papers = Richtextfield()
     updated_on = models.DateTimeField(auto_now= True)
     created_on = models.DateTimeField(auto_now_add=True)
     status = models.IntegerField(choices=STATUS, default=1)
     

     def __str__(self):
         return self.fullname
        
