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
    city = models.CharField(max_length=50, blank=True, default='')
    country = models.CharField(max_length=50, blank=True, default='')
    is_remote = models.BooleanField(default=False)

    def __str__(self):
        if self.is_remote:
            return 'Remote'
        elif self.city.strip() == '' and self.country.strip() == '':
            return 'Worldwide'
        elif self.city.strip() == '':
            return self.country
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
    languages = models.ManyToManyField(
        ProgrammingLanguage)
    tools = models.ManyToManyField(Tools)

    def __str__(self):
        programming_langages = ', '.join(
            [lang.name for lang in self.languages.all()])
        return f'{self.role}, {self.company} ({programming_langages})'
