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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('gowns/', views.gowns, name='gowns'),   # 👈 put back the gowns list view
    path('party-dresses/', views.party_dresses, name='party_dresses'),
    path('maids-dresses/', views.maids_dresses, name='maids_dresses'),
    path('wedding-videos/', views.wedding_videos, name='wedding_videos'),
    path('about_us/', views.about_us, name='about_us'),
    path('search/', views.search, name='search'),

    # Detail views
    path('gowns/<int:gown_id>/', views.gown_detail, name='gown_detail'),
    path('gown/<int:gown_id>/<str:source>/', views.gown_detail, name='gown_detail_source'),
    
  # Add these for new categories
    path('casual/', views.casual, name='casual'),
    path('shoes/', views.shoes, name='shoes'),
    path('bags/', views.bags, name='bags'),
    path('lingeries/', views.lingeries, name='lingeries'),
    path('jewelry/', views.jewelry, name='jewelry'),  
     path('traditional/', views.traditional_clothes, name='traditional_clothes'),

    
]

# ✅ Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
