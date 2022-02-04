from django.urls import path
from . import views

urlpatterns = [
    path('',views.ApiRoot.as_view(), name = views.ApiRoot.name),

    path('create/',views.CreatePermitView.as_view(), name = 'create_permit'),
    path("list/",views.ListPermitView.as_view(), name = 'list_permit'),
    path("update/<int:pk>/",views.UpdatePermitView.as_view(), name = 'update_permit'),
    path("delete/<int:pk>/",views.DeletePermitView.as_view(), name = 'delete_permit'),

    path("create-activity/",views.CreateExamplePermitView.as_view(), name = "create_activity"),
    path("list-activity/",views.ListExamplePermitView.as_view(), name = "list_activity"),
    path("update-activity/<int:pk>/",views.UpdateExamplePermitView.as_view()),
    path("delete-activity/<int:pk>/",views.DeleteExamplePermitView.as_view())
]