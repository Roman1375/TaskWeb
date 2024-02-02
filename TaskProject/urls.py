from django.contrib import admin
from django.urls import path, include, re_path
from mainApp import views
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),
]


urlpatterns += i18n_patterns(
    path('', views.index, name='index'),
    path('<str:page_link>/', views.pages, name='page'),
    path('<str:page_link>/<str:sub_page_link>', views.sub_pages, name='sub_page'),
)


if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]
