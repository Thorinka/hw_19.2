# Generated by Django 4.2.3 on 2023-07-22 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=150, verbose_name='заголовок')),
                ('slug', models.CharField(max_length=150, verbose_name='slug')),
                ('post', models.TextField(verbose_name='публикация')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('is_published', models.BooleanField(default=True, verbose_name='статус')),
                ('view_count', models.IntegerField(default=0, verbose_name='просмотры')),
            ],
        ),
    ]
