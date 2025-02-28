from django.db import models

CAT_CHOICES = {
    "RG": "Ring",
    "NL": "Necklace",
}

STONE_CHOICES = {
    "DI": "Diamond",
    "PR": "Pearl",
    "QZ": "Quartz",
    "TP": "Topaz",
    "SYN": "Synthetic"
}

METAL_CHOICES = {
    "GL": "Gold",
    "RG": "Rose Gold",
    "YG": "Yellow Gold",
    "WG": "White Gold",
    "SS": "Sterling Silver",
    "BRZ": "Bronze",
    "TIT": "Titanium"
}

CHAIN_LENGTH_CHOICES = {
    "16": "16 Inches",
    "18": "18 Inches",
    "20": "20 Inches",
    "22": "22 Inches",
    "24": "24 Inches",
    "26": "26 Inches",
    "28": "28 Inches",    
}

CHAIN_THICKNESS_CHOICES = {
    "1": "1mm",
    "2": "2mm",
    "3": "3mm",
    "4": "4mm",
    "5": "5mm",    
}

 
class Product(models.Model):
    category = models.CharField(max_length=50, null=True, choices=CAT_CHOICES)
    sku = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    stone_type = models.CharField(max_length=50, null=True, blank=True, choices=STONE_CHOICES)
    metal_type = models.CharField(max_length=50, null=True, blank=True, choices=METAL_CHOICES)
    chain_length = models.CharField(max_length=50, null=True, blank=True, choices=CHAIN_LENGTH_CHOICES)
    chain_thickness = models.CharField(max_length=50, null=True, blank=True, choices=CHAIN_THICKNESS_CHOICES)
    has_sizes = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.name