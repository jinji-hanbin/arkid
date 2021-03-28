from django.db import models
from django.apps import AppConfig
from common.model import BaseModel
from inventory.models import User
from tenant.models import Tenant


class GiteeAppConfig(AppConfig):

    name = "gitee"


class GiteeUser(BaseModel):
    class meta:

        app_label = "gitee"

    tenant = models.ForeignKey(Tenant, on_delete=models.PROTECT)
    user = models.OneToOneField(
        User, verbose_name="用户", related_name="gitee_user", on_delete=models.PROTECT
    )
    gitee_user_id = models.CharField(
        max_length=255, blank=True, verbose_name="Gitee ID"
    )