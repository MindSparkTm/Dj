from Dj.celery import celery_app
from .utils import parse_uploaded_file

@celery_app.task
def handle_uploaded_file(instance_id):
    parse_uploaded_file(instance_id)
