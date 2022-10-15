from django.db import models
from django.utils.timezone import now

# Create your models here.
class Phone(models.Model):
    phone_number = models.IntegerField()

    def __int__(self):
        return self.phone_number

class Ariza(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    telegram = models.CharField(max_length=100)
    date = models.DateTimeField(default=now, editable=False)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class CourseName(models.Model):
    name = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='images/', blank=True)
    darslar_soni = models.IntegerField()
    vazifalar_soni = models.IntegerField()

    def __str__(self):
        return self.name


class CourseFacts(models.Model):
    title = models.CharField(max_length=400)

    def __str__(self):
        return self.title


class Teacher(models.Model):
    name = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.name

class TeacherFacts(models.Model):
    title = models.CharField(max_length=300)
    icon = models.ImageField(upload_to='images/icon/')

    def __str__(self):
        return self.title

class KimlarUchun(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title


class LearningList(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tartib_raqami = models.SmallIntegerField()

    def __str__(self):
        return self.title

class LearningBody(models.Model):
    photo = models.ImageField()

class Loyihalar(models.Model):
    photo = models.ImageField()

class LoyihalarFacts(models.Model):
    title = models.CharField(max_length=250)
    icon = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title


class Feedbacks(models.Model):
    title = models.CharField(max_length=250)
    name = models.CharField(max_length=150)
    description = models.TextField()
    photo = models.ImageField(upload_to='images/')

    tartib_raqami = models.SmallIntegerField()

    def __str__(self):
        return self.title

class SababTitle(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class SababList(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.ImageField(upload_to='images/icon/')

    def __str__(self):
        return self.title


class Qulayliklar(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.ImageField(upload_to='images/icon/', blank=True)

    def __str__(self):
        return self.title


class KursAfzalliklari(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    icon = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class Imkoniyat(models.Model):
    description = models.TextField()
    narx = models.TextField()
    photo = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.narx

class Admin(models.Model):
    name = models.CharField(max_length=100)
    telegram_id = models.IntegerField()
    bot_token = models.CharField(max_length=100)

    def __str__(self):
        return self.name