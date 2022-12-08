from rest_framework.viewsets import ModelViewSet

from jobslist_app.models import Contract
from jobslist_app.api.serializers import *


class ContractView(ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer


class LevelView(ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class RoleView(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class ProgrammingLanguageView(ModelViewSet):
    queryset = ProgrammingLanguage.objects.all()
    serializer_class = ProgrammingLanguageSerializer


class ToolView(ModelViewSet):
    queryset = Tool.objects.all()
    serializer_class = ToolsSerializer


class CompanyView(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class LocationView(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class JobOfferView(ModelViewSet):
    queryset = JobOffer.objects.all()
    serializer_class = JobOfferSerializer
