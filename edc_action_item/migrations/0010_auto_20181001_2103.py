# Generated by Django 2.1 on 2018-10-01 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edc_action_item', '0009_auto_20180927_0306'),
    ]

    operations = [
        migrations.AddField(
            model_name='reference',
            name='action_item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='edc_action_item.ActionItem'),
        ),
        migrations.AlterField(
            model_name='reference',
            name='parent_reference_identifier',
            field=models.CharField(help_text='action identifier that links to parent reference model instance.', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='reference',
            name='related_reference_identifier',
            field=models.CharField(help_text='action identifier that links to related reference model instance.', max_length=30, null=True),
        ),
    ]
