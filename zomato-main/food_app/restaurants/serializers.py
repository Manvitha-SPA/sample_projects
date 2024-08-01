from rest_framework import serializers
from .models import Restaurant

class ObjSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = ["R_name","R_address","R_phone","R_timings","R_apc","R_parking","R_pet","R_cu","R_pay","R_more_info","R_seat","R_reserve"]

