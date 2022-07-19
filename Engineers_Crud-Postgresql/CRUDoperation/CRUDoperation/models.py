from unicodedata import name
from django.db import models

class engineers(models.Model):
    engineer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    class Meta:
        db_table = "engineers" 