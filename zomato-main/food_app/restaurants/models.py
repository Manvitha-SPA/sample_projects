from django.db import models

class Restaurant(models.Model):
    
    R_name=models.CharField(max_length=50)
    R_address=models.CharField(max_length=50)
    R_phone = models.CharField(max_length=50)  # Increase the max length to 50 characters or more
    R_timings=models.CharField(max_length=500,default="6am to 9pm")
    R_apc=models.CharField(max_length=500,default="Rs 5000")
    R_parking=models.CharField(max_length=5,default=True)
    R_pet=models.CharField(max_length=5,default=False)
    R_cu=models.CharField(max_length=500,default=['a','b','c'])
    R_pay=models.CharField(max_length=500,default="Cash or Cards Accepted")
    R_more_info=models.CharField(max_length=500,default=['ac','bd'])
    R_seat=models.CharField(max_length=50,default='Indoor Seating')
    R_reserve=models.CharField(max_length=5,default='Yes')
    def __str__(self):
        return f"{self.R_name}, {self.R_address},{self.R_phone},{self.R_timings},{self.R_apc},{self.R_parking},{self.R_pet},{self.R_cu},{self.R_pay},{self.R_more_info},{self.R_seat},{self.R_reserve}"

    