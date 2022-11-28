from django.db import models

# Create your models here.


class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Tools(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=50)
    # logo = models. NEED TO LEARN HOW TO ADD IMAGES

    def __str__(self):
        return self.name


class Location(models.Model):
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    is_remote = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.city}, {self.country}'


class JobOffer(models.Model):
    company = models.OneToOneField(
        Company, on_delete=models.CASCADE)
    is_new = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    position = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    level = models.CharField(max_length=30)
    posted_at = models.DateTimeField()
    contract = models.CharField(max_length=50)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    languages = models.ForeignKey(
        ProgrammingLanguage, on_delete=models.CASCADE, blank=True, null=True)
    # tools

    def __str__(self):
        return f'{self.role}, {self.company}'
