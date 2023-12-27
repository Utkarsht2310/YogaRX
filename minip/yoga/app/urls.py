from django.urls import  path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from . forms import LoginForm

urlpatterns = [
    path('',views.home,name="home"),
    path('search/',views.search,name="search"),
    path('about/',views.about,name="about"),
     path('registration/' ,views.CustomerRegistrationView.as_view(), name='registraion'),
    path('accounts/login/', auth_view.LoginView.as_view(template_name = 'app/login.html',authentication_form=LoginForm),name='login'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)