from django.db import models

# Create your models here.


class Contract(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Level(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


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
    logo = models.FileField(upload_to="company-logos", null=True)

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
            return self.country + ' only'
        return f'{self.city}, {self.country}'


class JobOffer(models.Model):
    company = models.OneToOneField(
        Company, on_delete=models.CASCADE)
    is_new = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    position = models.CharField(max_length=100)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    posted_at = models.DateTimeField()
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    languages = models.ManyToManyField(
        ProgrammingLanguage)
    tools = models.ManyToManyField(Tools, blank=True)

    def __str__(self):
        programming_langages = ', '.join(
            [lang.name for lang in self.languages.all()])
        return f'{self.role}, {self.company} ({programming_langages})'
