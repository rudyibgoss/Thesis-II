
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from transportation.decorators import role_required
from django.core.paginator import Paginator
from .forms import *
from datetime import datetime
from django.utils.timezone import now 
import pytz
from django.db.models import Sum, Max
from django.db.models import Q



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



def home(request):
    controlsite = get_object_or_404(controls, pk=1)
    if controlsite.control == 1:
        return redirect(controlsite.site)
    
    context = {
    }
    return render(request,'public/index.html',context)

def vehicle(request):
    controlsite = get_object_or_404(controls, pk=1)
    if controlsite.control == 1:
        return redirect(controlsite.site)
    vehicle = Vehicle.objects.filter(status="published")

    if request.method=="POST":
        searchbrand= request.POST.get('brand')
        searchseat = request.POST.get('seat')
        searchtransmission= request.POST.get('transmission')
        vehicle = Vehicle.objects.filter(
            Q(categories=searchbrand) | 
            Q(seat=searchseat) | 
            Q(transmission=searchtransmission)
        ).filter(status="published")
    else:
        vehicle = Vehicle.objects.filter(status="published")
    
    context = {
        "vehicle":vehicle,
        'Brands':Brands,
        'fuel_types':fuel_types,
        'seat':seat,
        'transmission':transmission,
    }
    return render(request,'public/vehicle.html',context)

def drivers(request):
    controlsite = get_object_or_404(controls, pk=1)
    if controlsite.control == 1:
        return redirect(controlsite.site)
    context = {
    }
    return render(request,'public/drivers.html',context)

def car_details(request, pk):
    controlsite = get_object_or_404(controls, pk=1)
    if controlsite.control == 1:
        return redirect(controlsite.site)
    vehicle_details = get_object_or_404(Vehicle,pk=pk)
    shop = vehicle_details.shop_belong.id
    shop_details = get_object_or_404(Shops,pk=shop)
    reviews = Rented_Cars.objects.filter(unit_rented=vehicle_details,rating_bolean=2)
    
    context = {
        "vehicle_details":vehicle_details,
        "shop_details":shop_details,
        "reviews":reviews,
    }
    return render(request,'public/car_details.html',context)

def driver_details(request):
    controlsite = get_object_or_404(controls, pk=1)
    if controlsite.control == 1:
        return redirect(controlsite.site)
    context = {
    }
    return render(request,'public/driver_details.html',context)


def shop(request):
    controlsite = get_object_or_404(controls, pk=1)
    if controlsite.control == 1:
        return redirect(controlsite.site)
    shop = Shops.objects.filter(status="published")
    context = {
        'shop':shop,
        
    }
    return render(request,'public/shop.html',context)

def shop_details(request,slug):
    controlsite = get_object_or_404(controls, pk=1)
    if controlsite.control == 1:
        return redirect(controlsite.site)
    shop_details = get_object_or_404(Shops,slug=slug)
    shop_cars = Vehicle.objects.filter(shop_belong=shop_details,status="published")
    shop_cars_count = Vehicle.objects.filter(shop_belong=shop_details,status="published").count()
    shop_driver = driver_shop.objects.filter(shop_under=shop_details,status=1)
    shop_driver_count = driver_shop.objects.filter(shop_under=shop_details,status=1).count()
    page_cars = Paginator(shop_cars, 6)  
    page_number = request.GET.get("cars")
    cars_objects = page_cars.get_page(page_number)
    context = {
        'cars_objects':cars_objects,
        'shop_details':shop_details,
        'shop_cars_count':shop_cars_count,
        'shop_driver':shop_driver,
        'shop_driver_count':shop_driver_count,
    }
    return render(request,'public/shop_details.html',context)


def contacts(request):
    controlsite = get_object_or_404(controls, pk=1)
    if controlsite.control == 1:
        return redirect(controlsite.site)
    context = {
        
    }
    return render(request,'public/contact.html',context)


def createaacount(request):
    controlsite = get_object_or_404(controls, pk=1)
    if controlsite.control == 1:
        return redirect(controlsite.site)
    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            request.session['unverified_email'] =  user.email
            user.username = user.username.lower()
            user.code = int(get_random_string(length=6, allowed_chars='1234567890'))
            user.save()
            # Send OTP to the user's email
            subject = 'Your OTP for Registration'
            message = f'Your OTP is {user.code}. Enter this code to complete your registration.'
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = user.email
            try:
                send_mail(subject, message, from_email, [to_email], fail_silently=False)
            except Exception as e:
                messages.error(request, f"Error sending email: {e}")
            #login(request, user, backend='django.contrib.auth.backends.ModelBackend')  # for Direct log in after registration
            messages.success(request, 'Account Created Successfully')
            return redirect('verify_email')
        else:
            messages.error(request, 'An error occurred during registration {form.errors}')
    
    context = {
        'form': form,
    }
    return render(request,'public/createaacount.html',context)



def verify_email(request):
    controlsite = get_object_or_404(controls, pk=1)
    if controlsite.control == 1:
        return redirect(controlsite.site)
    if request.method == 'POST':
        otp = request.POST.get("otp")
        email = request.session['unverified_email']

        if not email:
            messages.error(request, 'Email not found in session')
            return redirect('signin')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'User not found')
            return redirect('signin')

        # Perform pattern match on user code
        if str(user.code) == otp:
            user.status = "verified"
            user.code = 0  # Assuming 0 represents the verified status
            user.save()
            messages.info(request, 'Account verified and signed in successfully...')
            subject = 'Account Verification'
            message = f'Congratulations! Your account is now verified. You can now log in. '
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = user.email
            send_mail(subject, message, from_email, [to_email], fail_silently=False)
            request.session.flush()
            messages.success(request, "Account Verified")
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('users')
        else:
            messages.error(request, "Code doesn't match")

    return render(request, 'public/verify.html')



def signin(request):
    controlsite = get_object_or_404(controls, pk=1)
    if controlsite.control == 1:
        return redirect(controlsite.site)
    page = 'login'
    if request.user.is_authenticated:
        
        return redirect('admin')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'Account does not exist')
            return render(request, 'public/signin.html', {'page': page})

        user = authenticate(request, email=email, password=password)

        if user is not None:
            # Check user's status and code
            if user.status == 'verified' or user.code == 0:
                if user.lock == 'restricted':
                    logout(request)
                    messages.error(request,'Please Try Again Later.')
                    return redirect('signin')
                else:
                    user.log_status = "online"
                    user.save()
                    login(request, user)
                    messages.success(request,'Login succesfully')
                    return redirect('admin')
            else:
                # Save email in session and render a template for email verification
                request.session['unverified_email'] = email
                messages.success(request,'Please Verify your Account')
                return render(request, 'public/verify.html', {'user': user})
        else:
            messages.error(request, 'Username OR password does not exist')

    context = {
        'page': page,
        }
    return render(request,'public/signin.html')


#============================================================================================================
#ADMINISTRATORS


@login_required(login_url='signin')
@role_required(allowed_roles=['1'], redirect_url='users')
def admin(request):
    controlsite = get_object_or_404(controls, pk=1)
    if controlsite.control == 1:
        return redirect(controlsite.site)
    page = 'homedashboard'
    title_page = 'Administrator'
    users = request.user
    rent_issues = rent_issue.objects.filter(rent__renters=users)
    manila_timezone = pytz.timezone("Asia/Manila")
    yrs = datetime.now(manila_timezone).strftime('%Y')
    current_time = datetime.now(manila_timezone).strftime('%Y-%m-%d %H:%M:%S')
    count_cars = Vehicle.objects.all().count()
    count_users = User.objects.filter(roles=2).count()
    all_transactions = Rented_Cars.objects.all()
    revenue = Rented_Cars.objects.filter(yr=yrs, transaction_done=1, excess_exist=0).aggregate(total_share_rates=Sum('share_rates'))   
    total_revenue = revenue['total_share_rates'] or 0 
    monthly_counts = Rented_Cars.objects.filter(yr=yrs,transaction_done=1,excess_exist=0).values('mth').annotate(share_rates=Sum('share_rates')).order_by('sqc')
    context = {
        'page':page,
        'title_page':title_page,
        'users':users,
        'rent_issues':rent_issues,
        'monthly_counts':monthly_counts,
        'count_cars':count_cars,
        'count_users':count_users,
        'total_revenue':total_revenue,
        'current_time':current_time,
        'all_transactions':all_transactions,
       
    }
    return render(request, 'accounts/index.html',context)





