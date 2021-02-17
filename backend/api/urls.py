from django.urls import path

from . import views

from . import faculty
# from .navigationBar import about
# from . import news
# from . import singlePage
# from . import faq


urlpatterns = [
    path('', views.index, name='index'),
     path('faculty', faculty.faculty, name='Faculty'),
#     path('/About_CSE', about.about, name='About CSE'),
#  #   path('/Message_from_the_chairman', views.index, name=''),
#  #    path('/Industry_advisory panel', views.index, name=''),
#      path('/Why_CSE_at_BUBT', singlePage.Why_CSE_at_BUBT, name='Why_CSE_at_BUBT'),
#    #  path('/Achievements', singlePage, name=''),
#  #    path('/Contact', views.index, name=''),
#  #    path('/Program', views.index, name=''),
# #    path('/Vision_of_CSE_department', views.index, name=''),
# #    path('/Mission_of_CSE_department', views.index, name=''),
# #    path('/Program_Educational_Objectives', views.index, name=''),
# #    path('/Department', views.index, name=''),
# #    path('/Mapping_of_PEOs_to_Mission_of_CSE_department', views.index, name=''),
# #    path('/Program_Outcomes', views.index, name=''),
# #    path('/Mapping_of_Program_Outcomes', views.index, name=''),
# #    path('/Educational_Objectives', views.index, name=''),
# #    path('/Complex_Engineering_Activities', views.index, name=''),
# #    path('/Course_Summary', views.index, name=''),
# #    path('/List_of_Courses', views.index, name=''),
# #    path('/Course_Description', views.index, name=''),
# #    path('/Course_Flowchart', views.index, name=''),
# #    path('/Academic_Calendar', views.index, name=''),
# #    path('/Admission', views.index, name=''),
# #    path('/Admission_information', views.index, name=''),
# #    path('/Tuition_Fee_and_Waiver', views.index, name=''),
# #    path('/Admission_Requirements', views.index, name=''),
# #    path('/Apply_Online.', views.index, name=''),
# #    path('/Admission_Test.', views.index, name=''),
# #    path('/People', views.index, name=''),

# #    path('/Lab_Instructors_and_IT_Officers', views.index, name=''),
# #    path('/Administrative_Staffs', views.index, name=''),
# #    path('/Researches', views.index, name=''),
# #    path('/Journal', views.index, name=''),
# #    path('/Conference', views.index, name=''),
# #    path('/Book', views.index, name=''),
# #    path('/Research_Projects', views.index, name=''),
# #    path('/Research_Collaboration', views.index, name=''),
# #    path('/Students_Corner', views.index, name=''),
# #     path('/Class_Routine', views.index, name=''),
# #    path('/Microsoft_Imagine_Program', views.index, name=''),
# #    path('/Study_Tour', views.index, name=''),
# #    path('/Industry_Visit', views.index, name=''),
# #    path('/Resources_and_Facilities', views.index, name=''),
# #    path('/Learning_Room_Space', views.index, name=''),
# #    path('/Lab_Facilities', views.index, name=''),
# #    path('/Medical_Facilities', views.index, name=''),
# #    path('/Club_Facilities', views.index, name=''),
# #    path('/Counseling', views.index, name=''),
# #    path('/Cafeteria', views.index, name=''),
# #    path('/IT_Services_for_Students', views.index, name=''),
# #    path('/Library', views.index, name=''),
# #    path('/BUBT_Annex', views.index, name=''),
# #    path('/Alumni', views.index, name=''),
# #    path('/Constitution', views.index, name=''),
# #    path('/Committee', views.index, name=''),
# #    path('/Recent_Activities', views.index, name=''),
# #    path('/Alumni_Search', views.index, name=''),
#     path('/faq', faq.index, name='FAQ'),
# #    path('/Login', views.index, name=''),
#     path('/news', news.index, name='NEWS')
# CSE BUBT News
# Faculty List
# Consultation Services
# Training
# Industrial Affiliation
]