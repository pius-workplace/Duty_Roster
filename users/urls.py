from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, RoleViewSet, StaffViewSet, ShiftViewSet, RosterViewSet, AttendanceViewSet, NotificationViewSet, user_info
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'staff', StaffViewSet)
router.register(r'shifts', ShiftViewSet)
router.register(r'rosters', RosterViewSet)
router.register(r'attendances', AttendanceViewSet)
router.register(r'notifications', NotificationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user-info/', user_info, name='user_info'),
]
