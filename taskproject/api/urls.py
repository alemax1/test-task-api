from django.urls import path

from api.views import GetSessionId, GetItemInfo

urlpatterns = [
    path('buy/<item_id>/', GetSessionId.as_view()),
    path('item/<item_id>/', GetItemInfo.as_view()),
]
