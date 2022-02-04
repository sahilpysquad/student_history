# Generated by Django 3.2.11 on 2022-02-03 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_delete_fileupload'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('media_file', models.FileField(upload_to='')),
                ('course', models.CharField(choices=[('BSC', 'Bachelor of Science (BSC)'), ('BE', 'Bachelor of Engineering (BE)'), ('BCA', 'Bachelor of Computer Applications (BCA)'), ('BPT', 'Bachelor of Physiotherapy (BPT)'), ('CCC', 'Course on Computer Concepts (CCC)'), ('BA', 'Bachelor of Arts (BA)'), ('BCOM', 'Bachelor of Commerce (BCOM)'), ('MBBS', 'Bachelor of Medicine (MBBS)')], default='BE', max_length=5)),
            ],
        ),
    ]
