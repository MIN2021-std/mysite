"""
URL configuration for mysite project.

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
from django.contrib import admin
from django.urls import include, path
# include()함수는 다른 URLconf들을 참조할 수 있도록 도와준다.

urlpatterns = [
    path('polls/', include('polls.urls')), # 우리가 작성한 url
    path('admin/', admin.site.urls),
]

# 최상위 url conf에서 url를 파싱하고 받아서 
# path에 따른 앱으로 분기함


