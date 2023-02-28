from django.db import models
import datetime
# Create your models here.
class Details(models.Model):
   end_year = models.IntegerField(blank=True, null=True)
   intensity=models.CharField(max_length=122)
   sector=models.CharField(max_length=122)
   topic=models.CharField(max_length=122)
   insight=models.CharField(max_length=122)
   url=models.URLField(blank=True)
   region=models.CharField(max_length=122)
   start_year = models.IntegerField(blank=True, null=True)
   impact=models.CharField(max_length=122)
   #added=models.DateTimeField()
   #published=models.DateTimeField()
   country=models.CharField(max_length=122)
   #relevance=models.IntegerField()
   pestle=models.CharField(max_length=122)
   source=models.CharField(max_length=122)
   title=models.TextField()
   likelihood=models.CharField(max_length=122)

