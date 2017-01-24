import os
import base64
from django.db.models import F, Q
from xos.config import Config
from core.models.role import Role
from core.models.site import SiteRole, Controller, ControllerRole
from core.models.slice import SliceRole
from xos.logger import observer_logger as logger
from synchronizers.base.ansible_helper import *
from synchronizers.base.syncstep import *

class SyncRoles(SyncStep):
    provides=[Role]
    requested_interval=0
    observes=[SiteRole,SliceRole,ControllerRole]

    def sync_record(self, role):
        if not role.enacted:
            controllers = Controller.objects.all()
            """
       	    for controller in controllers:
                driver = self.driver.admin_driver(controller=controller)
                driver.create_role(role.role)
            """
            role.save()
    
