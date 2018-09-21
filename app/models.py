from django.contrib.auth.models import User
from django.db import models

class UserLocation(models.Model):
    """Represents a geographic location for a user at a point in time"""
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False)
    # Per https://stackoverflow.com/a/16743805
    # latitude is [-90, +90], longitude is [-180, +180]
    # six decimal places is 10 cm distance for latitude and longitude at the equator (and less at the poles)
    latitude = models.DecimalField(null=False, decimal_places=6, max_digits=8)
    longitude = models.DecimalField(null=False, decimal_places=6, max_digits=9)
    timestamp = models.DateTimeField(null=False, auto_now=True)

    def __str__(self):
        return "{user_name} at {latitude},{longitude} since {timestamp}".format(
            user_name=self.user.user_name, latitude=self.latitude, longitude=self.longitude, timestamp=self.timestamp
        )
