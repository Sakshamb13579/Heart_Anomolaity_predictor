from django.db import models
from django.contrib.auth.models import User

# Create your models here.
yn = [('Y', 'Yes'), ('N', 'No')]
gender_choices = [('m', 'Male'), ('f', 'Female'), ('o', 'Other')]
blood_group_choices = [('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-'), ('RH+', 'RH+') ]
smoker_state = [('C', 'Current'), ('F', 'Former'), ('N', 'Never')]
often = [('R', 'Regularly'), ('S', 'Seldom'), ('N', 'Never')]


class UserHealthStats(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=1,choices=gender_choices)
    blood_group = models.CharField(max_length=3,choices=blood_group_choices)
    height = models.IntegerField()
    weight = models.IntegerField()
    smoker_status = models.CharField(max_length=1,choices=smoker_state)
    heart_rate = models.IntegerField()
    alcoholic = models.CharField(max_length=1,choices=yn)
    balenced_diet = models.CharField(max_length=1,choices=often)
    exercise = models.CharField(max_length=1,choices=often)
    pre_heart_cond = models.CharField(max_length=1,choices=yn)
    family_heart_cond = models.CharField(max_length=1,choices=yn)
    diabetic = models.CharField(max_length=1,choices=yn)
    blood_pressure = models.IntegerField()
    bp_hypert = models.CharField(max_length=1,choices=yn)
    hypert_treatment = models.CharField(max_length=1,choices=yn)
    asprin_treatment = models.CharField(max_length=1,choices=yn)
    lipid_level = models.IntegerField()
    statin = models.CharField(max_length=1,choices=yn)
    non_cardiac_ailment = models.CharField(max_length=1,choices=yn)
    non_cardiac_treatment = models.CharField(max_length=1,choices=yn)
    psychiatric_health_cond = models.CharField(max_length=1,choices=yn)

    sugar_level = models.CharField(max_length=3, blank=True, null=True)
    psychiatric_health_cond_name = models.CharField(max_length=50 ,blank=True)

    def __str__(self):
        return self.user.username