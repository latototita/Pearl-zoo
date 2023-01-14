from django.db import models

class Type(models.Model):
	name =models.CharField(max_length=100)
	def __str__(self):
		return self.name

class File(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='media/images',blank=True,null=True)
    file =models.FileField(upload_to='media/movies',blank=True,null=True)
    types=models.ForeignKey(Type,
                                on_delete=models.CASCADE)
    description=models.TextField(max_length=1000)
    download_link =models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return self.title

class SeriesName(models.Model):
	name =models.CharField(max_length=100)
	def __str__(self):
		return self.name

class Series(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='media/images',blank=True,null=True)
    file =models.FileField(upload_to='media/movies',blank=True,null=True)
    seriename=models.ForeignKey(SeriesName,
                                on_delete=models.CASCADE)
    types=models.ForeignKey(Type,
                                on_delete=models.CASCADE)                    
    description=models.TextField(max_length=1000)
    download_link =models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return self.title

