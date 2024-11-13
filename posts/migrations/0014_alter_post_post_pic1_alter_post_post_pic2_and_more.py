# Generated by Django 5.1.1 on 2024-11-07 14:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0013_alter_post_post_pic1_alter_post_post_pic2_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="post_pic1",
            field=models.FileField(
                blank=True, default="empty.jpg", null=True, upload_to="post-pic1/"
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="post_pic2",
            field=models.FileField(
                blank=True, default="empty.jpg", null=True, upload_to="post-pic2/"
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="post_pic3",
            field=models.FileField(
                blank=True, default="empty.jpg", null=True, upload_to="post-pic3/"
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="post_pic4",
            field=models.FileField(
                blank=True, default="empty.jpg", null=True, upload_to="post-pic4/"
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="post_pic5",
            field=models.FileField(
                blank=True, default="empty.jpg", null=True, upload_to="post-pic5/"
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="post_pic6",
            field=models.FileField(
                blank=True, default="empty.jpg", null=True, upload_to="post-pic6/"
            ),
        ),
    ]