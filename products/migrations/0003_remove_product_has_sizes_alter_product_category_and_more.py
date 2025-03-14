# Generated by Django 5.1.6 on 2025-03-01 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_chain_length_product_chain_thickness_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='has_sizes',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('RG', 'Ring'), ('NL', 'Necklace')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='chain_length',
            field=models.CharField(blank=True, choices=[('16', '16 Inches'), ('18', '18 Inches'), ('20', '20 Inches'), ('22', '22 Inches'), ('24', '24 Inches'), ('26', '26 Inches'), ('28', '28 Inches')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='chain_thickness',
            field=models.CharField(blank=True, choices=[('1', '1mm'), ('2', '2mm'), ('3', '3mm'), ('4', '4mm'), ('5', '5mm')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='metal_type',
            field=models.CharField(blank=True, choices=[('GL', 'Gold'), ('RG', 'Rose Gold'), ('YG', 'Yellow Gold'), ('WG', 'White Gold'), ('SS', 'Sterling Silver'), ('BRZ', 'Bronze'), ('TIT', 'Titanium')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='stone_type',
            field=models.CharField(blank=True, choices=[('DI', 'Diamond'), ('PR', 'Pearl'), ('QZ', 'Quartz'), ('TP', 'Topaz'), ('SYN', 'Synthetic')], max_length=50, null=True),
        ),
    ]
