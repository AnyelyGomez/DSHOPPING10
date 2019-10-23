from django.db import models

# Create your models here.
class Category(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField('Title', max_length=150)
    description=models.TextField('Description')
    status=models.BooleanField(default=True)
    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'
    def __str__(self):
        return self.title

class Country(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField('Title', max_length=150)
    abbreviation=models.CharField('Abbreviation', max_length=150)
    status=models.BooleanField(default=True)
    class Meta:
        verbose_name='Country'
        verbose_name_plural='Contries'
    def __str__(self):
        return self.title
    
class product(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField('Title', max_length=150)
    description=models.TextField('Description')
    id_category=models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity=models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity=models.IntegerField('Quantity')
    status=models.BooleanField(default=True)
    class Meta:
        verbose_name='product'
        verbose_name_plural='Products'
    def __str__(self):
        return self.title