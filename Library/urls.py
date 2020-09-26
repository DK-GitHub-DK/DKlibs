"""Library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from user import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.browse, name='browse'),
    path('bookinfo/<str:pk>/', views.bookinfo, name='bookinfo'),
    path('signup/', views.signup, name = 'signup'),
    path('signin/', views.signin, name = 'signin'),
    path('signout/', views.signout, name = 'signout'),
    path('mybooks/', views.mybooks, name = 'mybooks'),
    path('orderbook/<str:pk>', views.orderbook, name = 'orderbook'),
    path('returnbook/<str:pk>/', views.returnbook, name = 'returnbook'),
    path('returnconfirm/<str:pk>', views.returnconfirm, name = 'returnconfirm'),
    path('chores/', views.chores, name = 'chores'),
    path('userinfo/<str:pk>/', views.userinfo, name='userinfo'),
    path('deliverconfirm/<str:pk>', views.deliverconfirm, name = 'deliverconfirm'),
    path('deliver/<str:pk>', views.deliver, name = 'deliver'),
    path('returns/<str:pk>', views.returns, name = 'returns'),
    path('activity/<str:pk>', views.activity, name = 'activity'),
    path('pay/<str:pk>', views.pay, name = 'pay')
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
