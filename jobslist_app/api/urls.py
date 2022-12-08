from django.urls import path

from rest_framework.routers import SimpleRouter

from jobslist_app.api.views import *

router = SimpleRouter(trailing_slash=False)

router.register('contract/', ContractView, basename='contract')
router.register('level/', LevelView, basename='level')
router.register('role/', RoleView, basename='role')
router.register('programming-language/', ProgrammingLanguageView,
                basename='programminglanguage')
router.register('tool/', ToolView, basename='tool')
router.register('company/', CompanyView, basename='company')
router.register('location/', LocationView, basename='location')
router.register('joboffer/', JobOfferView, basename='joboffer')

urlpatterns = router.urls
