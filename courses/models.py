from django.db import models


# Create your models here.
class Discount(models.Model):
    type = models.CharField(max_length=200)
    discount_percentage = models.FloatField(null=True, default=0.00)
    discount_amount = models.FloatField(null=True, default=0.00)

    def __str__(self) -> str:
        return (
            self.type
            + " $"
            + str(self.discount_amount)
            + " __ "
            + str(self.discount_percentage)
            + "%"
        )


class Course_Type(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Day(models.Model):
    DAYS_OF_WEEK = [
        ("1", "Sunday"),
        ("2", "Monday"),
        ("3", "Tuesday"),
        ("4", "Wednesday"),
        ("5", "Thursday"),
        ("6", "Friday"),
        ("7", "Saturday"),
    ]
    days = models.CharField(max_length=20, choices=DAYS_OF_WEEK)


class Course(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    schedule_start = models.DateTimeField(default=None)
    schedule_end = models.DateTimeField(default=None)
    schedule_days = models.ManyToManyField(Day)
    course_type = models.ForeignKey(Course_Type, on_delete=models.CASCADE)
    price = models.FloatField()
    discount = models.ManyToManyField(Discount)

    def __str__(self) -> str:
        return self.type.course_type + "-" + self.start_date.year


class Subject(models.Model):
    subject_name = models.CharField(max_length=200)
    professor = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.name + " " + self.course.type.course


class Lesson(models.Model):
    class_name = models.CharField(max_length=200)
    end_date: models.DateField()
    start_date: models.DateField()
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    test_require = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name + " " + self.subject.name
