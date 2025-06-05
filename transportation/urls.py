#imports that are needed for modules, url patterns, and manage user authentication—routing
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path, include
#for Routing #trexcontroladmin 

#landing page/home page
urlpatterns = [
    path('',views.home,name = 'home'), #home page
    path('vehicle/',views.vehicle,name = 'vehicle'), #list of vehicles
    path('vehicle/<int:pk>/details/',views.car_details,name = 'car_details'), #vehicle details—if you selected one of the published vehicles
    path('drivers/',views.drivers,name = 'drivers'),
    path('drivers/details/',views.driver_details,name = 'driver_details'),
    path("shop/", views.shop, name="shop"), #shop view
    path("shop/details/<slug:slug>/", views.shop_details, name="shop_details"), #shop details
    path("contacts/", views.contacts, name="contacts"),
    path('createaccount/',views.createaacount, name='createaacount'), #create account page
    path('login/',views.signin, name='signin'), #login page
    path('verify/',views.verify_email, name='verify_email'), #email verification
    path('logout/',views.logoutUser, name='logoutUser'), #logout
    path("profile/",views.profile, name="profile"), #user profile page
    #======================================================

    #admin side routing, or view/landing page
    path('administrator/', views.admin, name='admin'), #admin dashboard/landing page
    path('blank/', views.blank, name='blank'),
    path('list/admins/', views.list_administrators, name='list_administrators'), #list of admins
    path('list/users/', views.list_users, name='list_users'), #list of users
    path('list/users/details/<int:pk>', views.user_details, name='user_details'), #details of a certain user
    path('shops/', views.shops, name='shops'), #list of shops—published and not
    path('shops/details/<int:pk>/', views.shops_details, name='shops_details'), #details of a certain shop—view/display
    path('shops/<int:pk>/', views.unlock_shops, name='unlock_shops'),
    path('published/cars/<int:pk>/', views.published_cars, name='published_cars'), #lsit of published vehicles
    path('vehicles/', views.vehicles_list, name='vehicles_list'), #lsit of all vehicles—published and not
    path('payments/', views.payments, name='payments'), #list of payments transactions
    path('payments/details/<str:refnumber>', views.payments_details, name='payments_details'), #details of a certain payment transaction
    path('payments/details/approved/<int:pk>', views.payments_request_approved, name='payments_request_approved'), #approved payment
    #======================================================

    #shop owners
    path('primecars/', views.users, name='users'),
    path('my/registered/shops/', views.myshops, name='myshops'), #registered and published shops of user shop owner
    path('my/registered/shops/<slug:slug>/edit/', views.edit_myshops, name='edit_myshops'), #edit shop information—can be done by shop owner
    path('my/registered/shops/<slug:slug>/delete/', views.delete_myshops, name='delete_myshops'), #delete shop—if shop owner wants to
    path('my/shop/', views.mylistshop, name='mylistshop'), #list of shops of user shop owner—published and not
    path('registered/shops/', views.registered_shops, name='registered_shops'), #lsit of registered shop
    path('registered/shops/<slug:slug>/', views.details_shops, name='details_shops'), #shop details
    #======================================================

    #specific shop views
    path('myshop/details/<slug:slug>/', views.myshop_details, name='myshop_details'), #shop details
    path('myshop/payment/details/<slug:slug>/', views.myshop_payment_details, name='myshop_payment_details'), #payment details
    path('myshop/payment/request/<slug:slug>/', views.Request_payment, name='Request_payment'), #request payment
    path('myshop/payment/submission/<slug:slug>/', views.Submit_payment, name='Submit_payment'), #submit payment
    path('myshop/payment/transaction/details/<str:tref>/', views.payment_transaction_details, name='payment_transaction_details'), #payment transaction details
    #======================================================

    #driver payout
    path('myshop/drivers/payout/<slug:slug>/', views.drivers_payout, name='drivers_payout'), #driver payouts
    path('myshop/drivers/released/<int:pk>/', views.driver_released_requests, name='driver_released_requests'), #released payouts
    #======================================================

    #rental processing and issues
    path('myshop/rent/<str:rentid>/', views.rent_details_shop, name='rent_details_shop'), #rent details
    path('myshop/rent/<int:pk>/issues/', views.report_issues, name='report_issues'), #report issue
    path('myshop/rent/<int:pk>/issues/deleted/', views.report_issues_deleted, name='report_issues_deleted'), #delete report issue
    path('myshop/rent/<int:pk>/issues/all/deleted/', views.all_report_issues_deleted, name='all_report_issues_deleted'),  #delete all report issue
    path('myshop/rent/admin/<str:rentid>/', views.rent_details_shop_admin, name='rent_details_shop_admin'), #rent details
    path('myshop/vehicles/<slug:slug>/', views.vehicles, name='vehicles'), #list of vehicles by shop
    path('myshop/<slug:slug>/vehicles/edit/<int:pk>/', views.edit_vehicles, name='edit_vehicles'), #edit/update vehicle informations
    path('myshop/<slug:slug>/vehicles/delete/<int:pk>/', views.delete_vehicles, name='delete_vehicles'), #delete vehicle—no longer available for rental
    path('myshop/drivers/<slug:slug>/', views.shopdrivers, name='shopdrivers'), #list of drivers
    path('myshop/drivers/<slug:slug>/list/', views.mydrivers, name='mydrivers'),
    path('myshop/drivers/<slug:slug>/approved/<int:pk>/', views.approved_driver, name='approved_driver'), #approved driver
    path('myshop/drivers/<slug:slug>/delete/<int:pk>/', views.delete_driver, name='delete_driver'), #delete driver—no longer employed
    #======================================================
    
    #shop unit views
    path('shop/<slug:slug>/unit/<int:pk>/', views.shop_unit, name='shop_unit'), #specific unit details
    path('registered/vehicles/', views.registered_vehicles, name='registered_vehicles'), #registered vehicles list
    path('rent/details/<str:rentid>/', views.rent_details, name='rent_details'), #rent detail
    path('rent/payment/<int:pk>/paid/', views.payment_paid, name='payment_paid'), #payment status as paid
    path('rent/payment/<int:pk>/paid/onsite/', views.payment_paid_onsite, name='payment_paid_onsite'), #onsite payment
    path('rent/vehicles/<int:pk>/', views.rent_vehicles, name='rent_vehicles'), #rent a vehicle
    path('rent/vehicles/<int:renteid>/unit/<int:unit>/edit/', views.rent_vehicles_edit, name='rent_vehicles_edit'), #edit rented vehicle
    #======================================================
    
    #driver account & appointments
    path('driver/details/<int:pk>/', views.driverdetails, name='driverdetails'), #driver detail
    path('shop/mydrive/', views.mydrivingshops, name='mydrivingshops'),
    path('shop/mydrive/<int:pk>/lock/', views.account_lock_driver, name='account_lock_driver'), #lock driver account
    path('shop/mydrive/<int:pk>/removal/', views.account_removal_driver, name='account_removal_driver'), #remove driver
    path('shop/mydrive/appointment/<int:pk>/', views.mydrivingshops_details, name='mydrivingshops_details'), #appointment details
    path('shop/mydrive/appointment/<int:pk>/approved/', views.approve_driver_appointment, name='approve_driver_appointment'), #approve appointment
    path('shop/mydrive/appointment/<int:pk>/denied/', views.denied_driver_appointment, name='denied_driver_appointment'), #deny appointment
    path('shop/mydrive/appointment/<int:pk>/cancelled/', views.cancel_driver_appointment, name='cancel_driver_appointment'), #cancel appointment
    #======================================================
    
    #car rental status updates
    path('car/rent/approved/<int:pk>/', views.unpaid_rente, name='unpaid_rente'), #approve rent request
    path('car/rent/denied/<int:pk>/', views.denied_rente, name='denied_rente'), #deny rent
    path('car/rent/cancelled/<int:pk>/', views.cancel_rent, name='cancel_rent'), #cancel rent
    path('car/rent/release/<int:pk>/', views.out_garage, name='out_garage'), #mark as released
    path('car/rent/returning/<int:pk>/', views.return_garage, name='return_garage'), #mark as returning
    path('car/rent/recieved/<int:pk>/', views.recieved_garage, name='recieved_garage'), #mark as received
    path('car/rent/refund/<int:pk>/', views.refund_cost, name='refund_cost'), #issue refund
    path('car/rent/excess/<int:pk>/', views.excess_cost, name='excess_cost'), #charge excess
    path('car/rent/excess/online/<int:pk>/', views.online_pay_excess, name='online_pay_excess'), #pay excess online
    path('driver/payout/request/<int:pk>/', views.driver_payout_requests, name='driver_payout_requests'), #payout request
    path('review/status/<int:pk>/', views.review_status, name='review_status'), #review status page
    #======================================================
    
    #path('features/', views.feature_view, name='features'),
    #path('developers/', views.Developers, name='developers'),
    #path('contact/', views.ContactUS, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
