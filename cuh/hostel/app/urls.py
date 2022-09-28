from app import views
from django.urls import path
from django.contrib.auth import views as auth_views
from app.forms import LoginForm, MyPasswordChangeForm
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('', views.home),
    # path('accounts/profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page = 'login'), name='logout'),
    path('register/', views.RegisterationView.as_view(), name='register'),
]  +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)