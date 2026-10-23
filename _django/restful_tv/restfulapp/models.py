from django.db import models

# Create your models here.
class ShowManager(models.Manager):
  def basic_validator(self, postData):
    errors = {}

    title = postData.get('title', '').strip()
    network = postData.get('network', '').strip()
    desc = postData.get('desc', '').strip()

    if len(title) < 2:
      errors['title'] = "Title of the show ,ust be at least 2 characters long"
    if len(network) < 2:
      errors['network'] = "The name of the network should be at least 3 characters long"
    if len(desc) < 4:
      errors['desc'] = "the description should be at least 5 characters long"
    return errors
  
class Tv_Show(models.Model):
  title = models.CharField(max_length=255)
  network = models.CharField(max_length=255)
  release_date = models.DateField()
  desc = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = ShowManager()
