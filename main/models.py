from django.db import models


class Tours(models.Model):
    # id = models.IntegerField(primary_key=True)
	city_name = models.CharField('Название тура или города', max_length=30)
	description = models.TextField('О туре')
	img1 = models.ImageField('Изображение', upload_to='/images/')
	# img2 = models.ImageField(upload_to='', verbose_name)
	price = models.IntegerField('Цена', default=0)
	discount = models.PositiveIntegerField('Скидка', default=0, null=True)
	available = models.BooleanField('В наличии')
    
    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'
    
    def __str__(self):
            return self.city_name


    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})


class Categories(models.Model):
	name = models.Charfield('Категория/Название страны', max_length=30)
    
    class Meta:
        verbose_name = 'Категория/Название страны'
        verbose_name_plural = 'Категории/Название стран'

	def __str__(self):
        	return self.name

# class Reviews (models.Model):
    # user = models.ForeignKey('Пользователь', User, on_delete=models.CASCADE)
    # created = models.DateTimeField(auto_now_add=True)
    # content = models.TextField('Отзыв')
    # post = models.ForeignKey('Tours', related_name='reviews', on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.user.username
