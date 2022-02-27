from django.urls import path

from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('hospital_login', LoginView.as_view(template_name='hospital/hospital_login.html'), name='hospital_login'),
    path('hospital_signup', views.hospital_signup_view, name='hospital-signup'),
    path('hospital_dashboard', views.hospital_dashboard_view, name='hospital-dashboard'),
    path('make-request', views.make_request_view, name='make-request'),
    path('my-request', views.my_request_view, name='my-request'),
]
