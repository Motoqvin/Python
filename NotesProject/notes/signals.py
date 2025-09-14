from django.db.models.signals import post_save
from django.dispatch import receiver
from models import Note, Tag

@receiver(post_save, sender=Note)
def add_untagged(sender, instance, created, **kwargs):
    if created and instance.tags.count() == 0:
        tag, _ = Tag.objects.get_or_create(slug='untagged', defaults={'name': 'untagged'})
        instance.tags.add(tag)