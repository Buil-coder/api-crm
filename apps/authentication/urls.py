from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    app_check_password_viewset,
    app_check_username_viewset,
    app_edit_password_viewset,
    app_register_client_viewset,
    auth_login_viewset,
    auth_register_staff_viewset,
    auth_register_client_viewset,
    auth_recovery_send_code_viewset,
    auth_recovery_check_code_viewset,
    auth_recovery_change_password_viewset,
    app_client_numberattempts_viewset,
    client_info_view,
    password_recovery_request_view,
    password_recovery_verify_view,
    delete_this
)

urlpatterns  = [
    path('login/',auth_login_viewset.as_view()),
    path('app/client/number_attempts/', app_client_numberattempts_viewset.as_view()),
    path('app/check_password/', app_check_password_viewset.as_view()),
    path('app/check_username/', app_check_username_viewset.as_view()),
    path('app/edit_password/', app_edit_password_viewset.as_view()),
    path('staff/register/',auth_register_staff_viewset.as_view()),
    path('panel/client/register/',auth_register_client_viewset.as_view()),
    path('app/client/register/',app_register_client_viewset.as_view()),
    path('panel/client/send_code/',auth_recovery_send_code_viewset.as_view()),
    path('panel/client/check_code/',auth_recovery_check_code_viewset.as_view()),
    path('panel/client/change_password/',auth_recovery_change_password_viewset.as_view()),
    path('panel/client/password_recovery/request/', password_recovery_request_view.as_view()),
    path('panel/client/password_recovery/verify/', password_recovery_verify_view.as_view()),
    path('panel/client/client_recovery/info/<str:client_id>/', client_info_view.as_view()),
    path('delete_this/', delete_this.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)