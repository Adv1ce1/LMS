from django.db import models
from users.models import User


class Payment(models.Model):
    """
        Модель представляет платеж в системе.

        Attributes:
            user (User): Связь с пользователем, который совершил платеж.
            date (DateField): Дата, когда был совершен платеж.
            course (Course): Связь с оплаченным курсом, если платеж касается курса.
            lesson (Lesson): Связь с оплаченным уроком, если платеж касается урока.
            amount (DecimalField): Сумма платежа.
            payment_method (str): Способ оплаты, выбирается из опций в PAYMENT_METHOD_CHOICES.

        PAYMENT_METHOD_CHOICES:
            Выбор из двух вариантов: 'cash' (Наличные) или 'transfer' (Перевод на счет).

        Methods:
            __str__(): Возвращает строковое представление объекта, используется для отображения
                информации о платеже при выводе в административной панели Django.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="пользователь")
    date = models.DateField(verbose_name="дата оплаты")
    course = models.ForeignKey('course.Course', on_delete=models.CASCADE, null=True, blank=True,
                               verbose_name="оплаченный курс")
    lesson = models.ForeignKey('course.Lesson', on_delete=models.CASCADE, null=True, blank=True,
                               verbose_name="оплаченный урок")

    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Наличные'),
        ('transfer', 'Перевод на счет'),
    ]
    payment_method = models.CharField(
        max_length=10,
        choices=PAYMENT_METHOD_CHOICES,
        default='cash',
        verbose_name="способ оплаты"
    )


    def __str__(self):
        return f'{self.user.email} - {self.date}'
