from django.db import models
import datetime 


class Image(models.Model):
	title = models.CharField('Название',max_length = 150)
	image = models.ImageField('Изображения', upload_to = 'shop/', blank = True)
	description = models.TextField('Описание')
	pub_date = models.DateTimeField('Дата публикации', default = '')


	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Картинка'
		verbose_name_plural = 'Картинки'
