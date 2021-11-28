from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Attendances(models.Model):
    # on_~: 参照しているobj削除時:該当のデータも削除
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    attendance_time = models.DateTimeField(default=datetime.now)
    leave_time = models.DateTimeField(null=True)
