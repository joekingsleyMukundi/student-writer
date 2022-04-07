from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    phone = models.CharField(null=True, blank=True, max_length=15)
    profile_image = models.ImageField(null=True, blank=True, default='user-avatar-placeholder.png')
    otp = models.IntegerField(null=True, blank=True)
    is_client = models.BooleanField(default=False)
    is_super = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    amount_spent = models.IntegerField(default=0)
    REQUIRED_FIELDS = ['username', 'phone', ]
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email

    def soft_delete(self):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()

    def ban_user(self):
        self.is_active = False
        self.save()

    def unban_user(self):
        self.is_active = True
        self.save()


class Jobs(models.Model):
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    jobId = models.CharField(blank=True, null=True, max_length=200)
    title = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=200, blank=True, null=True)
    delivery_qty = models.CharField(max_length=200, blank=True, null=True)
    delivery_type = models.CharField(max_length=200, blank=True, null=True)
    min_salary = models.CharField(max_length=200,blank=True,null=True)
    max_salary = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    uploadedfile = models.FileField(blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    is_denied = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    is_regected = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Chats(models.Model):
    client=models.ForeignKey(CustomUser,on_delete=models.CASCADE, null=True,blank=True)
    admin = models.CharField(blank=True, null=True, max_length=200)
    chatid = models.CharField(blank=True, null=True, max_length=200)

    def __str__(self):
        return self.chatid

class Messages(models.Model):
    message = models.CharField(blank=True, null=True, max_length=1000)
    chat = models.ForeignKey(Chats, on_delete=models.CASCADE,null=True, blank=True)
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

class Bids(models.Model):
    freelancer= models.CharField(blank=True, null=True, max_length=1000)
    job= models.ForeignKey(Jobs, on_delete=models.CASCADE, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.freelancer


class Funds(models.Model):
    amount = models.CharField(blank=True, null=True,max_length=200)
    reciver = models.CharField(blank=True, null=True, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False)
    transaction_id = models.CharField(blank=True,null=True, max_length=200)
    payment_method = models.CharField(blank=True, null=True, max_length=100)
    status = models.CharField(default='unpaid', max_length=100)
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.transaction_id

