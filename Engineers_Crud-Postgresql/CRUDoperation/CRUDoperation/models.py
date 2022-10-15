from unicodedata import name
from django.db import models

class Engineers(models.Model):
    engineer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'engineers'

    def __str__(self):
        return self.name

class Mips(models.Model):
    mip_id = models.AutoField(primary_key=True)
    mip_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'mips'

    def __str__(self):
        return self.mip_name
  

class Learningpaths(models.Model):
    learningpath_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=150)
    mip = models.ForeignKey('Mips', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'learningpaths'
    
    def __str__(self):
        return self.description


class Learningpathsteps(models.Model):
    lp_step_id = models.AutoField(primary_key=True)
    learningpath = models.ForeignKey(Learningpaths, models.DO_NOTHING)
    name = models.CharField(max_length=150)
    
    class Meta:
        managed = False
        db_table = 'learningpathsteps'  
    
    def __str__(self):
        return self.name

class EngineerLearningPaths(models.Model):
    englp_id = models.AutoField(primary_key=True)
    engineer = models.ForeignKey('Engineers', models.DO_NOTHING)
    learningpath = models.ForeignKey('Learningpaths', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'engineer_learning_paths'
    
    def __str__(self):
        return self.learningpath.description

class Lpstepcompletions(models.Model):
    engineer = models.ForeignKey(Engineers, models.DO_NOTHING)
    lp_step = models.ForeignKey(Learningpathsteps, models.DO_NOTHING)
    completed = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'lpstepcompletions'

class EngineerAcccreditations(models.Model):
    engineer = models.ForeignKey('Engineers', models.DO_NOTHING)
    mip = models.ForeignKey('Mips', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'engineer_acccreditations'
        
class EngineerLearningPathSteps(models.Model):
    englpstep_id = models.AutoField(primary_key=True)
    engineer = models.ForeignKey(Engineers, null = True, on_delete=models.CASCADE)
    lp_step = models.ForeignKey(Learningpathsteps, null = True, on_delete=models.CASCADE)
    completed = models.BooleanField(db_index=True ,default=False)
    name = (str(engineer) + " : " + str(lp_step))
    class Meta:
        db_table = "lpstepcompletions"
        #ordering = ("engineer","lp_step")
    def __str__(self):
        return self.lp_step.name