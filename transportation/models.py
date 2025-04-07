from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.utils.crypto import get_random_string
import random
import string

ROLES = (
    ('1', 'Administrator'),
    ('2', 'renter')
)


stat = (
    (1, 'Lock'),
    (2, 'Unclock')
)

#primeadmin - primeadmin
class controls(models.Model):
    '''Model definition for controls.'''
    control = models.IntegerField(choices=stat)
    site = models.CharField(max_length=50)
    class Meta:

        verbose_name = 'controls'
        verbose_name_plural = 'controls'


class rates(models.Model):
    rates = models.IntegerField()
    class Meta:

        verbose_name = 'rates'
        verbose_name_plural = 'rates'



class User(AbstractUser):
    fname = models.CharField(max_length=100, null=True)
    lname = models.CharField(max_length=100, null=True)
    Address = models.CharField(max_length=200, null=True)
    Contact = models.IntegerField(null=True)
    email = models.EmailField(unique=True, null=True)
    roles = models.CharField(choices=ROLES, default='2', max_length=50)  
    avatar = models.ImageField(upload_to="Profiles", null=True, default="Profiles/avatar.png")
    code = models.IntegerField(blank=True, null=True)  # Allow blank and null values
    status = models.CharField(default="notverified", max_length=50)
    lock = models.CharField(max_length=50, default='none')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []




class Shops(models.Model):
    owner = models.ForeignKey('User', related_name='myshops', on_delete=models.CASCADE)
    validids = models.ImageField(upload_to='valid_id', verbose_name="Owners valid id")
    banner = models.ImageField(upload_to='Banners')
    logo = models.ImageField(upload_to='logos')
    shop_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, max_length=150)  # New slug field
    shop_description = models.TextField()
    tin = models.CharField(max_length=50)
    brn = models.CharField(max_length=50)
    contact = models.IntegerField()
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=50)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=50, default="lock")
    date_created = models.DateTimeField(auto_now=True, auto_now_add=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.shop_name)
            unique_slug = base_slug
            num = 1
            while Shops.objects.filter(slug=unique_slug).exists():
                unique_slug = f'{base_slug}-{get_random_string(4)}-{num}'
                num += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)

Brands = (
    ('toyota', 'Toyota'),
    ('honda', 'Honda'),
    ('mitsubishi', 'Mitsubishi'),
    ('chevrolet', 'Chevrolet'),
    ('ford', 'Ford'),
    ('nissan', 'Nissan'),
    ('bmw', 'BMW'),
    ('mercedes_benz', 'Mercedes-Benz'),
    ('audi', 'Audi'),
    ('volkswagen', 'Volkswagen'),
    ('hyundai', 'Hyundai'),
    ('kia', 'Kia'),
    ('tesla', 'Tesla'),
    ('subaru', 'Subaru'),
    ('mazda', 'Mazda'),
    ('volvo', 'Volvo'),
    ('lexus', 'Lexus'),
    ('porsche', 'Porsche'),
    ('ferrari', 'Ferrari'),
    ('lamborghini', 'Lamborghini'),
    ('land_rover', 'Land Rover'),
    ('jaguar', 'Jaguar'),
    ('infiniti', 'Infiniti'),
    ('acura', 'Acura'),
    ('jeep', 'Jeep'),
    ('dodge', 'Dodge'),
    ('ram', 'Ram'),
    ('chrysler', 'Chrysler'),
    ('buick', 'Buick'),
    ('gmc', 'GMC'),
    ('cadillac', 'Cadillac'),
    ('peugeot', 'Peugeot'),
    ('renault', 'Renault'),
    ('citroen', 'Citroën'),
    ('fiat', 'Fiat'),
    ('alfa_romeo', 'Alfa Romeo'),
    ('suzuki', 'Suzuki'),
    ('skoda', 'Škoda'),
    ('seat', 'SEAT'),
    ('bentley', 'Bentley'),
    ('rolls_royce', 'Rolls-Royce'),
    ('aston_martin', 'Aston Martin'),
    ('maserati', 'Maserati'),
    ('lotus', 'Lotus'),
    ('mclaren', 'McLaren'),
    ('bugatti', 'Bugatti'),
    ('saab', 'Saab'),
    ('opel', 'Opel'),
)


transmission = (
    ('manual', 'Manual'),
    ('automatic', 'Automatic'),
    ('semi', 'Semi-Automatic'),
    ('cvt', 'Continuously Variable Transmission (CVT)'),
    ('dual_clutch', 'Dual-Clutch Transmission (DCT)'),
    ('tiptronic', 'Tiptronic'),
    ('electric', 'Electric'),
)