@login_required(login_url='signin')
@role_required(allowed_roles=['1'], redirect_url='users')
def rent_details_shop_admin(request,rentid):
    users = request.user
    rent_issues = rent_issue.objects.filter(rent__renters=users)
    page = 'myslistshop'
    title_page = 'Shop Details'
    rate_details = get_object_or_404(rates,pk=1)
    rate = rate_details.rates
    drivings = driver_shop.objects.filter(account=users)
    my_shops = Shops.objects.filter(owner=users)
    manila_timezone = pytz.timezone("Asia/Manila")
    current_time = datetime.now(manila_timezone).strftime('%Y-%m-%d %H:%M:%S')
    current_time_btn = datetime.now(manila_timezone)
    rent = get_object_or_404(Rented_Cars,rent_id=rentid)
    slugs = rent.unit_rented.shop_belong.slug
    proofs = onsitepayment.objects.filter(rent_reference=rent)
    
    context = {
        'page':page,
        'title_page':title_page,
        'users':users,
        'rent_issues':rent_issues,
        'my_shops':my_shops,
        'shops':shops,
        'drivings':drivings,
        'rent':rent,
        'slugs':slugs,
        'proofs':proofs,
        'current_time':current_time,
        'current_time_btn':current_time_btn,
        'rate':rate,
    }
    return render(request,'accounts/rent_details_shop_admin.html',context)


@login_required(login_url='signin')
@role_required(allowed_roles=['1'], redirect_url='users')
def blank(request):
    page = 'blank'
    title_page = 'blank'
    users = request.user
    rent_issues = rent_issue.objects.filter(rent__renters=users)
    context = {
        'page':page,
        'title_page':title_page,
        'users':users,
        'rent_issues':rent_issues,
       
    }
    return render(request, 'accounts/blank.html',context)


@login_required(login_url='signin')
@role_required(allowed_roles=['1'], redirect_url='users')
def list_administrators(request):
    page = 'adminlist'
    title_page = 'Administrator list'
    users = request.user
    rent_issues = rent_issue.objects.filter(rent__renters=users)
    admins = User.objects.filter(roles='1')
    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            add_admin = form.save(commit=False)
            raw_password = form.cleaned_data.get('password1')
            request.session['unverified_email'] =  add_admin.email
            add_admin.username = add_admin.username.lower()
            add_admin.roles = '1'
            add_admin.code = int(get_random_string(length=6, allowed_chars='1234567890'))
            add_admin.save()
            # Send OTP to the user's email
            subject = 'Access Administrative Accounts'
            message = f'''
                        Hi admin, this is ypur administrative credentials
                        Account Email :{add_admin.email} ,
                        Password: {raw_password} ,
                        Your OTP is {add_admin.code}. Enter this code to complete your autherntications.'''
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = add_admin.email
            send_mail(subject, message, from_email, [to_email], fail_silently=False)

            # login(request, user, backend='django.contrib.auth.backends.ModelBackend')  # for Direct log in after registration
            messages.success(request, 'Account Created Successfully')
            return redirect('list_administrators')
        else:
            messages.error(request, 'An error occurred during registration')
    context = {
        'page':page,
        'title_page':title_page,
        'users':users,
        'rent_issues':rent_issues,
        'form': form,
        'admins':admins,
       
    }
    return render(request, 'accounts/administrators.html',context)


@login_required(login_url='signin')
@role_required(allowed_roles=['1'], redirect_url='users')
def list_users(request):
    page = 'userlist'
    title_page = 'User list'
    users = request.user
    rent_issues = rent_issue.objects.filter(rent__renters=users)
    admins = User.objects.filter(roles='2',is_staff="0")
    context = {
        'page':page,
        'title_page':title_page,
        'users':users,
        'rent_issues':rent_issues,
        'admins':admins,
       
    }
    return render(request, 'accounts/users.html',context)


@login_required(login_url='signin')
@role_required(allowed_roles=['1'], redirect_url='users')
def user_details(request,pk):
    details = get_object_or_404(User,pk=pk)
    ishop = Shops.objects.filter(owner=details)
    page = 'userlist'
    title_page = 'User list'
    users = request.user
    rent_issues = rent_issue.objects.filter(rent__renters=users)
    context = {
        'page':page,
        'title_page':title_page,
        'users':users,
        'rent_issues':rent_issues,
        'details':details,
        'ishop':ishop,

       
    }
    return render(request, 'accounts/user_details.html',context)


@login_required(login_url='signin')
@role_required(allowed_roles=['1','2'], redirect_url='logoutUser')
def profile(request):
    users = request.user
    rent_issues = rent_issue.objects.filter(rent__renters=users)
    current_email = users.email
    user_id = users.id
    drivings = driver_shop.objects.filter(account=users)
    my_shops = Shops.objects.filter(owner=users)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=users )
        if form.is_valid():
            form.save()
            messages.success(request, "Saved Successfully")
            return redirect('profile')
        else:
             messages.error(request, "Please Try Again")
    else:
        form = UserForm(instance=users)
    context = {
        'current_email':current_email,
        'form':form,
        'users':users,
        'rent_issues':rent_issues,
        'my_shops':my_shops,
    }
    return render(request, 'accounts/profile.html',context)




@login_required(login_url='signin')
@role_required(allowed_roles=['1'], redirect_url='users')
def payments(request):
    users = request.user
    rent_issues = rent_issue.objects.filter(rent__renters=users)
    page = 'payments'
    title_page = 'Payments'
    payment_details = get_object_or_404(rates,pk=1)
    list_transactions_uncheck = payment_process.objects.filter(status="uncheck").count()
    list_transactions_approved = payment_process.objects.filter(status="approved").count()
    list_transactions = payment_process.objects.all()
    if request.method == 'POST':
        form = rates_form(request.POST, request.FILES,instance=payment_details)
        if form.is_valid():
            pymnt = form.save(commit=False)
            pymnt.save() 
            messages.success(request, "Rates Updated")
            return redirect('payments')
        else:
            print(form.errors) 
            messages.error(request, "Please Try Again")
    else:
        form = rates_form(instance=payment_details)
    
    context = {
        'page':page,
        'title_page':title_page,
        'form':form,
        'users':users,
        'rent_issues':rent_issues,
        'payment_details':payment_details,
        'list_transactions_approved':list_transactions_approved,
        'list_transactions_uncheck':list_transactions_uncheck,
        'list_transactions':list_transactions,

    }
    return render(request,'accounts/payments.html',context)





@login_required(login_url='signin')
@role_required(allowed_roles=['1'], redirect_url='users')
def payments_details(request,refnumber):
    users = request.user
    rent_issues = rent_issue.objects.filter(rent__renters=users)
    page = 'payments'
    admin = 1
    title_page = 'Request Payment Details'
    drivings = driver_shop.objects.filter(account=users)
    my_shops = Shops.objects.filter(owner=users)
    details = get_object_or_404(payment_process,transaction_reference=refnumber)
    list_rent = payment_process_items.objects.filter(payment_root=details)
    context = {
        'page':page,
        'title_page':title_page,
        'users':users,
        'rent_issues':rent_issues,
        'my_shops':my_shops,
        'shops':shops,
        'drivings':drivings,
        'details':details,
        'list_rent':list_rent,
        'admin':admin,

    }
    return render(request,'accounts/payment_transaction_details.html',context)



@login_required(login_url='signin')
@role_required(allowed_roles=['1'], redirect_url='users')
def shops(request):
    users = request.user
    rent_issues = rent_issue.objects.filter(rent__renters=users)
    page = 'regshops'
    title_page = 'Registered Shops'


    list_shops = Shops.objects.all()
    
    context = {
        'page':page,
        'title_page':title_page,
        'users':users,
        'rent_issues':rent_issues,
        'list_shops':list_shops,

    }
    return render(request,'accounts/shops.html',context)

