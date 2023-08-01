from django.db import models

# Create your models here.
class Discount(models.Model):
    type = models.CharField(max_length=200)
    discount_percentage = models.IntegerField(default=0.00)

    def __str__(self) -> str:
        return self.type


class Type(models.Model):
    value = models.CharField(max_length=200) 

    def __str__(self) -> str:
        return self.value


class Course(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    schedule = models.CharField(max_length=200)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    price = models.FloatField()
    discount = models.ManyToManyField(Discount)

    def __str__(self) -> str:
        return self.type.value


class Subject(models.Model):
    name = models.CharField(max_length=200)
    professor = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.name + '' + self.course.type.value


class Classes(models.Model):
    name = models.CharField(max_length=200)
    schedule = models.JSONField()
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    hasTest = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name + '' + self.subject.name