seat = (
    (2, '2 Seater'),
    (4, '4 Seater'),
    (5, '5 Seater'),
    (6, '6 Seater'),
    (7, '7 Seater'),
    (8, '8 Seater'),
    (9, '9 Seater'),
    (10, '10 Seater'),
)



fuel_types = (
    ('diesel', 'Diesel'),
    ('gasoline', 'Gasoline'),
    ('electric', 'Electric'),
    ('hybrid', 'Hybrid'),
    ('plug_in_hybrid', 'Plug-in Hybrid'),
    ('cng', 'Compressed Natural Gas (CNG)'),
    ('lpg', 'Liquefied Petroleum Gas (LPG)'),
    ('hydrogen', 'Hydrogen'),
    ('ethanol', 'Ethanol'),
    ('biodiesel', 'Biodiesel'),
    ('synthetic', 'Synthetic Fuel (eFuel)'),
)

vehicle_type = (
    ('sedan', 'Sedan'),
    ('suv', 'SUV (Sport Utility Vehicle)'),
    ('hatchback', 'Hatchback'),
    ('coupe', 'Coupe'),
    ('convertible', 'Convertible'),
    ('wagon', 'Wagon'),
    ('pickup', 'Pickup Truck'),
    ('van', 'Van'),
    ('motorcycle', 'Motorcycle'),
    ('bus', 'Bus'),
    ('truck', 'Truck'),
    ('minivan', 'Minivan'),
    ('crossover', 'Crossover'),
    ('electric', 'Electric Vehicle'),
    ('hybrid', 'Hybrid Vehicle'),
    ('sports', 'Sports Car'),
)


class Vehicle(models.Model):
    shop_belong = models.ForeignKey("Shops", verbose_name=("Shop Vehicles"), related_name='shopvehicles', on_delete=models.CASCADE)
    img1 = models.ImageField(upload_to="Vehicle Image", height_field=None, width_field=None, max_length=None)
    img2 = models.ImageField(upload_to="Vehicle Image", height_field=None, width_field=None, max_length=None)
    img3 = models.ImageField(upload_to="Vehicle Image", height_field=None, width_field=None, max_length=None)
    img4 = models.ImageField(upload_to="Vehicle Image", height_field=None, width_field=None, max_length=None)
    img5 = models.ImageField(upload_to="Vehicle Image", height_field=None, width_field=None, max_length=None)
    documents = models.FileField( upload_to="Car Documents", max_length=None)
    categories = models.CharField(choices=Brands, max_length=50)
    transmission = models.CharField(choices=transmission, max_length=50)
    seat = models.IntegerField(choices=seat)
    fuels = models.CharField(choices=fuel_types, max_length=50)
    color_description = models.CharField(verbose_name="Color description", max_length=150)
    model_car = models.CharField(verbose_name="Car Model", max_length=50)
    plate = models.CharField(verbose_name="Plate Number", max_length=50)
    chasis_number = models.CharField(verbose_name="Chasis Number", max_length=50)
    vin_no = models.CharField(verbose_name="Vin Number", max_length=50)
    vehicle_type = models.CharField(choices=vehicle_type,verbose_name="Vehicle Type", max_length=50)
    status = models.CharField(max_length=50, default="uncheck")
    rent_per_hr = models.IntegerField()


class driver_shop(models.Model):
    account = models.ForeignKey("User", verbose_name=("Account Driver"), related_name="account_driver", on_delete=models.CASCADE)
    shop_under = models.ForeignKey("Shops", verbose_name=("Shop Driver"),related_name="shopdriver", on_delete=models.CASCADE)
    drivers_license = models.ImageField(upload_to="Drivers License", height_field=None, width_field=None, max_length=None)
    phone_number = models.IntegerField()
    date_registered = models.DateTimeField(auto_now=True, auto_now_add=False)
    drivers_rate = models.IntegerField(verbose_name="Driver Hourly Rate")
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.account.fname +" "+ self.account.lname



pchoice = (
    (1, 'Onsite'),
    (2, 'Online'),
)

garage = (
    (1, 'Inside Garage'),
    (2, 'Outside'),
    (3, 'Return Garage'),
)

rate_num = (
    (1, 'one star'),
    (2, 'two star'),
    (3, 'three star'),
    (4, 'four star'),
    (5, 'five star'),
)