@login_required(login_url='signin')
@role_required(allowed_roles=['1'], redirect_url='users')
def shops_details(request, pk):
    users = request.user
    rent_issues = rent_issue.objects.filter(rent__renters=users)
    details_shop = get_object_or_404(Shops,pk=pk)
    car_count = Vehicle.objects.filter(shop_belong=details_shop).count()
    driver_count = driver_shop.objects.filter(shop_under=details_shop).count()
    page = 'regshops'
    title_page = 'Shop Details'
    
    context = {
        'page':page,
        'title_page':title_page,
        'users':users,
        'rent_issues':rent_issues,
        'details_shop':details_shop,
        'car_count':car_count,
        'driver_count':driver_count

    }
    return render(request,'accounts/shop_details.html',context)




@login_required(login_url='signin')
@role_required(allowed_roles=['1'], redirect_url='users')
def vehicles_list(request):
    users = request.user
    rent_issues = rent_issue.objects.filter(rent__renters=users)
    page = 'regcars'
    title_page = 'Registered Cars'


    list_vehicles = Vehicle.objects.all()
    
    context = {
        'page':page,
        'title_page':title_page,
        'users':users,
        'rent_issues':rent_issues,
        'list_vehicles':list_vehicles,

    }
    return render(request,'accounts/vehicles_list.html',context)



@login_required(login_url='signin')
@role_required(allowed_roles=['1'], redirect_url='users')
def unlock_shops(request, pk):
    shop_details = get_object_or_404(Shops, pk=pk)
    if shop_details.status == 'lock':
        shop_details.status = 'published'
        shop_details.save()
        messages.success(request, "Shop published")
    else:
        shop_details.status = 'lock'
        shop_details.save()
        messages.success(request, "Shop set to lock")
    return redirect('shops_details', pk)

@login_required(login_url='signin')
@role_required(allowed_roles=['1'], redirect_url='users')
def published_cars(request, pk):
    car_details = get_object_or_404(Vehicle, pk=pk)
    if car_details.status == 'uncheck':
        car_details.status = 'published'
        car_details.save()
        messages.success(request, "Car registration approved")
    else:
        car_details.status = 'uncheck'
        car_details.save()
        messages.success(request, "Car registration disapprove")
    return redirect('vehicles_list')
#============================================================================================================


@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def users(request):

    controlsite = get_object_or_404(controls, pk=1)
    if controlsite.control == 1:
        return redirect(controlsite.site)
    
    
    users = request.user
    rent_issues = rent_issue.objects.filter(rent__renters=users)
    rent_issues = rent_issue.objects.filter(rent__renters=users)
    page = 'homedashboard'
    title_page = 'Prime Cars'
    drivings = driver_shop.objects.filter(account=users)
    my_shops = Shops.objects.filter(owner=users)
    registred_shops = Shops.objects.filter(status="published")[:12]
    rented_cars = Rented_Cars.objects.filter(renters=users)

    context = {
        'page':page,
        'title_page':title_page,
        'users':users,
        'rent_issues':rent_issues,
        'my_shops':my_shops, 
        'registred_shops':registred_shops,
        'rented_cars':rented_cars,
        'rent_issues':rent_issues,
        'drivings':drivings,
    }
    return render(request, 'accounts/index_users.html',context)

@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def myshops(request):
    users = request.user
    rent_issues = rent_issue.objects.filter(rent__renters=users)
    page = 'myshops'
    title_page = 'My Shops'
    drivings = driver_shop.objects.filter(account=users)
    my_shops = Shops.objects.filter(owner=users)
    
    if request.method == 'POST':
        form = ShopForm(request.POST, request.FILES)
        if form.is_valid():
            shop = form.save(commit=False)  # Don't save to the database yet
            shop.owner = users  # Set the owner to the logged-in user
            shop.save()  # Now save to the database
            messages.success(request, "Saved Successfully")
            return redirect('myshops')
        else:
            print(form.errors)  # Print form errors to debug
            messages.error(request, "Please Try Again")
    else:
        form = ShopForm()

    context = {
        'page': page,
        'title_page': title_page,
        'users': users,
        'form': form,
        'my_shops': my_shops,
        'drivings':drivings,
    }
    return render(request, 'accounts/myshops.html', context)




@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def edit_myshops(request,slug):
    users = request.user
    rent_issues = rent_issue.objects.filter(rent__renters=users)
    page = 'myslistshop'
    title_page = 'Edit Shop details'
    drivings = driver_shop.objects.filter(account=users)
    my_shops = Shops.objects.filter(owner=users)
    shop_instance = get_object_or_404(Shops,slug=slug)
    if request.method == 'POST':
        form = ShopForm(request.POST, request.FILES,instance=shop_instance)
        if form.is_valid():
            shop = form.save(commit=False) # Don't save to the database yet
            shop.status = 'lock'
            new_slug = slugify(shop.shop_name)
            shop.slug = new_slug
            shop.owner = users  # Set the owner to the logged-in user
            shop.save()  # Now save to the database
            messages.success(request, "Saved Successfully")
            return redirect('mylistshop')
        else:
            messages.error(request, "Please Try Again")
    else:
        form = ShopForm(instance=shop_instance)

    context = {
        'page': page,
        'title_page': title_page,
        'users': users,
        'form': form,
        'my_shops':my_shops,
        'shop_instance':shop_instance,
        'drivings':drivings,
    }
    return render(request, 'accounts/myshops.html', context)


@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def delete_myshops(request, slug):
    shop_del = get_object_or_404(Shops, slug=slug)
    shop_del.delete()
    messages.success(request, "Shop Deleted successfully")
    return redirect('mylistshop')

@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def mylistshop(request):
    users = request.user
    rent_issues = rent_issue.objects.filter(rent__renters=users)
    page = 'myslistshop'
    title_page = 'My Shops'
    drivings = driver_shop.objects.filter(account=users)
    my_shops = Shops.objects.filter(owner=users)

    context = {
        'page':page,
        'title_page':title_page,
        'users':users,
        'rent_issues':rent_issues,
        'my_shops':my_shops, 
        'drivings':drivings,
    }
    return render(request, 'accounts/mylistshop.html',context)


@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def registered_shops(request):
    users = request.user
    rent_issues = rent_issue.objects.filter(rent__renters=users)
    page = 'regshops'
    title_page = 'Registered Shops'
    drivings = driver_shop.objects.filter(account=users)
    my_shops = Shops.objects.filter(owner=users)
    registred_shops = Shops.objects.filter(status="published")

    context = {
        'page':page,
        'title_page':title_page,
        'users':users,
        'rent_issues':rent_issues,
        'my_shops':my_shops, 
        'registred_shops':registred_shops,
        'drivings':drivings,
    }
    return render(request, 'accounts/registered_shops.html',context)


@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def details_shops(request,slug):
    users = request.user
    rent_issues = rent_issue.objects.filter(rent__renters=users)
    if rent_issues:
        messages.error(request, "You are not authorized to rent")
        return redirect('users')
    details_shop = get_object_or_404(Shops,slug=slug)
    shopname = details_shop.shop_name
    page = 'regshops'
    title_page = shopname


    drivings = driver_shop.objects.filter(account=users)
    my_shops = Shops.objects.filter(owner=users)
    registred_shops = Shops.objects.filter(status="published")
    approve_driver = driver_shop.objects.filter(shop_under=details_shop,status=1)
    driver_aplication = driver_shop.objects.filter(account=users)
    droptyple = Vehicle.objects.all()
    if request.method=="POST":
        searchbrand= request.POST.get('brand')
        searchfuel = request.POST.get('fuel')
        searchseat = request.POST.get('seat')
        searchtransmission= request.POST.get('transmission')
        vehicles = Vehicle.objects.filter(shop_belong=details_shop,categories=searchbrand,fuels=searchfuel,seat=searchseat,transmission=searchtransmission)
    else:
        vehicles = Vehicle.objects.filter(shop_belong=details_shop)

    paginator = Paginator(vehicles, 3)  
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    paginator_approve_driver = Paginator(approve_driver, 8)  
    page_number_driver = request.GET.get("drivers")
    page_obj_driver = paginator_approve_driver.get_page(page_number_driver)
    context = {
        'page':page,
        'title_page':title_page,
        'users':users,
        'rent_issues':rent_issues,
        'my_shops':my_shops, 
        'registred_shops':registred_shops,
        'details_shop':details_shop,
        'vehicles':vehicles,
        'droptyple':droptyple,
        'page_obj':page_obj,
        'slug':slug,
        'page_obj_driver':page_obj_driver,
        'Brands':Brands,
        'fuel_types':fuel_types,
        'seat':seat,
        'transmission':transmission,
        'driver_aplication':driver_aplication,
        'drivings':drivings,
        
    }
    return render(request, 'accounts/detail_registered_shops.html',context)


