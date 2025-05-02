from djongo import models

class Product(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    category = models.CharField(max_length=50)
    tags = models.TextField(blank=True)  # Store tags as comma-separated text

    def __str__(self):
        return self.name