class Rented_Cars(models.Model):
    renters = models.ForeignKey("User", verbose_name=("renters"), related_name="renters_driver", on_delete=models.CASCADE)
    unit_rented = models.ForeignKey("Vehicle", verbose_name=("Unit Rented"),related_name="unitrented", on_delete=models.CASCADE)
    driver_shp = models.ForeignKey("driver_shop", verbose_name=("Driver"), related_name="driversinrent",  on_delete=models.SET_NULL, null=True)
    renter_validid = models.FileField(verbose_name="Your 2 Valid(s) in 1 PDF" , upload_to="RentersID", max_length=100)
    pick_up_unit = models.DateTimeField(auto_now=False, auto_now_add=False)
    return_unit = models.DateTimeField(auto_now=False, auto_now_add=False)
    total_hrs = models.IntegerField()
    car_fee_total = models.IntegerField()
    driver_fee_total = models.IntegerField()
    total_fare = models.IntegerField(default=88)
    status = models.CharField(max_length=50, default="pending")
    drivers_approval = models.CharField(max_length=50, default="pending")
    payment_choice = models.IntegerField(choices=pchoice)
    unit_release = models.IntegerField(choices=garage, default=1)
    rent_id = models.CharField(max_length=20, unique=True, editable=False, verbose_name="RENTID")
    out_garage = models.DateTimeField( auto_now=False, auto_now_add=False, null=True)
    return_garage = models.DateTimeField( auto_now=False, auto_now_add=False, null=True)
    excess_exist = models.IntegerField(default=0)
    execes_hrs = models.IntegerField(null=True)
    execes_amount = models.IntegerField(null=True)
    paid_excess = models.CharField(max_length=50,default="none")
    transaction_done = models.IntegerField(default=0)
    #month_track
    mth = models.CharField(max_length=50)
    yr = models.CharField(max_length=50)
    sqc = models.CharField(max_length=50)
    #website revenues
    share_rates = models.IntegerField(default=0)
    #liquidated
    liquidated = models.IntegerField(default=0)
    #rating
    rating_bolean = models.IntegerField(default=0)
    rating_star = models.IntegerField(default=0,choices=rate_num)
    rating_reviews = models.TextField(null=True)
    #issues
    issues = models.IntegerField(default=0)
    total_cost_issue = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        # Generate a unique RENTID if not already set
        if not self.rent_id:
            self.rent_id = self.generate_rent_id()
        super().save(*args, **kwargs)

    @staticmethod
    def generate_rent_id():
        """Generate a unique RENTID with random digits."""
        random_number = ''.join(random.choices(string.digits, k=10))
        return f"RENT{random_number}C"
    



    

class onsitepayment(models.Model):

    rent_reference = models.ForeignKey("Rented_Cars", verbose_name=("rent payment"), related_name="rent_payments", on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    contact = models.IntegerField()
    date_pay = models.DateTimeField(auto_now=True, auto_now_add=False)
    proof_resibo = models.ImageField(upload_to="Reciepts", height_field=None, width_field=None, max_length=None)

    class Meta:
        verbose_name = ("onsitepayment")
        verbose_name_plural = ("onsitepayments")


class payment_process(models.Model):
    shop_processed = models.ForeignKey("Shops", verbose_name=("Shop Payments"), related_name='shoppayments', on_delete=models.SET_NULL, null=True)
    transaction_reference = models.CharField(max_length=20, unique=True, editable=False, verbose_name="Transacton")
    status = models.CharField(default="uncheck", max_length=50)
    amount = models.IntegerField()
    transaction_type = models.IntegerField(default=0, choices=pchoice)
    category = models.CharField(max_length=50) #request or submitted
    date_submitted = models.DateTimeField( auto_now=True, auto_now_add=False)
    
    def save(self, *args, **kwargs):
        # Generate a unique transaction_reference if not already set
        if not self.transaction_reference:
            self.transaction_reference = self.generate_transaction_reference()
        super().save(*args, **kwargs)

    @staticmethod
    def generate_transaction_reference():
        """Generate a unique transaction_reference with random digits."""
        random_number = ''.join(random.choices(string.digits, k=10))
        return f"TRSTN{random_number}"

class payment_process_items(models.Model):
    payment_root = models.ForeignKey("payment_process", verbose_name=("root"), on_delete=models.SET_NULL, null=True)
    rent_transactions = models.ForeignKey("Rented_Cars", verbose_name=("renttransaction"), on_delete=models.SET_NULL, null=True)
    

class rent_issue(models.Model):
    rent = models.ForeignKey("Rented_Cars", verbose_name=("Rent cars issue"), on_delete=models.CASCADE)
    issue_name = models.CharField(max_length=150)
    issue_details = models.TextField()
    issue_amount = models.IntegerField(default=500)

    
    


    




