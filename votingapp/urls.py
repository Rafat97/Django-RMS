from django.urls import path, include
from .views import VoteAddView
# EmployApiView,
urlpatterns = [
    # path('create/', add_employ,name='creating-employ'),
    path('create/', VoteAddView.as_view(), name='adding-vote'),
]


# {
#   "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzNzM2MTcwMCwiaWF0IjoxNjM3Mjc1MzAwLCJqdGkiOiJkYzhmNTY0YjI0NTQ0MGIzODY4NGZkOTRmYjYzNjZlMSIsInVzZXJfaWQiOjJ9.6fsBR9C3fGptc4JsTVrWkj8FfRhhn6FjYtwcbCcq0PM",
#   "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM3Mjc4OTAwLCJpYXQiOjE2MzcyNzUzMDAsImp0aSI6IjZlYTBkY2EzMjNmMzQwMzRhNjI0ODQxY2IzYzY0YmQwIiwidXNlcl9pZCI6Mn0.p_Fh4Hsf_np2VJQD3ymjpLWovq8SiPHVohyBrhG-HoI"
# }

# {
#   "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzNzM2NTQ2MSwiaWF0IjoxNjM3Mjc5MDYxLCJqdGkiOiI3MzBhOTdiZmU0ZmQ0ZDc3YjVmZDNmZGM5ZGUxNTk1YiIsInVzZXJfaWQiOjJ9.DYzTWkR_SqXUGCSQ-1NzvIMAG9IIYhs1eA35hGQDxy0",
#   "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM3MjgyNjYxLCJpYXQiOjE2MzcyNzkwNjEsImp0aSI6IjE5MTkzMjBiZTI3YjRkYjQ4NDQyOWVjZmYzYjMyYjAyIiwidXNlcl9pZCI6Mn0.Wcm0H2NOaOMFpDcAEZJII0JLjPRUdFXdIGn3tTWfA6E"
# }
