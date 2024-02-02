from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Option(MPTTModel):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=100, null=True, blank=True)
    active = models.BooleanField(default=False)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return f'{self.name}, {self.link}'
