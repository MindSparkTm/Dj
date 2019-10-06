from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Book,FileUpload
from .utils import parse_uploaded_file
from .tasks import handle_uploaded_file

@receiver(post_save, sender=FileUpload)
def test_signal(sender, instance, created, **kwargs):
    handle_uploaded_file.delay(instance.id)
