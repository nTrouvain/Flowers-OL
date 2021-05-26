from django.db import models
from manager_app.models import ParticipantProfile, ExperimentSession, Study
import uuid


class Question(models.Model):
    instrument = models.CharField(max_length=100, null=True)
    component = models.CharField(max_length=100, null=True)
    group = models.CharField(max_length=50, null=True, blank=True)
    handle = models.CharField(max_length=50, null=True, unique=True)
    order = models.IntegerField(null=True, blank=True)
    prompt = models.CharField(max_length=300, null=True)
    reverse = models.BooleanField(null=True, blank=True)
    min_val = models.IntegerField(null=True, blank=True)
    max_val = models.IntegerField(null=True, blank=True)
    step = models.IntegerField(null=True, blank=True)
    annotations = models.CharField(max_length=200, null=True)
    type = models.CharField(max_length=30, null=True)
    widget = models.CharField(max_length=30, null=True)
    help_text = models.CharField(max_length=200, null=True, blank=True)
    validate = models.CharField(max_length=200, default='', blank=True)
    initial = models.CharField(max_length=200, default='', blank=True)

    def __unicode__(self):
        return self.handle

    def __str__(self):
        return self.__unicode__()


class Answer(models.Model):
    participant = models.ForeignKey(ParticipantProfile, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    session = models.ForeignKey(ExperimentSession, null=True, on_delete=models.DO_NOTHING)
    value = models.CharField(null=True, max_length=100)
    study = models.ForeignKey(Study, null=True, on_delete=models.CASCADE)
    # study = ParticipantProfile.objects.values_list('study')