@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def myshop_details(request,slug):
    users = request.user
    rent_issues = rent_issue.objects.filter(rent__renters=users)
    page = 'myslistshop'
    title_page = 'Shop Details'
    drivings = driver_shop.objects.filter(account=users)
    manila_timezone = pytz.timezone("Asia/Manila")
    current_time = datetime.now(manila_timezone).strftime('%Y-%m-%d %H:%M:%S')
    
    mth = datetime.now(manila_timezone).strftime('%b')
    yrs = datetime.now(manila_timezone).strftime('%Y')
    my_shops = Shops.objects.filter(owner=users)
    shops = get_object_or_404(Shops,slug=slug)
    count_vehicles = Vehicle.objects.filter(shop_belong=shops).count()
    count_not_approve = driver_shop.objects.filter(shop_under=shops ,status=0).count()
    drivers_list = driver_shop.objects.filter(shop_under=shops,status=1)
    count_approve = driver_shop.objects.filter(shop_under=shops,status=1).count()
    rented_cars = Rented_Cars.objects.filter(unit_rented__shop_belong__in=my_shops) 

    rented_cars_processing = Rented_Cars.objects.filter(unit_rented__shop_belong__in=my_shops,status__in=["pending","unpaid"])
    rented_cars_release = Rented_Cars.objects.filter(unit_rented__shop_belong__in=my_shops,unit_release__in=[2,3])
    rented_cars_reviews = Rented_Cars.objects.filter(unit_rented__shop_belong__in=my_shops,rating_bolean__in=[1,2])
    rented_cars_transaction = Rented_Cars.objects.filter(unit_rented__shop_belong__in=my_shops,transaction_done=1)
    rented_cars_issues = Rented_Cars.objects.filter(unit_rented__shop_belong__in=my_shops,issues=1)
    monthly_counts = Rented_Cars.objects.filter(yr=yrs,transaction_done=1,excess_exist=0, unit_rented__shop_belong=shops).values('mth').annotate(total_fare=Sum('total_fare')).order_by('sqc')
    unclaimed_transactions_count = Rented_Cars.objects.filter(unit_rented__shop_belong=shops,status="paid",excess_exist=0,liquidated=0).count
    payment_request_count = Rented_Cars.objects.filter(unit_rented__shop_belong=shops,drivers_approval="payout").count
    context = {
        'page':page,
        'title_page':title_page,
        'users':users,
        'rent_issues':rent_issues,
        'my_shops':my_shops,
        'shops':shops,
        'count_vehicles':count_vehicles,
        'count_not_approve':count_not_approve,
        'drivers_list':drivers_list,
        'count_approve':count_approve,
        'rented_cars':rented_cars,
        'rented_cars_processing':rented_cars_processing,
        'rented_cars_release':rented_cars_release,
        'rented_cars_transaction':rented_cars_transaction,
        'rented_cars_issues':rented_cars_issues,
        'drivings':drivings,
        'monthly_counts':monthly_counts,
        'unclaimed_transactions_count':unclaimed_transactions_count,
        'current_time':current_time,
        'payment_request_count':payment_request_count,
        'rented_cars_reviews':rented_cars_reviews,
    }
    return render(request,'accounts/myshop_details.html',context)





@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def drivers_payout(request,slug):
    users = request.user
    rent_issues = rent_issue.objects.filter(rent__renters=users)
    page = 'myslistshop'
    title_page = 'Drivers Payout Request'
    drivings = driver_shop.objects.filter(account=users)
    my_shops = Shops.objects.filter(owner=users)
    shops = get_object_or_404(Shops,slug=slug)
    list_payout = Rented_Cars.objects.filter(unit_rented__shop_belong=shops,drivers_approval="payout")
    context = {
        'page':page,
        'title_page':title_page,
        'users':users,
        'rent_issues':rent_issues,
        'my_shops':my_shops,
        'shops':shops,
        'slug':slug,
        'drivings':drivings,
        'list_payout':list_payout,
    }
    return render(request,'accounts/drivers_payout.html',context)




@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def myshop_payment_details(request,slug):
    users = request.user
    rent_issues = rent_issue.objects.filter(rent__renters=users)
    page = 'myslistshop'
    title_page = 'Shop payment details'
    drivings = driver_shop.objects.filter(account=users)
    my_shops = Shops.objects.filter(owner=users)
    shops = get_object_or_404(Shops,slug=slug)
    list_payment = payment_process.objects.all()
    unclaimed_transactions_online = Rented_Cars.objects.filter(unit_rented__shop_belong=shops,status="paid",excess_exist=0,liquidated=0,transaction_done=1,payment_choice=2)
    unclaimed_transactions_onsite = Rented_Cars.objects.filter(unit_rented__shop_belong=shops,status="paid",excess_exist=0,liquidated=0,transaction_done=1,payment_choice=1)
    total_online = 0
    total_onsite = 0
    
    for online in unclaimed_transactions_online:
        minus = online.total_fare - online.share_rates
        total_online = total_online + minus

    for onsite in unclaimed_transactions_onsite:
        onsite_minus = onsite.total_fare - onsite.share_rates
        total_onsite = total_onsite + onsite_minus
    # unclaimed_transactions_online_sum = Rented_Cars.objects.filter(unit_rented__shop_belong=shops,status="paid",excess_exist=0,liquidated=0,transaction_done=1,payment_choice=2).aggregate(total_fare_sum=Sum('total_fare'))
    # unclaimed_transactions_onsite_sum = Rented_Cars.objects.filter(unit_rented__shop_belong=shops,status="paid",excess_exist=0,liquidated=0,transaction_done=1,payment_choice=1).aggregate(total_fare_sum=Sum('total_fare'))


    context = {
        'page':page,
        'title_page':title_page,
        'users':users,
        'rent_issues':rent_issues,
        'slug':slug,
        'my_shops':my_shops,
        'drivings':drivings,
        'shops':shops,
        'unclaimed_transactions_online':unclaimed_transactions_online,
        'unclaimed_transactions_onsite':unclaimed_transactions_onsite,
        # 'unclaimed_transactions_online_sum': unclaimed_transactions_online_sum.get('total_fare_sum', 0),
        # 'unclaimed_transactions_onsite_sum': unclaimed_transactions_onsite_sum.get('total_fare_sum', 0),
        'total_online':total_online,
        'total_onsite':total_onsite,
        'list_payment':list_payment
    }
    return render(request,'accounts/shop_payments.html',context)



@login_required(login_url='signin')
@role_required(allowed_roles=['1'], redirect_url='users')
def payments_request_approved(request,pk):
    pay = get_object_or_404(payment_process,pk=pk)
    pay.status = "approved"
    pay.save()
    messages.success(request, "Paid Succefully")
    return redirect('payments') 


@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def Request_payment(request,slug):
    shops = get_object_or_404(Shops,slug=slug)
    unclaimed_transactions_online = Rented_Cars.objects.filter(unit_rented__shop_belong=shops,status="paid",excess_exist=0,liquidated=0,transaction_done=1,payment_choice=2)
    total_online = 0
    for online in unclaimed_transactions_online:
        minus = online.total_fare - online.share_rates
        total_online = total_online + minus

        online.liquidated = 1
        online.save()

    payment_process_record = payment_process.objects.create(
        shop_processed=shops,
        amount=total_online,
        transaction_type=2,
        category="request"
    )

    for online_save in unclaimed_transactions_online:
        payment_process_items.objects.create(
            payment_root=payment_process_record,
            rent_transactions=online_save
        )
    messages.success(request, "Payment Requested")
    return redirect('myshop_payment_details', slug=slug) 



