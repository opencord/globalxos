import os
import base64
from django.db.models import F, Q
from xos.config import Config
from core.models.site import Site
from xos.logger import observer_logger as logger
from synchronizers.base.ansible import *
from synchronizers.base.syncstep import *

class SyncSites(SyncStep):
    provides=[Site]
    requested_interval=0
    observes=[Site]

    # We're not sync'ing sites with L-XOS
    # Just mark it as sync'ed
    def sync_record(self, site):
        site.backend_status = "0 - not sync'ed by globalxos"
        site.save()
