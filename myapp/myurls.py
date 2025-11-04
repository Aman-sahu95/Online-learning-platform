from django.urls import path
from myapp import views

urlpatterns = [
    # path('',views.index,name='index'),
    path('',views.adhome,name='adhome'),
    path('adnews/',views.adnews,name="adnews"),
    path('adbranch/',views.adbranch,name="adbranch"),
    path('adcourse/',views.adcourse,name="adcourse"),
    path('adsession/',views.adsession,name="adsession"),
    path('adstudy/',views.adstudy,name="adstudy"),
    path('viewstudy/',views.viewstudy,name="viewstudy"),
    path('adstu/',views.adstu,name="adstu"),
    path('editbranch/<id>',views.editbranch,name="editbranch"),
    path('editcourse/<id>',views.editcourse,name="editcourse"),
    path('editsession/<id>',views.editsession,name="editsession"),
    path('editnews/<id>',views.editnews,name="editnews"),
    path('deletebranch/<id>',views.deletebranch,name="deletebranch"),
    path('deletecourse/<id>',views.deletecourse,name="deletecourse"),
    path('deletesession/<id>',views.deletesession,name="deletesession"),
    path('deletenews/<id>',views.deletenews,name="deletenews"),
    path('adstudy/',views.adstudy,name="adstudy"),
    path('editstudy/<id>',views.editstudy,name="editstudy"),
    path('deletestudy/<id>',views.deletestudy,name="deletestudy"),
    
]