@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def Submit_payment(request,slug):
    shops = get_object_or_404(Shops,slug=slug)
    unclaimed_transactions_onsite = Rented_Cars.objects.filter(unit_rented__shop_belong=shops,status="paid",excess_exist=0,liquidated=0,transaction_done=1,payment_choice=1)
    total_onsite= 0
    for onsite in unclaimed_transactions_onsite:
        minus = onsite.total_fare - onsite.share_rates
        total_onsite = total_onsite + minus

        onsite.liquidated = 1
        onsite.save()

    payment_process_record = payment_process.objects.create(
        shop_processed=shops,
        amount=total_onsite,
        transaction_type=1,
        status="approved",
        category="Submission"
    )

    for online_save in unclaimed_transactions_onsite:
        payment_process_items.objects.create(
            payment_root=payment_process_record,
            rent_transactions=online_save
        )
    messages.success(request, "Payment Requested")
    return redirect('myshop_payment_details', slug=slug) 


@login_required(login_url='signin')
@role_required(allowed_roles=['1','2'], redirect_url='logoutUser')
def payment_transaction_details(request,tref):
    users = request.user
    rent_issues = rent_issue.objects.filter(rent__renters=users)
    page = 'myslistshop'
    title_page = 'Shop Details'
    drivings = driver_shop.objects.filter(account=users)
    my_shops = Shops.objects.filter(owner=users)
    details = get_object_or_404(payment_process,transaction_reference=tref)
    list_rent = payment_process_items.objects.filter(payment_root=details)
    admin = 0
    context = {
        'page':page,
        'title_page':title_page,
        'users':users,
        'rent_issues':rent_issues,
        'my_shops':my_shops,
        'shops':shops,
        'drivings':drivings,
        'details':details,
        'list_rent':list_rent,
        'admin':admin
    }
    return render(request,'accounts/payment_transaction_details.html',context)


@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def rent_details_shop(request,rentid):
    users = request.user
    rent_issues = rent_issue.objects.filter(rent__renters=users)
    page = 'myslistshop'
    title_page = 'Shop Details'
    rate_details = get_object_or_404(rates,pk=1)
    rate = rate_details.rates
    drivings = driver_shop.objects.filter(account=users)
    my_shops = Shops.objects.filter(owner=users)
    manila_timezone = pytz.timezone("Asia/Manila")
    current_time = datetime.now(manila_timezone).strftime('%Y-%m-%d %H:%M:%S')
    current_time_btn = datetime.now(manila_timezone)
    rent = get_object_or_404(Rented_Cars,rent_id=rentid)
    slugs = rent.unit_rented.shop_belong.slug
    proofs = onsitepayment.objects.filter(rent_reference=rent)
    
    context = {
        'page':page,
        'title_page':title_page,
        'users':users,
        'rent_issues':rent_issues,
        'my_shops':my_shops,
        'shops':shops,
        'drivings':drivings,
        'rent':rent,
        'slugs':slugs,
        'proofs':proofs,
        'current_time':current_time,
        'current_time_btn':current_time_btn,
        'rate':rate,
    }
    return render(request,'accounts/rent_details_shop.html',context)



@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def report_issues(request,pk):
    users = request.user
    rent_issues = rent_issue.objects.filter(rent__renters=users)
    page = 'myslistshop'
    title_page = 'report issues'
    rent_details = get_object_or_404(Rented_Cars,pk=pk)
    list_issue = rent_issue.objects.filter(rent=rent_details)
    total = 0
    for issiue in list_issue:
        total = total + issiue.issue_amount
    if rent_details.issues == 0:
        rent_details.issues = 1
        rent_details.save()
    elif rent_details.issues == 1:
        rent_details.total_cost_issue = total
        rent_details.save()

    if request.method == 'POST':
        form = rent_issue_form(request.POST, request.FILES)
        if form.is_valid():
            issue = form.save(commit=False)  # Don't save to the database yet
            issue.rent = rent_details
            issue.save()
            messages.success(request, "Saved issue report")
            return redirect('report_issues', pk=pk)
       
        else:
            print(form.errors)  # Debug form errors
            messages.error(request, "Please Try Again")
    else:
        form = rent_issue_form()
    
    context = {
        'page':page,
        'title_page':title_page,
        'users':users,
        'rent_issues':rent_issues,
        'form':form,
        'rent_details':rent_details,
        'list_issue':list_issue,
        'total':total,
            #list issue view modal and delete 
    }
    return render(request,'accounts/issues.html',context)


@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def report_issues_deleted(request,pk):
    users = request.user
    rent_issues = rent_issue.objects.filter(rent__renters=users)
    delete_detail = get_object_or_404(rent_issue,pk=pk)
    r_id = delete_detail.rent.id
    delete_detail.delete()
    messages.success(request, "Delete Successfully")
    return redirect('report_issues', pk=r_id)
   


@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def all_report_issues_deleted(request,pk):
    users = request.user
    rent_issues = rent_issue.objects.filter(rent__renters=users)
    rent_details = get_object_or_404(Rented_Cars,pk=pk)
    r_id= rent_details.rent_id
    list_issue = rent_issue.objects.filter(rent=rent_details)
    list_issue.delete()
    rent_details.issues = 0
    rent_details.save()
    messages.success(request, "Delete all records successfully")
    return redirect('rent_details_shop', rentid=r_id)  

@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def vehicles(request, slug):
    users = request.user
    rent_issues = rent_issue.objects.filter(rent__renters=users)
    page = 'myslistshop'
    title_page = 'Vehicles'
    drivings = driver_shop.objects.filter(account=users)
    my_shops = Shops.objects.filter(owner=users)
    shops = get_object_or_404(Shops, slug=slug)
    shopID = shops.id
    garage = Vehicle.objects.filter(shop_belong=shopID)
    
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            ve = form.save(commit=False)  # Don't save to the database yet
            ve.shop_belong = shops
            ve.save()  # Now save to the database
            messages.success(request, "Saved Successfully")
            return redirect('vehicles',slug)
        else:
            print(form.errors)  # Debug form errors
            messages.error(request, "Please Try Again")
    else:
        form = VehicleForm()

    context = {
        'page': page,
        'title_page': title_page,
        'users': users,
        'my_shops': my_shops,
        'drivings':drivings,
        'shops': shops,
        'form': form,
        'slug':slug,
        'garage':garage
    }
    return render(request, 'accounts/vehicles.html', context)



@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def shopdrivers(request, slug):
    users = request.user
    rent_issues = rent_issue.objects.filter(rent__renters=users)
    page = 'regshops'
    title_page = 'Driver Registration '
    drivings = driver_shop.objects.filter(account=users)
    my_shops = Shops.objects.filter(owner=users)
    shops = get_object_or_404(Shops, slug=slug)
    shopID = shops.id
    garage = Vehicle.objects.filter(shop_belong=shopID)
    check_driver = driver_shop.objects.filter(shop_under=shops,account=users)
   

    if request.method == 'POST':
        form = DriverForm(request.POST, request.FILES)
        if form.is_valid():
            driver = form.save(commit=False)  # Don't save to the database yet
            driver.account = users
            driver.shop_under = shops
            driver.save()  # Now save to the database
            messages.success(request, "Saved Successfully")
            return redirect('shopdrivers',slug)
        else:
            print(form.errors)  # Debug form errors
            messages.error(request, "Please Try Again")
    else:
        form = DriverForm()

    context = {
        'page': page,
        'title_page': title_page,
        'users': users,
        'my_shops': my_shops,
        'drivings':drivings,
        'shops': shops,
        'form': form,
        'slug':slug,
        'garage':garage,
        'check_driver':check_driver,
        
    }
    return render(request, 'accounts/shopdrivers.html', context)


@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def edit_vehicles(request, slug, pk):
    users = request.user
    rent_issues = rent_issue.objects.filter(rent__renters=users)
    page = 'myslistshop'
    title_page = 'Vehicles'
    drivings = driver_shop.objects.filter(account=users)
    my_shops = Shops.objects.filter(owner=users)
    shops = get_object_or_404(Shops, slug=slug)
    shopID = shops.id
    garage = Vehicle.objects.filter(shop_belong=shopID)
    vehicle = get_object_or_404(Vehicle, pk=pk, shop_belong=shops) 
    
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES, instance=vehicle)
        if form.is_valid():
            ve = form.save(commit=False) 
            ve.shop_belong = shops
            ve.status = "uncheck"  # Assign the Shops object itself
            ve.save()  
            messages.success(request, "Vehicle updated successfully")
            return redirect('vehicles', slug=slug)  
        else:
            print(form.errors)  # For debugging form errors
            messages.error(request, "Please try again")
    else:
        form = VehicleForm(instance=vehicle)

    context = {
        'page': page,
        'title_page': title_page,
        'users': users,
        'my_shops': my_shops,
        'shops': shops,
        'form': form,
        'drivings':drivings,
        'slug':slug,
        'garage': garage,
    }

    return render(request, 'accounts/vehicles.html', context)


