# Generated by Django 4.0.1 on 2022-05-02 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blogapp', '0006_alter_blog_genre'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportedPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(choices=[('spam', 'Spam'), ('scam', 'Scam'), ('misinformation', 'Misinformation'), ('hate_speech', 'Hate Speech'), ('inappropriate', 'Inappropriate'), ('other', 'Other')], default='spam', max_length=100)),
                ('elaboration', models.TextField(blank=True, null=True)),
                ('reports', models.IntegerField(default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('reported_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.blog')),
                ('reporter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Reported Post',
                'verbose_name_plural': 'Reported Posts',
                'ordering': ('-updated',),
                'unique_together': {('reported_post', 'reporter')},
            },
        ),
    ]