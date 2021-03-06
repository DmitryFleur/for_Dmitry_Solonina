"""library_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.conf.urls import url, include
from rest_framework_swagger.views import get_swagger_view
from library_django.views import ReturnStatistics

schema_view = get_swagger_view(title='Library API')

urlpatterns = [
    url(r'^api/', include('library_django.views')),
    url(r'^api/return_statistics', ReturnStatistics.as_view()),
    url(r'^$', schema_view)
]
