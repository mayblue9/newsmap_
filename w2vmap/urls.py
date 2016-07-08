from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
##add REST API
from rest_framework import routers
from quickstart import views
##
##


###add REST API
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)



urlpatterns = patterns(
    '',
    url(
        r'^photo/(?P<photo_id>\d+)/$',
        'photo.views.single_photo',
        name='view_single_photo'
    ),
    url(r'^photo/upload/$', 'photo.views.new_photo', name='new_photo'),
    url(r'^photo/$', 'photo.views.single_photo', name='view_single_photo'),
     url(r'^json/$', 'photo.views.as_json', name='as_json'),
    url(r'^admin/', include(admin.site.urls)),
    ##add REST API
    # Wire up our API using automatic URL routing.
    # Additionally, we include login URLs for the browseable API.
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
   # url(r'^word2vec/$', 'photo.views.word2vec', name='word2vec'),

    url(r'^search_form/$', 'photo.views.search_form1'),
    url(r'^search/$','photo.views.search', name= 'search1'),
    url(r'^search_an/$','photo.views.search_angular', name= 'search_an'),
    url(r'^crispy/$','photo.views.crispy', name= 'crispy1'),

    #url(r'^test/$', test_list),



)

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )



