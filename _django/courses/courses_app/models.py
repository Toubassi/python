from django.db import models

# Create your models here.
class CourseManager(models.Manager):
  def basic_validator(self, postData):
    errors = {}

    course = postData.get('the_course', '').strip()
    desc = postData.get('the_description', '').strip()

    if len(course) < 5:
      errors['course'] = "Course title must be at least 5 characters long."
    if len(desc) < 15:
      errors['desc'] = "Coure details should be at least 15 characters long."
    return errors
      

class Course(models.Model):
  the_course = models.CharField(max_length=255)
  objects = CourseManager()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Description(models.Model):
  the_description = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  course = models.OneToOneField(Course, on_delete=models.CASCADE, related_name="description")