"""
URL configuration for trussybridal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from django.urls import path
from collection1 import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gowns/', views.gowns, name='gowns'),
    path('party-dresses/', views.party_dresses, name='party_dresses'),
    path('wedding-videos/', views.wedding_videos, name='wedding_videos'),
    path('maids_dresses/', views.maids_dresses, name='maids_dresses'),
    path('about_us/', views.about_us, name='about_us'),
    path('search/', views.search, name='search'),

    # New: Gown detail page, expects integer id
    path('gowns/<int:gown_id>/', views.gown_detail, name='gown_detail'),
    path('gown/<int:gown_id>/<str:source>/', views.gown_detail, name='gown_detail_source'),
]

