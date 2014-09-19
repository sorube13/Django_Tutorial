from django.db import models

class List(models.Model):
	list_name = models.CharField(max_length=200)
	def __str__(self):
		return self.list_name

class Task(models.Model):
	list_set = models.ForeignKey(List)
	task_name = models.CharField(max_length=200)
	task_date = models.DateTimeField('date published')
	def __str__(self):
		return self.task_name