from django.db import models


class Technologies(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}({self.slug}'


class Projects(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    show_on_home = models.BooleanField(default=False)
    show_on_jewels = models.BooleanField(default=False)
    show_on_bootcamp = models.BooleanField(default=False)
    has_demo = models.BooleanField(default=False)
    github_link = models.CharField(max_length=256, blank=True)
    external_link = models.CharField(max_length=256, blank=True)
    image_name = models.CharField(max_length=256, blank=True)
    description = models.TextField(blank=True)
    the_ask = models.TextField(blank=True)
    challenges = models.TextField(blank=True)
    solution = models.TextField(blank=True)
    follow_up = models.TextField(blank=True)

    technologies = models.ManyToManyField(Technologies, related_name='projects')

    def __str__(self):
        return f'{self.name}({self.slug}'