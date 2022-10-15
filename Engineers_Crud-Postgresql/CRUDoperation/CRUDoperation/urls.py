"""CRUDoperation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from . import views 

app_name = 'CRUDoperation'

urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('edit/<int:engineer_id>', views.Editeng, name="Editeng"),
    path('update/<int:engineer_id>', views.updateeng, name="updateeng"),
    


    path('', views.index, name = 'index'),
    path('cadmin/landing/', views.adminView, name='adminView'),
    path('cadmin/landing/<str:pk>/mips/', views.mipView, name='mipView'),
    path('cadmin/landing/<str:pk>/mips/<str:lpk>/steps/', views.stepView, name='stepView'),
    path('cadmin/landing/miplist/', views.mipList, name='mipList'),
    path('cadmin/landing/pathlist/', views.pathList, name='pathList'),
    path('cadmin/landing/edit/<int:engineer_id>', views.Editeng, name="Editeng"),
    path('cadmin/landing/miplist/delMip/<str:pk>', views.delMip, name='delMip'),
    path('cadmin/landing/miplist/delMip/', views.delMip, name='delMip'),
    path('cadmin/landing/miplist/delMip', views.delMip, name='delMip'),
    path('cadmin/landing/pathlist/delPath/<str:pk>', views.delPath, name='delPath'),
    path('createEngineerLearningPath/<str:pk>',views.createEngLearningPath,name='createEngLearningPath'),
    path('createEngineerLearningPath/<str:pk>',views.createEngLearningPath,name='createEngLearningPath'),
    path('createEngineerLearningPathStep/<str:pk>',views.createEngineerLearningPathStep, name='createEngineerLearningPathStep'),
    path('cadmin/landing/stepList/', views.stepList, name='steplist'),
    path('cadmin/landing/stepList/delStep/<str:pk>', views.delStep, name='delStep'),
]
