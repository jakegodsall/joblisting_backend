from rest_framework import serializers
from jobslist_app.models import *


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ['name']


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class ProgrammingLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgrammingLanguage
        fields = '__all__'


class ToolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tools
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class JobOfferSerializer(serializers.ModelSerializer):
    contract = ContractSerializer()
    level = LevelSerializer()
    role = RoleSerializer()
    languages = ProgrammingLanguageSerializer()
    tools = ToolsSerializer()
    company = CompanySerializer()
    location = LocationSerializer()

    class Meta:
        model = JobOffer
        fields = '__all__'
