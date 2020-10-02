from django.db import models

# Create your models here.

JOB_CHOICES = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
)

class Job(models.Model):
    title         = models.CharField(max_length=100)
    # location
    job_type      = models.CharField(choices = JOB_CHOICES, max_length=20)
    description   = models.TextField(max_length=2000)
    published_At  = models.DateTimeField(auto_now=True)
    positions_num = models.IntegerField(default=1)
    salary        = models.IntegerField(default=0)
    experience    = models.IntegerField(default=1)
    category      = models.ForeignKey('Category', on_delete = models.CASCADE)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
