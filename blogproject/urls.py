from django.contrib import admin
from django.urls import path, include
import blogapp.views
import portfolio.views
import accounts.views
from django.conf import settings
from django.conf.urls.static import static #습관처럼 외우래.... 나도잘 몰라 ㅜ

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blogapp.urls')),
    path('accounts/', include('accounts.urls')),
    path('', blogapp.views.home, name="home"),
    path('portfolio/', portfolio.views.portfolio, name="portfolio"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #지금으로써는 외우는게 좋다. 
# or
# urlpattenrns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)