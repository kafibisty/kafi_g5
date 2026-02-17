from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)    # পণ্যের নাম
    price = models.IntegerField()              # দাম (পূর্ণসংখ্যা)
    description = models.TextField()           # বিবরণ
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name