"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from django.contrib import admin
# from django.urls import path
# from . import views

# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("home/", views.home),
#     path("index/", views.index),
#     path("about/", views.about),
#     path("contact/", views.contact),
#     path("data/", views.data_render),

# ]
# from django.contrib import admin

# from django.contrib import admin
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # path('', views.home, name='home'),  # Default home page
#     path('index/', views.index, name='index'),
#     path('about/', views.about, name='about'),
#     path('contact/', views.contact, name='contact'),
#     path('data/', views.data_render, name='data'),
#     path('country-selection/', views.country_selection, name='country_selection'),
#     path('student/<int:student_id>/', views.student_detail, name='student_detail'),
# ]

from django.contrib import admin
from django.urls import path, include
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Root URL
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('data/', views.data_render, name='data'),
    path('country-selection/', views.country_selection, name='country_selection'),
    path('student/<int:student_id>/', views.student_detail, name='student_detail'),
    path('myapp/', include('myapp.urls')),
]
