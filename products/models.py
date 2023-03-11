from django.db import models


class CarMark(models.Model):
    name_mark = models.CharField(max_length=250)

    def __str__(self):
        return self.name_mark


class CarModel(models.Model):
    carmark = models.ForeignKey(CarMark, on_delete=models.CASCADE,
                                verbose_name='carmark')
    name_mod = models.CharField(max_length=250)

    def __str__(self):
        return self.name_mod


class CarEngine(models.Model):
    carmodel = models.ForeignKey(CarModel, on_delete=models.CASCADE,
                                 verbose_name='carmodel')
    careng = models.CharField(max_length=250)

    def __str__(self):
        return self.careng


class GoodsItem(models.Model):
    goodsi = models.ForeignKey("products.Goods", on_delete=models.CASCADE, verbose_name="ggggggggooodsi")
    carmark = models.ForeignKey(CarMark, on_delete=models.CASCADE, verbose_name='carmark')
    carmodel = models.ForeignKey(CarModel, on_delete=models.CASCADE, verbose_name='carmodel')
    carengine = models.ForeignKey(CarEngine, on_delete=models.CASCADE, verbose_name='carengine')

    def __str__(self):
        return f'{self.carmodel}'


class DictionaryCategory(models.Model):
    title_dictionary = models.CharField(max_length=120, unique=True)
    categories = models.ManyToManyField('Category', blank=True, related_name='category_dictionaries')

    def __str__(self):
        return self.title_dictionary


class Brand(models.Model):
    title_brand = models.CharField(primary_key=True, max_length=40)

    def __str__(self):
        return self.title_brand


class Category(models.Model):
    title_category = models.CharField(max_length=120, unique=True)
    dictionaries = models.ManyToManyField('DictionaryCategory', blank=True, related_name='category_dictionaries')

    def get_dictionaries_display(self):
        return [dictionary.title_dictionary for dictionary in self.category_dictionaries.all()]

    def __str__(self):
        return self.title_category


class Goods(models.Model):
    article = models.CharField(max_length=24, primary_key=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    title_goods = models.CharField(max_length=140)
    description = models.TextField(max_length=3500, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='goods')

    def __str__(self):
        return str(f'{self.title_goods}: {self.article}')


class AllowedCombination(models.Model):
    carmark = models.ForeignKey(CarMark, on_delete=models.CASCADE)
    carmodel = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    carengine = models.ForeignKey(CarEngine, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.carmark} {self.carmodel} {self.carengine}'

    class Meta:
        ordering = ['pk']
