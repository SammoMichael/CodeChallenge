from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()

    def __str__(self):
        return self.title

class Company(models.Model):
    company_id = models.IntegerField(primary_key=True) 
    fractal_index = models.FloatField()

class Candidate(models.Model):
    candidate_id = models.IntegerField(primary_key=True)
    communication_score = models.IntegerField()
    coding_score = models.IntegerField()
    title = models.CharField(max_length=30)
    company_id = models.ForeignKey(
        Company, on_delete=models.CASCADE)