from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('addcourse',views.addcourse,name='addcourse'),
    # path('addstudent',views.addstudent,name='addstudent'),
    path('add_course',views.add_course,name='add_course'),
    path('add_student',views.add_student,name='add_student'),
    path('add_studentdb',views.add_studentdb,name='add_studentdb'),
    path('show_student',views.show_student,name='show_student'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('editpage/<int:pk>',views.editpage,name='editpage'),
    path('deletepage/<int:pk>',views.deletepage,name='deletepage')


]
