# Generated by Django 4.1.7 on 2023-04-11 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='studentapp.course'),
        ),
        migrations.AlterField(
            model_name='student',
            name='joining_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]