from django.db import models

# Create your models here.
status=(
    ('pending','pending'),
    ('completed','completed')
)
class Todo(models.Model):
    Title=models.CharField(max_length=500)
    Description=models.TextField()
    Date=models.DateField(blank=True,auto_now_add=True)
    Time=models.TimeField(blank=True,auto_now_add=True)
    Status=models.CharField(max_length=400,choices=status,default="pending")
    User=models.CharField(max_length=500)
    
    def __str__(self):
        return self.Title
        
