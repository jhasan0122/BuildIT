# Generated by Django 5.1.1 on 2024-09-23 03:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0005_post_exterior1st_post_exterior2nd"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="post_pic1",
            field=models.ImageField(default="empty.jpg", upload_to="post-pic1"),
        ),
        migrations.AddField(
            model_name="post",
            name="post_pic2",
            field=models.ImageField(default="empty.jpg", upload_to="post-pic2"),
        ),
        migrations.AddField(
            model_name="post",
            name="post_pic3",
            field=models.ImageField(default="empty.jpg", upload_to="post-pic3"),
        ),
        migrations.AddField(
            model_name="post",
            name="post_pic4",
            field=models.ImageField(default="empty.jpg", upload_to="post-pic4"),
        ),
        migrations.AddField(
            model_name="post",
            name="post_pic5",
            field=models.ImageField(default="empty.jpg", upload_to="post-pic5"),
        ),
        migrations.AddField(
            model_name="post",
            name="post_pic6",
            field=models.ImageField(default="empty.jpg", upload_to="post-pic6"),
        ),
    ]
