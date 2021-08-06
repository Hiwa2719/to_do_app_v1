from django.db import models
from django.urls import reverse


class ToDo(models.Model):
    NEVER = 'NE'
    EVERY_DAY = 'ED'
    MONDAY_TO_FRIDAY = 'MF'
    EVERY_WEEK = 'EW'
    EVERY_MONTH = 'EM'
    EVERY_YEAR = 'EY'

    REPETITIONS = [
        (NEVER, 'Never'),
        (EVERY_DAY, 'Every day'),
        (MONDAY_TO_FRIDAY, 'Monday to Friday'),
        (EVERY_WEEK, 'Every week (Friday)'),
        (EVERY_MONTH, 'Every month (Same date)'),
        (EVERY_YEAR, 'Every year (Same date)')
    ]

    title = models.CharField(max_length=120)
    description = models.TextField()
    deadline = models.DateTimeField()
    repetition = models.CharField(max_length=2, choices=REPETITIONS, default=NEVER)
    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateField(auto_now=True)

    def __str__(self):
        return '{} on {}'.format(self.title, self.deadline.strftime('%d/%m/%Y %H:%M:%S'))

    def get_absolute_url(self):
        return reverse('basicapp:task-detail', kwargs={'pk': self.pk})
