from django.db import models
#from django.db.models.fields import CharField

class Salon(models.Model):
    # id = models.AutoField(primary_key=True)
    aula = models.CharField(max_length=2)
    hora_entrada = models.TimeField()

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    idSalon = models.ForeignKey(Salon, on_delete = models.CASCADE)

    def full_name(self):
        return self.first_name + " " + self.last_name

    class Meta:
        abstract = True
        

class Alumno(Person):
    idSalon = models.ForeignKey(Salon, on_delete = models.CASCADE)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ['id', 'first_name', 'last_name'], name = 'primary_key_alumno'
            )
        ]

class Profesor(Person):
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ['id', 'first_name', 'last_name'], name = 'primary_key_profesor'
            )
        ]
    


# class OrderedAlum(Person):
#     class Meta:
#         proxy = True
#         ordering = ["last_name"]

class aniade_item(models.Model):
    titulo_proyecto = models.CharField(max_length=100)
    descripcion_proyecto = models.CharField(max_length=100)
    tags = models.CharField(max_length=100)
    url_github = models.CharField(max_length=100)
        