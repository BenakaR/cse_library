from django.urls import path
from . import views
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Other URL patterns
    path('', RedirectView.as_view(url='login/')),
    path('login/', views.login_user, name='login_user'),
    path('book/', views.books, name="books"),
    path('<int:id>', views.index, name='index'),
    # Other URL patterns
    path("logout/", views.logout_user, name='logout_user'),
    path('data/<int:usn_id>/user', views.data, name='data'),
    path('createuser/', views.createuser, name='createuser'),
]
