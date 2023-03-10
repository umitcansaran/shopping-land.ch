# Generated by Django 4.1.3 on 2023-01-12 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0005_remove_profile_category_remove_profile_description_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="category",
            field=models.ManyToManyField(
                blank=True, null=True, related_name="profile", to="base.productcategory"
            ),
        ),
        migrations.AddField(
            model_name="profile",
            name="description",
            field=models.TextField(
                blank=True, null=True, verbose_name="profile description"
            ),
        ),
        migrations.AddField(
            model_name="profile",
            name="founded",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="headquarter",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="image",
            field=models.ImageField(
                blank=True, default="/no-image.jpeg", null=True, upload_to="store"
            ),
        ),
        migrations.AddField(
            model_name="profile",
            name="industry",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="website",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