@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def mydrivers(request, slug):
    users = request.user
    rent_issues = rent_issue.objects.filter(rent__renters=users)
    page = 'myslistshop'
    title_page = 'My Drivers'
    drivings = driver_shop.objects.filter(account=users)
    my_shops = Shops.objects.filter(owner=users)
    shops = get_object_or_404(Shops, slug=slug)
    shopID = shops.id
    garage = Vehicle.objects.filter(shop_belong=shopID)
    aply_drivers = driver_shop.objects.filter(shop_under=shops,status=0)
    reg_drivers = driver_shop.objects.filter(shop_under=shops, status__in=[1, 2, 3, 4])
    check_driver = driver_shop.objects.filter(shop_under=shops,account=users)
    context = {
        'page': page,
        'title_page': title_page,
        'my_shops':my_shops,
        'aply_drivers':aply_drivers,
        'drivings':drivings,
        'reg_drivers':reg_drivers,
        'slug':slug,
        'users':users
    }
    return render(request, 'accounts/drivers.html', context)

@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def approved_driver(request, slug, pk):
    shop_details = get_object_or_404(Shops, slug=slug) 
    driver_approved = get_object_or_404(driver_shop, pk=pk)
    email = driver_approved.account.email
    shop_name = shop_details.shop_name
    address = shop_details.address
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = email
    
    
    if driver_approved.status == 1:
        subject = 'Driver Status Updated'
        message = f'''
            Good Day to our skillfull driver of our shop {shop_name}, we are notifying you that your account is temporarily 
            dismmised, please visit to our office at {address} for further information.'''
        driver_approved.status = 2
        messages.success(request, "Driver Status Temporary dismissed")
    elif driver_approved.status == 2:
        subject = 'Driver Registration Re-Approved'
        message = f'''
            Congratulations your status as driver in our shop "{shop_name}" is re-deployed.
            please visit to our office at {address} for further information.'''
        driver_approved.status = 1
        messages.success(request, "Driver Status Re-deployed")
    else:
        subject = 'Driver Registration Approved'
        message = f'''
            Congratulations your registration as driver in our shop "{shop_name}" is approved.
            please visit to our office at {address} for further information.'''
        driver_approved.status = 1
        messages.success(request, "Driver Registration Approved")

    send_mail(subject, message, from_email, [to_email], fail_silently=False)
    driver_approved.save()  
    return redirect('mydrivers', slug=slug)


@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def delete_driver(request, slug, pk):
    driver_delete = get_object_or_404(driver_shop, pk=pk)
    shop_details = get_object_or_404(Shops, slug=slug) 
    email = driver_delete.account.email
    shop_name = shop_details.shop_name
    address = shop_details.address
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = email
    subject = 'Driver Registration Denied'
    message = f'''
            Hi to our aspring driver to this shop "{shop_name}", we are humbly to say that, 
            we disapproved your driver aplications, due to some reason like,
            1, data are not match in drivers licence.
            2, unrealistic input in application.

            please visit to our office at {address} for further information.'''
    send_mail(subject, message, from_email, [to_email], fail_silently=False)
    messages.success(request, "Driver Denied")
    driver_delete.delete() 
    return redirect('mydrivers', slug=slug)

@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def account_lock_driver(request,pk):
    lock_account = get_object_or_404(driver_shop, pk=pk)
    if lock_account.status == 1:
        lock_account.status = 3
        message = "Lock"
    else:
        lock_account.status = 1
        message = "Unlock"
    lock_account.save()  
    messages.success(request, "Succesfully " + message)
    return redirect('mydrivingshops')


@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def account_removal_driver(request,pk):
    lock_account = get_object_or_404(driver_shop, pk=pk)
    if lock_account.status != 4:
        lock_account.status = 4
        message = "Removal requested"
    else:
        lock_account.status = 3
        message = "Removal cancelled"
    lock_account.save()  
    messages.success(request, "" + message)
    return redirect('mydrivingshops')



@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def delete_vehicles(request, slug, pk):
    vehicle_delete = get_object_or_404(Vehicle, pk=pk) 
    vehicle_delete.delete()  
    messages.success(request, "Vehicle deleted successfully")
    return redirect('vehicles', slug=slug) 









@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def shop_unit(request, slug , pk):
    users = request.user
    rent_issues = rent_issue.objects.filter(rent__renters=users)
    cars = get_object_or_404(Vehicle, pk=pk)
    cars_name = cars.categories
    page = 'regshops'
    title_page = cars_name
    drivings = driver_shop.objects.filter(account=users)
    my_shops = Shops.objects.filter(owner=users)
    details_shop = get_object_or_404(Shops,slug=slug)
    check_car = Rented_Cars.objects.filter(unit_rented=cars, status__in=["approved", "paid", "unpaid"] ).exclude(unit_release=1)
    ratings = Rented_Cars.objects.filter(unit_rented=cars, rating_bolean__in=[2,3])
    context = {
        'page':page,
        'title_page':title_page,
        'users':users,
        'rent_issues':rent_issues,
        'my_shops':my_shops, 
        'details_shop':details_shop,
        'drivings':drivings,
        'slug':slug,
        'cars':cars,
        'check_car':check_car,
        'ratings':ratings,
    }
    return render(request, 'accounts/shopunit.html',context)


@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def registered_vehicles(request):
    users = request.user
    rent_issues = rent_issue.objects.filter(rent__renters=users)
    page = 'regcars'
    title_page = 'Registered Cars'
    drivings = driver_shop.objects.filter(account=users)
    my_shops = Shops.objects.filter(owner=users)
    if request.method=="POST":
        searchbrand= request.POST.get('brand')
        searchseat = request.POST.get('seat')
        searchtransmission= request.POST.get('transmission')
        vehicles = Vehicle.objects.filter(
            Q(categories=searchbrand) | 
            Q(seat=searchseat) | 
            Q(transmission=searchtransmission)
        ).exclude(status="uncheck")
    else:
        vehicles = Vehicle.objects.exclude(status="uncheck")

    paginator = Paginator(vehicles, 3)  
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'page':page,
        'title_page':title_page,
        'users':users,
        'rent_issues':rent_issues,
        'my_shops':my_shops,
        'page_obj':page_obj,
        'Brands':Brands,
        'fuel_types':fuel_types,
        'drivings':drivings,
        'seat':seat,
        'transmission':transmission,
    }
    return render(request, 'accounts/registered_vehicles.html',context)














