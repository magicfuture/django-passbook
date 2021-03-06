from django.db import models


class Pass(models.Model):
    """
    Pass instance
    """
    pass_type_identifier = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=50)
    authentication_token = models.CharField(max_length=50)
    data = models.FileField(upload_to='passes')
    updated_at = models.DateTimeField()

    def __unicode__(self):
        return self.serial_number


class Registration(models.Model):
    """
    Registration of a Pass on a device
    """
    device_library_identifier = models.CharField(max_length=50)
    push_token = models.CharField(max_length=50)
    pazz = models.ForeignKey(Pass)

    def __unicode__(self):
        return self.device_library_identifier


class Log(models.Model):
    """
    Log message sent by a device
    """
    message = models.TextField()

    def __unicode__(self):
        return self.message
