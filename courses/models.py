from django.db import models
from datetime import datetime
from instructors.models import Instructor

class Course(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    duration = models.IntegerField()
    course_curriculum = models.TextField(blank=True)
    main_image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    next_batch_start_date = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=False)
    is_mvp = models.BooleanField(default=False)
    course_mode = models.CharField(max_length=50, default=False)

    def __str__(self):
        return self.title
    