@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def rent_vehicles(request, pk):
    users = request.user
    rent_issues = rent_issue.objects.filter(rent__renters=users)
    if rent_issues:
        messages.error(request, "You are not authorized to rent")
        return redirect('users')
    cars = get_object_or_404(Vehicle, pk=pk)
    rate_details = get_object_or_404(rates,pk=1)
    rate = rate_details.rates
    unit = pk
    manila_timezone = pytz.timezone("Asia/Manila")
    mth = datetime.now(manila_timezone).strftime('%b')
    yrs = datetime.now(manila_timezone).strftime('%Y')
    if mth == 'Jan':
        sqc = 1
    elif mth == 'Feb':
        sqc = 2
    elif mth == 'Mar':
        sqc = 3
    elif mth == 'Apr':
        sqc = 4
    elif mth == 'May':
        sqc = 5
    elif mth == 'Jun':
        sqc = 6
    elif mth == 'Jul':
        sqc = 7
    elif mth == 'Aug':
        sqc = 8
    elif mth == 'Sep':
        sqc = 9
    elif mth == 'Oct':
        sqc = 10
    elif mth == 'Nov':
        sqc = 11
    elif mth == 'Dec':
        sqc = 12


    current_time = now()
    check_spamming = Rented_Cars.objects.filter(renters=users,unit_rented=cars,status="pending").count()
    if check_spamming > 0:
        messages.error(request, "You rented that car already")
        return redirect('registered_vehicles')
        
    else:
        car_hourly_rate  = cars.rent_per_hr
        carshop = cars.shop_belong.id
        shop_detail = get_object_or_404(Shops, pk=carshop)
        car_name = cars.categories
        drivings = driver_shop.objects.filter(account=users)
        my_shops = Shops.objects.filter(owner=users)
        page = 'regcars'
        title_page = "Rent " + car_name
        
        if request.method == 'POST':
            form = Rented_CarsForm(request.POST, request.FILES)
            if form.is_valid():
                rented = form.save(commit=False)  
                rented.renters = users
                rented.unit_rented = cars
                
                driver_id = request.POST.get('driver_shp')
                if driver_id: 
                    driver_details = driver_shop.objects.get(id=driver_id)
                    hourly_rate = driver_details.drivers_rate
                    rented.driver_shp = driver_details
                else:
                    hourly_rate = 0
                if rented.pick_up_unit > current_time :
                    if rented.return_unit > rented.pick_up_unit:
                        duration = rented.return_unit - rented.pick_up_unit
                    else:
                        messages.error(request, "Set time Correctly,please try again")
                        return redirect('rent_vehicles', pk=pk)
                else:
                    messages.error(request, "Set time Correctly,please try again")
                    return redirect('rent_vehicles', pk=pk)

                total_hours = duration.total_seconds() / 3600

                combine_rate = hourly_rate + car_hourly_rate
                if driver_id: 
                    combine_drivers_rate = hourly_rate * total_hours
                else:
                    combine_drivers_rate = 0
                combine_car_rate = car_hourly_rate * total_hours
                total_cost = combine_rate * total_hours
                charge_rate = rate / 100  
                total_after_charge = combine_car_rate - (combine_car_rate * charge_rate)
                charge_rate_total = combine_car_rate - total_after_charge

                rented.share_rates = charge_rate_total
                rented.total_hrs = total_hours 
                rented.total_fare = total_cost
                rented.car_fee_total = total_after_charge 
                rented.driver_fee_total = combine_drivers_rate
                rented.mth = mth
                rented.yr = yrs
                rented.sqc = sqc
                rented.save() 
                messages.success(request, "Successfully Transactions")
                return redirect('users')
            else:
                messages.error(request, "Please try again.")
        else:
            form = Rented_CarsForm()

    context = {
        'page': page,
        'title_page': title_page,
        'my_shops': my_shops,
        'shop_detail': shop_detail,
        'car_name': car_name,
        'drivings':drivings,
        'cars': cars,
        'form': form,
        'current_time':current_time,
        'users':users,
        'rent_issues':rent_issues,
        'unit':unit,
        'mth':mth,
        'yrs':yrs

    }
    
    return render(request, 'accounts/rent_cars.html', context)





@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def rent_vehicles_edit(request, unit, renteid):
    users = request.user
    rent_issues = rent_issue.objects.filter(rent__renters=users)
    cars = get_object_or_404(Vehicle, pk=unit)
    rentdetails = get_object_or_404(Rented_Cars, pk=renteid)
    current_time = now()
    car_hourly_rate  = cars.rent_per_hr
    carshop = cars.shop_belong.id
    shop_detail = get_object_or_404(Shops, pk=carshop)
    car_name = cars.categories
    drivings = driver_shop.objects.filter(account=users)
    my_shops = Shops.objects.filter(owner=users)
    page = 'regcars'
    title_page = "Rent " + car_name
    rate_details = get_object_or_404(rates,pk=1)
    rate = rate_details.rates
        
    if request.method == 'POST':
        form = Rented_CarsForm(request.POST, request.FILES, instance=rentdetails)
        if form.is_valid():
            rented = form.save(commit=False)  
            rented.renters = users
            rented.unit_rented = cars
                
            driver_id = request.POST.get('driver_shp')
            if driver_id: 
                    driver_details = driver_shop.objects.get(id=driver_id)
                    hourly_rate = driver_details.drivers_rate
                    rented.driver_shp = driver_details
            else:
                    hourly_rate = 0
            if rented.pick_up_unit > current_time :
                if rented.return_unit > rented.pick_up_unit:
                        duration = rented.return_unit - rented.pick_up_unit
                else:
                    messages.error(request, "Set time Correctly,please try again")
                    return redirect('rent_vehicles', pk=unit)
            else:
                messages.error(request, "Set time Correctly,please try again")
                return redirect('rent_vehicles', pk=unit)

            total_hours = duration.total_seconds() / 3600

            combine_rate = hourly_rate + car_hourly_rate
            if driver_id: 
                combine_drivers_rate = hourly_rate * total_hours
            else:
                combine_drivers_rate = 0
            combine_car_rate = car_hourly_rate * total_hours
            total_cost = combine_rate * total_hours
            charge_rate = rate / 100  
            total_after_charge = combine_car_rate - (combine_car_rate * charge_rate)
            charge_rate_total = combine_car_rate - total_after_charge

            rented.share_rates = charge_rate_total
            rented.total_hrs = total_hours 
            rented.total_fare = total_cost
            rented.car_fee_total = total_after_charge 
            rented.driver_fee_total = combine_drivers_rate
            rented.save()  
            messages.success(request, "Successfully Transactions")
            return redirect('users')
        else:
            messages.error(request, "Please try again.")
    else:
        form = Rented_CarsForm(instance=rentdetails)
    
    context = {
        'page': page,
        'title_page': title_page,
        'my_shops': my_shops,
        'shop_detail': shop_detail,
        'drivings':drivings,
        'car_name': car_name,
        'cars': cars,
        'form': form,
        'current_time':current_time,
        'users':users,
        'rent_issues':rent_issues,
    }
    
    return render(request, 'accounts/rent_cars.html', context)




@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def driverdetails(request,pk):
    users = request.user
    rent_issues = rent_issue.objects.filter(rent__renters=users)
    page = ''
    title_page = 'Driver Details'
    driverdet = get_object_or_404(driver_shop,pk=pk)
    drivings = driver_shop.objects.filter(account=users)
    my_shops = Shops.objects.filter(owner=users)
    context = {
        'page': page,
        'title_page': title_page,
        'my_shops': my_shops,
        'driverdet':driverdet,
        'drivings':drivings,
        'users':users,
        'rent_issues':rent_issues,

    }
    return render(request, 'accounts/driverdetails.html', context)



@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def mydrivingshops(request):
    users = request.user
    rent_issues = rent_issue.objects.filter(rent__renters=users)
    page = 'mydrivingshops'
    title_page = 'Affiliated Shops'
    drivings = driver_shop.objects.filter(account=users)
    my_shops = Shops.objects.filter(owner=users)
    appointments = Rented_Cars.objects.filter(driver_shp__account=users)

    context = {
        'page':page,
        'title_page':title_page,
        'users':users,
        'rent_issues':rent_issues,
        'drivings':drivings,
        'my_shops':my_shops, 
        'drivings':drivings,
        'appointments':appointments
    }
    return render(request, 'accounts/driveshop.html',context)

@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def mydrivingshops_details(request,pk):
    users = request.user
    rent_issues = rent_issue.objects.filter(rent__renters=users)
    page = 'mydrivingshops'
    title_page = 'Affiliated Shops'
    drivings = driver_shop.objects.filter(account=users)
    my_shops = Shops.objects.filter(owner=users)
    appointment_details = get_object_or_404(Rented_Cars,pk=pk)
    context = {
        'page':page,
        'title_page':title_page,
        'users':users,
        'rent_issues':rent_issues,
        'drivings':drivings,
        'my_shops':my_shops, 
        'drivings':drivings,
        'appointment_details':appointment_details,
    }
    return render(request, 'accounts/mydrivingshops_details.html',context)


@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def approve_driver_appointment(request,pk):
    apr = get_object_or_404(Rented_Cars, pk=pk) 
    apr.drivers_approval= "approved"
    apr.save()  
    messages.success(request, "Appointment Approved")
    return redirect('mydrivingshops') 

@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def denied_driver_appointment(request,pk):
    apr = get_object_or_404(Rented_Cars, pk=pk) 
    apr.drivers_approval= "denied"
    apr.save()  
    messages.success(request, "Appointment denied")
    return redirect('mydrivingshops') 



