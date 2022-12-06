from django.urls import path
from jobslist_app.api.views import *

urlpatterns = [
    path('contracts/', ContractListAV.as_view()),
    path('levels/', LevelListAV.as_view()),
    path('roles/', RoleListAV.as_view()),
    path('languages/', ProgrammingLanguagesListAV.as_view()),
    path('tools/', ToolsListAV.as_view()),
    path('locations/', LocationListAV.as_view()),
    path('jobs/', JobOfferListAV.as_view())

]
