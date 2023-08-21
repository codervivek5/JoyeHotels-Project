from django.contrib.auth.models import User
from django.db import models
import uuid


# Create your models here.

class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Amenities(BaseModel):
    amenity_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.amenity_name


class Hotel(BaseModel):
    hotel_name = models.CharField(max_length=100)
    actual_price = models.IntegerField(default=1000)
    hotel_price = models.IntegerField()
    gst_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=18,
        help_text="GST percentage"
    ) 
    description = models.TextField()
    place = models.CharField(max_length=100)
    amenities = models.ManyToManyField(Amenities)
    room_count = models.IntegerField(default=10)
    



    def __str__(self) -> str:
        return self.hotel_name


class HotelImages(BaseModel):
    hotel = models.ForeignKey(Hotel, related_name="hotel_images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="hotel")

    def __str__(self):
        return f"Image: {self.image.name}"

class HotelBooking(BaseModel):
    hotel = models.ForeignKey(Hotel, related_name="hotel_booking", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_booking', on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    booking_type = models.CharField(max_length=30, choices=(('pre_paid', 'pre paid'), ('post_paid', 'post paid')))

