from django.db import models


class Technology(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}({self.slug}'


class Image(models.Model):
    name = models.CharField(max_length=256, help_text='Enter the FULL name of the file')
    is_video = models.BooleanField(default=False)
    caption = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, help_text='use_underscores')
    has_demo = models.BooleanField(default=False)
    demo_link = models.CharField(max_length=256, blank=True, help_text='Leave blank for default demo path')
    github_link = models.CharField(max_length=256, blank=True)
    external_link = models.CharField(max_length=256, blank=True)
    image_name = models.CharField(max_length=256, blank=True)
    description = models.TextField(blank=True, help_text='This text will appear in project listings as well as the page for this project')
    the_ask = models.TextField(blank=True)
    challenges = models.TextField(blank=True)
    solution = models.TextField(blank=True)
    follow_up = models.TextField(blank=True)

    technologies = models.ManyToManyField(Technology, related_name='project')
    images = models.ManyToManyField(Image, related_name='project', blank=True)

    def __str__(self):
        return f'{self.name}({self.slug}'


class Page(models.Model):
    name = models.CharField(max_length=30)
    is_home = models.BooleanField(default=False)
    description = models.TextField(blank=True)

    projects = models.ManyToManyField(Project, related_name='page')

    def __str__(self):
        return self.name



