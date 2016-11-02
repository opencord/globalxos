import os
import base64
from django.db.models import F, Q
from xos.config import Config
from core.models.image import Image
from xos.logger import observer_logger as logger
from synchronizers.base.syncstep import *

class SyncImages(SyncStep):
    provides=[Image]
    requested_interval=0
    observes=Image

    # We're not sync'ing sites with L-XOS
    # Just mark it as sync'ed
    def sync_record(self, image):
        image.backend_status = "0 - not sync'ed by globalxos"
        image.save()
