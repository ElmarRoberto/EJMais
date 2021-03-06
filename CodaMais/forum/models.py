'''
    Copyright (C) 2017, CodaMais.
    License: GNU General Public License v3.0, see LICENSE.txt
    App: forum
    File: models.py
    Contains all classes related to the forum, it is django's default to keep all models in single file.
'''

# Django.
from django.db import models
from datetime import datetime

# local Django.
from forum import constants
from user.models import User


# Class: Topic
# The class represents a topic in the site forum.
class Topic(models.Model):
    title = models.CharField(max_length=constants.MAX_LENGTH_TITLE)
    subtitle = models.CharField(max_length=constants.MAX_LENGTH_SUBTITLE, null=True, blank=True)
    author = models.ForeignKey(
          User,
          on_delete=models.CASCADE,)
    description = models.CharField(max_length=constants.MAX_LENGTH_TOPIC_DESCRIPTION)
    date_topic = models.DateTimeField(auto_now_add=True, blank=True)
    planned_date = models.CharField(max_length=255,null=True)
    delivery_date = models.DateTimeField(null=True, blank=True)
    best_answer = models.ForeignKey('Answer', models.SET_NULL, related_name='best_answer', null=True)
    locked = models.BooleanField(default=False)
    complexity = models.CharField(max_length=255, choices=constants.COMPLEXITIES)
    completed = models.BooleanField(default=False)

    def new_topics():
        topics = Topic.objects.all().order_by('-id')[:5]
        return topics

    def answers(self):
        assert self is not None, "Topic not exists."
        # Getting all current topic answers except the best answer
        answers = Answer.objects.filter(topic=self)
        return answers

    @property
    def is_delayed(self):
        planned_date = datetime.strptime(self.planned_date, '%Y-%m-%dT%H:%M')
        return planned_date < self.delivery_date

    @property
    def display_planned_date(self):
        planned_date = datetime.strptime(self.planned_date, '%Y-%m-%dT%H:%M')
        return planned_date


    def __str__(self):
        return self.title


# Class: Answer
# The class represents a answer to a topic in the site forum.
class Answer(models.Model):
    description = models.CharField(max_length=constants.MAX_LENGTH_ANSWER_DESCRIPTION)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,)
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,)
    date_answer = models.DateTimeField(auto_now_add=True, blank=True)

    def creates_answer(self, user, topic, description):
        self.user = user
        self.topic = topic
        self.description = description
        self.save()

    def __str__(self):
        return self.description
