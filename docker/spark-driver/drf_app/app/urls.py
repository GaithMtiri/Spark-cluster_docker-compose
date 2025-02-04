


from django.conf.urls import include, url
from rest_framework import routers
from app.services import views

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)
router.register(r'pie', views.PieViewSet, base_name='pie')
router.register(r'calc', views.CalWordViewSet, base_name='calcWord')
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    url('', include(router.urls)),
    url('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
