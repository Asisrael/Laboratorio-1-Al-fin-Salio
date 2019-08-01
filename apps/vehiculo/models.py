from django.db import models


class Parqueo(models.Model):
    lchoices = [
        ("A","A"),
        ("B","B"),
        ("C","C"),
        ("D","D"),
        ("E","E"),
        ("F","F"),
        ("G","G"),
        ("H","H"),
        ("I","I"),
        ("J","J"),
    ]
    parking_spot = models.CharField(max_length=4, choices=lchoices)
    def __str__(self):
        return " Lugar: " + self.parking_spot

class Vehiculo(models.Model):
    Vehicle_type = models.TextField(max_length=20)
    plate = models.CharField(max_length=10)
    spot = models.ManyToManyField(Parqueo, through="Asign")

    def __str__(self):
        return self.plate

class Asign(models.Model):
    vehicle = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    spot = models.ForeignKey(Parqueo, on_delete=models.CASCADE)
    start_hour = models.TimeField()
    end_hour = models.TimeField()

    def __str__(self):
        return self.Vehiculo.plate



    
