from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        db_table = 'category'


    def __str__(self):
        return self.name


class Articles(models.Model):
    title = models.CharField(max_length=256, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='default/', blank=True, null=True, default='not_available.png')

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


    class Meta:
        db_table = 'articles'

    def __str__(self):
        return self.title