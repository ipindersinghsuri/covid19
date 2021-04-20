from django.db import models


# Create your models here.
class Hospital(models.Model):
    state_choices = (
        ("Andhra Pradesh", "Andhra Pradesh"), ("Arunachal Pradesh ", "Arunachal Pradesh "), ("Assam", "Assam"),
        ("Bihar", "Bihar"), ("Chhattisgarh", "Chhattisgarh"), ("Goa", "Goa"), ("Gujarat", "Gujarat"),
        ("Haryana", "Haryana"), ("Himachal Pradesh", "Himachal Pradesh"), ("Jammu and Kashmir ", "Jammu and Kashmir "),
        ("Jharkhand", "Jharkhand"), ("Karnataka", "Karnataka"), ("Kerala", "Kerala"),
        ("Madhya Pradesh", "Madhya Pradesh"),
        ("Maharashtra", "Maharashtra"), ("Manipur", "Manipur"), ("Meghalaya", "Meghalaya"), ("Mizoram", "Mizoram"),
        ("Nagaland", "Nagaland"), ("Odisha", "Odisha"), ("Punjab", "Punjab"), ("Rajasthan", "Rajasthan"),
        ("Sikkim", "Sikkim"), ("Tamil Nadu", "Tamil Nadu"), ("Telangana", "Telangana"), ("Tripura", "Tripura"),
        ("Uttar Pradesh", "Uttar Pradesh"), ("Uttarakhand", "Uttarakhand"), ("West Bengal", "West Bengal"),
        ("Andaman and Nicobar Islands", "Andaman and Nicobar Islands"), ("Chandigarh", "Chandigarh"),
        ("Dadra and Nagar Haveli", "Dadra and Nagar Haveli"), ("Daman and Diu", "Daman and Diu"),
        ("Lakshadweep", "Lakshadweep"), ("Delhi", "Delhi"),
        ("Puducherry", "Puducherry"))
    state = models.CharField(choices=state_choices, max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, blank=False)
    phone = models.CharField(max_length=256)
    normal_bed = models.IntegerField(default=0)
    oxygen_bed = models.IntegerField(default=0)
    ventilator_bed = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)  # This should add the created date on its own only once.
    updated_at = models.DateTimeField(auto_now=True)  # This should add the updated date every time.

    def __str__(self):
        return f"{self.name} - {self.state}"
