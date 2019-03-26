from django.db import models

class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)
    usr_bday = models.DateField(None)

#    woman = 'Ж'
 #   man = 'М'
#
 #   SEX_CHOICES = (
  #      (woman, 'Женский'),
   #     (man, 'Мужской'),
    #)
    #sex = models.CharField(
    #    max_length=1,
    #   choices=SEX_CHOICES,
    #    default=man,
    #)

    def __str__(self):
        return "Пользователь %s Имя %s Дата Рождения %s" % (self.email, self.name, self.usr_bday)

    class Meta:
        verbose_name = 'My Subscriber'
        verbose_name_plural = 'A lot of Subscribers'

