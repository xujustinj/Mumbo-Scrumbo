from django.urls import path
from .views import user_current, user_list, create_user
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('signup/', create_user),
    path('me/', user_current),
    path('all/', user_list),
]
