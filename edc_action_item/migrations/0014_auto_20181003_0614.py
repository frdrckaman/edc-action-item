# Generated by Django 2.1 on 2018-10-03 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edc_action_item', '0013_auto_20181002_0411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actionitem',
            name='parent_action_item',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='edc_action_item.ActionItem'),
        ),
    ]
