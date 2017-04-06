from __future__ import unicode_literals

from django.db import models

# Create your models here.


class StartupName(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    found_date = models.DateField('date')
    link = models.CharField(max_length=200)
    logo_url = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    startup = models.ForeignKey(StartupName, on_delete=models.CASCADE)
    industry = models.CharField(max_length=200)


class StartupContact(models.Model):
    startup = models.ForeignKey(StartupName, on_delete=models.CASCADE)
    contact = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    linkedIn = models.CharField(max_length=200)
    facebook = models.CharField(max_length=200)
    twitter = models.CharField(max_length=200)

    def __unicode__(self):
        return self.contact


class Founder(models.Model):
    name = models.CharField(max_length=200)
    startup = models.ForeignKey(StartupName, on_delete=models.CASCADE)
    img_url = models.CharField(max_length=200)
    linkedIn_link = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Funding(models.Model):
    investor = models.CharField(max_length=1000)
    amount_round = models.CharField(max_length=1000)
    funding_date = models.CharField(max_length=1000)
    startup = models.ForeignKey(StartupName, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.investor


class Invested(models.Model):
    startup = models.ForeignKey(StartupName, on_delete=models.CASCADE)
    invested_in = models.CharField(max_length=1000)
    invested_amount = models.CharField(max_length=1000)
    invested_date = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.startup


class News(models.Model):
    heading = models.CharField(max_length=200)
    content = models.CharField(max_length=500)
    pub_date = models.DateField('date')
    img_link = models.CharField(max_length=200)
    source = models.CharField(max_length=200)
    link = models.CharField(max_length=200)

    def __unicode__(self):
        return self.heading


class NewsCategory(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    startup = models.ForeignKey(StartupName, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.news


class Internship(models.Model):
    startup = models.ForeignKey(StartupName, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    apply_post = models.CharField(max_length=200)
    salary = models.CharField(max_length=100)
    start_date = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    source = models.CharField(max_length=200)

    def __unicode__(self):
        return self.startup.name
