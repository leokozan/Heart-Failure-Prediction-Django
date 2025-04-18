from django.db import models

class CoracaoModel(models.Model):
    id = models.AutoField(primary_key=True)
    age = models.IntegerField(max_length=10)
    sex = models.CharField(max_length=10)
    exercise_angina = models.CharField(max_length=10)
    chest_pain_type = models.TextField(max_length=10)
    st_slope = models.TextField()
    resting_ecg = models.TextField()
    resting_bp = models.IntegerField()
    cholesterol = models.IntegerField()
    fastingBS = models.CharField(max_length=10)
    max_hr = models.IntegerField()
    oldpeak = models.FloatField()
    heart_disease = models.CharField(max_length=10)

    class Meta:
        db_table = 'coracao'