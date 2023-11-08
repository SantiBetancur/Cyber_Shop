from django.db import models

# Create your models here.

class Project(models.Model):
    # Create the fields
    name = models.CharField(max_length = 45)# VARCHAR(45)
    def __str__(self):
        return self.name
    

class Task(models.Model):
    title = models.CharField(max_length = 45)   
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete = models.CASCADE) #On_delete is for delete all ocurrences if any project is deleted

    def __str__(self):
        return self.project.name + " -> " + self.title

