# Dreamweb-app

## คำสั่ง runs
    python manage.py runserver

## คำสั่งสร้างแอพ
    python manage.py startapp <ชื่อแอพ>

## คำสั่งสร้างแอดมิน
    python manage.py createsuperuser



# สร้างโมเดล
```python
 from django.db import models

# Create your models here.

class Student(models.Model):

    std_id = models.IntegerField()
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)

    phone = models.CharField(max_length=10)



```