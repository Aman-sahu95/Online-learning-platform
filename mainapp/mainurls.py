from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('registration/',views.registration,name="registration"),
    path('adlogin/',views.adlogin,name="adlogin"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('org/',views.org,name="org"),
    path('cert/',views.cert,name="cert"),
    path('outreach/',views.outreach,name="outreach"),
    path('service/',views.service,name="service"),
    path('training/',views.training,name="training"),
    path('enquiry/',views.enquiry,name="enquiry"),
    path('ceo/',views.ceo,name="ceo"),
    path('error/',views.error,name="error"),
    path('viewenquiry/', views.viewenquiry, name='viewenquiry')
]