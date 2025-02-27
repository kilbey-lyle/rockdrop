from django.db import models

CAT_CHOICES = {
    "RG": "ring",
    "CF": "cuff",
    "NL": "necklace",
}

 
class Product(models.Model):
    category = models.CharField(max_length=50, null=True, choices=CAT_CHOICES)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.name