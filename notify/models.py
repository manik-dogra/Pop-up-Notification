from django.db import models

class User(models.Model):
    user_id = models.AutoField
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField(max_length=254, default="abc@gmail.com")
    user_number = models.CharField(max_length=20)
    user_whatsapp = models.CharField(max_length=30)
    userchoice_email = models.BooleanField(default=False)
    userchoice_message = models.BooleanField(default=False)
    userchoice_whatsapp = models.BooleanField(default=False)

    def __str__(self):
        return self.user_name