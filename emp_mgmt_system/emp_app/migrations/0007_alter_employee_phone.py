# Generated by Django 4.1.7 on 2023-03-14 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0006_alter_department_id_alter_employee_id_alter_role_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
