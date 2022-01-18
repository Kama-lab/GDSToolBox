from django.db import models
from django.core.validators import RegexValidator


class Airline(models.Model):
    only_alpha = RegexValidator(r'^[a-zA-Z]*$','Only letters are allowed')
    name = models.CharField(max_length=50,blank=False,null=False,validators=[only_alpha])
    code = models.CharField(max_length=2,blank=False,null=False)
    def save(self,force_insert=False,force_update=False):
        self.code = self.code.upper()
        super(Airline,self).save(force_insert,force_update)

    def __str__(self):
        return f"{self.name} : {self.code}"


class AirlineAddRequest(models.Model):
        """Airline add requests"""
        only_alpha = RegexValidator(r'^[a-zA-Z]*$')
        name = models.CharField(max_length=50,blank=False,null=False,validators=[only_alpha])
        code = models.CharField(max_length=2,blank=False,null=False)
        def save(self,force_insert=False,force_update=False):
            self.code = self.code.upper()
            super(AirlineAddRequest,self).save(force_insert,force_update)

        def __str__(self):
            return f"{self.name} : {self.code}"
