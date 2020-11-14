from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('create/',views.create,name='create'),
    path('check/',views.check,name="check"),
    path('modify/<int:question_id>/',views.modify,name="modify"),
    path('participate/<int:question_id>/',views.participate,name="participate"),
    path('results/<int:question_id>/',views.results,name ="result")


]