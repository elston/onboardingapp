
from django.db import models


class Organization(models.Model):
    # ...
    name = models.CharField(
        max_length=255)
    description = models.TextField(
        blank=True)
    owner = models.ForeignKey(
        'team.TeamUser',
            related_name='organizations')
    team = models.ManyToManyField(
        'team.Team', 
            related_name='organizations', 
                blank=True)

    def __str__(self):
        return self.name
