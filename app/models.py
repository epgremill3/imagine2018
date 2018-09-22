from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class Car(models.Model):
    """Represents a car that a person owns"""
    owner = models.ForeignKey(User, on_delete=models.PROTECT, null=False)
    year = models.IntegerField(null=False)
    make = models.TextField(max_length=255, blank=False, null=False)
    model = models.TextField(max_length=255, blank=False, null=False)
    color = models.TextField(max_length=255, blank=False, null=False)
    vin = models.TextField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField(null=False, auto_now=True)

    def _set_year(self, year: int):
        """Validate that the year is within a valid range for cars before setting"""
        current_year = now().year
        if 1800 <= year <= current_year:
            self.year = year
        else:
            raise ValueError("Year {year} must be between 1800 and {current_year}".format(
                year=year, current_year=current_year
            ))

    def __init__(self, owner: User, year: int, make: str, model: str, color: str, vin: str = "", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.owner = owner
        self.make = make
        self.model = model
        self.color = color
        self.vin = vin
        self._set_year(year)

    def __str__(self):
        return "{owner}'s {color} {year} {make} {model}".format(
            owner=self.owner, color=self.color, year=self.year, make=self.make, model=self.model
        )
