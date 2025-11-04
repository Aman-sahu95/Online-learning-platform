from django.urls import path
from .import views


urlpatterns =[
    path('',views.parent,name='parent'),
    path('stuhome/',views.stuhome,name='stuhome'),
    path('stunews/',views.stunews,name='stunews'),
    path('stustudy/',views.stustudy,name='stustudy'),
    path('stufeedback/',views.stufeedback,name='stufeedback'),
    path('viewfeedback/',views.viewfeedback,name='viewfeedback'),
]
