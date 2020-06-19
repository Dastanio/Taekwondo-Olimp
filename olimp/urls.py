from django.urls import path
from . import views

urlpatterns = [
	path('', views.main, name = 'main'),
	path('about/', views.about, name = 'about'),
	path('email/', views.email, name = 'email'),
	path('gallery/', views.gallery, name = 'gallery'),
	path('kyrgyzstan/', views.kyrgyzstan, name = 'kyrgyzstan'),
]