@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def cancel_driver_appointment(request,pk):
    apr = get_object_or_404(Rented_Cars, pk=pk) 
    apr.drivers_approval= "cancelled"
    apr.save()  
    messages.success(request, "Appointment Cancelled")
    return redirect('mydrivingshops') 


@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def unpaid_rente(request,pk):
    apr = get_object_or_404(Rented_Cars, pk=pk) 
    slugs = apr.unit_rented.shop_belong.slug
    apr.status= "unpaid"
    apr.save()  
    messages.success(request, "Rent Car Approved")
    return redirect('myshop_details', slug=slugs) 


@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def denied_rente(request,pk):
    apr = get_object_or_404(Rented_Cars, pk=pk) 
    slugs = apr.unit_rented.shop_belong.slug
    apr.status= "denied"
    apr.save()  
    messages.success(request, "Rent Car Denied")
    return redirect('myshop_details', slug=slugs) 


@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def cancel_rent(request,pk):
    apr = get_object_or_404(Rented_Cars, pk=pk) 
    slugs = apr.unit_rented.shop_belong.slug
    apr.status= "cancelled"
    apr.save()  
    messages.success(request, "Cancelled Succesfully")
    return redirect('users') 



@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def rent_details(request,rentid):
    users = request.user
    rent_issues = rent_issue.objects.filter(rent__renters=users)
    page = 'homedashboard'
    title_page = 'Prime Cars'
    drivings = driver_shop.objects.filter(account=users)
    my_shops = Shops.objects.filter(owner=users)
    registred_shops = Shops.objects.filter(status="published")[:12]
    cars = get_object_or_404(Rented_Cars,rent_id=rentid)
    proofs = onsitepayment.objects.filter(rent_reference=cars)
    list_of_damages = rent_issue.objects.filter(rent=cars)

    if request.method == 'POST':
        form = onsite_pay(request.POST, request.FILES)
        if form.is_valid():
            pay = form.save(commit=False)  # Don't save to the database yet
            pay.rent_reference = cars
            pay.save()  # Now save to the database
            messages.success(request, "Save proof of payments")
            return redirect('rent_details', rentid=rentid)
        rev = ratings_review_form(request.POST, request.FILES, instance=cars )
        if rev.is_valid():
            rv = rev.save(commit=False) 
            rv.rating_bolean = 2
            rv.save()
            messages.success(request, "Rated Succefully")
            return redirect('rent_details', rentid=rentid)
        else:
            print(form.errors)  # Debug form errors
            messages.error(request, "Please Try Again")
    else:
        form = onsite_pay()
        rev = ratings_review_form(instance=cars)

    
    context = {
        'page':page,
        'title_page':title_page,
        'users':users,
        'rent_issues':rent_issues,
        'my_shops':my_shops, 
        'registred_shops':registred_shops,
        'cars':cars,
        'drivings':drivings,
        'form':form,
        'proofs':proofs,
        'rev':rev,
        'stars': range(cars.rating_star),
        'list_of_damages':list_of_damages,
    }
    return render(request, 'accounts/rent_details.html',context)





@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def payment_paid(request,pk):
    apr = get_object_or_404(Rented_Cars, pk=pk) 
    rent_id = apr.rent_id
    apr.status= "paid"
    apr.save()  
    messages.success(request, "Rent paid succesfully")
    return redirect('rent_details', rentid=rent_id ) 


@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def payment_paid_onsite(request,pk):
    apr = get_object_or_404(Rented_Cars, pk=pk) 
    rent_id = apr.rent_id
    apr.status= "paid"
    apr.save()  
    messages.success(request, "Rent paid succesfully")
    return redirect('rent_details_shop', rentid=rent_id ) 



@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def out_garage(request,pk):
    manila_timezone = pytz.timezone("Asia/Manila")
    current_time = datetime.now(manila_timezone).strftime('%Y-%m-%d %H:%M:%S')
    apr = get_object_or_404(Rented_Cars, pk=pk) 
    slug = apr.unit_rented.shop_belong.slug
    apr.out_garage = current_time
    apr.unit_release = 2
    apr.save()  
    messages.success(request, "Car is out of Garage")
    return redirect('myshop_details',slug=slug) 


@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def return_garage(request,pk):
    apt = get_object_or_404(Rented_Cars, pk=pk) 
    apt.unit_release = 3 
    apt.save()  
    messages.success(request, "Returning to Garage")
    return redirect('users') 





@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def recieved_garage(request, pk):
    manila_timezone = pytz.timezone("Asia/Manila")
    current_time = datetime.now(manila_timezone)
    apr = get_object_or_404(Rented_Cars, pk=pk)
    if apr.return_unit.tzinfo is None:
        apr.return_unit = apr.return_unit.replace(tzinfo=manila_timezone)
    time_difference = current_time - apr.return_unit  
    totalhours = abs(time_difference.days * 24 + time_difference.seconds // 3600)

    if totalhours == 0:
        exist = 0  
        apr.paid_excess = "none"
    else:
        if time_difference.total_seconds() >= 0:
            exist = 1  
            apr.paid_excess = "unpaid"
        else:
            exist = 2  # Refund
            apr.paid_excess = "refund"
    
    
    additional = totalhours * apr.unit_rented.rent_per_hr
    apr.excess_exist = exist
    apr.execes_hrs = totalhours
    apr.execes_amount = additional
    apr.return_garage = current_time
    apr.unit_release = 1
    apr.rating_bolean = 1
    apr.transaction_done = 1 #balik
    apr.save()
    messages.success(request, "Returning Successfully")
    return redirect('rent_details_shop', rentid=apr.rent_id)


@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def refund_cost(request,pk):
    apr = get_object_or_404(Rented_Cars, pk=pk) 
    rentid = apr.rent_id
    apr.excess_exist = 0
    apr.car_fee_total = apr.car_fee_total - apr.execes_amount
    apr.total_fare = apr.total_fare - apr.execes_amount
    apr.paid_excess = 'refunded' 
    apr.save()  
    messages.success(request, "Refund Payment Successfully")
    return redirect('rent_details_shop', rentid=rentid) 

@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def excess_cost(request,pk):
    apr = get_object_or_404(Rented_Cars, pk=pk) 
    rentid = apr.rent_id
    apr.excess_exist = 0
    apr.car_fee_total = apr.car_fee_total + apr.execes_amount
    apr.total_fare = apr.total_fare + apr.execes_amount
    apr.paid_excess = 'paid' 
    apr.save()  
    messages.success(request, "Excess amount Successfully paid")
    return redirect('rent_details_shop', rentid=rentid) 


@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def online_pay_excess(request,pk):
    apr = get_object_or_404(Rented_Cars, pk=pk) 
    rentid = apr.rent_id
    apr.excess_exist = 0
    apr.car_fee_total = apr.car_fee_total + apr.execes_amount
    apr.total_fare = apr.total_fare + apr.execes_amount
    apr.paid_excess = 'paid' 
    apr.save()  
    messages.success(request, "Excess amount Successfully paid")
    return redirect('rent_details', rentid=rentid) 



@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def driver_payout_requests(request,pk):
    apr = get_object_or_404(Rented_Cars, pk=pk) 
    apr.drivers_approval= "payout"
    apr.save()  
    messages.success(request, "Payout Request")
    return redirect('mydrivingshops') 


@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def driver_released_requests(request,pk):
    apr = get_object_or_404(Rented_Cars, pk=pk) 
    apr.drivers_approval= "released"
    slug = apr.unit_rented.shop_belong.slug
    apr.save()
    messages.success(request, "Payout Released")
    return redirect('myshop_details', slug=slug) 


@login_required(login_url='signin')
@role_required(allowed_roles=['2'], redirect_url='admin')
def review_status(request,pk):
    apr = get_object_or_404(Rented_Cars, pk=pk) 
    if apr.rating_bolean == 1:
        apr.rating_bolean = 2
    else:
        apr.rating_bolean = 1
    slug = apr.unit_rented.shop_belong.slug
    apr.save()
    messages.success(request, "Review Status Updated")
    return redirect('myshop_details', slug=slug) 

def logoutUser(request):
    user = request.user
    user.log_status = "offline"
    user.save()
    logout(request)
    return redirect('home')




