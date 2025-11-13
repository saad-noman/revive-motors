from django.db import models


class ContactDetail(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='contacts')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.phone_number or self.email or self.profile_link}"


class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    condition = models.CharField(max_length=50)
    transmission = models.CharField(max_length=50)
    mileage = models.IntegerField()
    description = models.TextField()
    photo = models.URLField()
    current_owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='owned_cars')
    available_for_sale = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"


class OwnershipRecord(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='ownership_records')
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.car} owned by {self.owner.username}"


class Transaction(models.Model):
    buyer = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='purchases')
    seller = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='sales')
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    transaction_date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Transaction: {self.buyer.username} bought {self.car} from {self.seller.username}"


class Rating(models.Model):
    transaction = models.OneToOneField(Transaction, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Rating for {self.transaction.seller.username} by {self.transaction.buyer.username}"