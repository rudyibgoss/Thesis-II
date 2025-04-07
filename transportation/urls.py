
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path, include
#for Routing #trexcontroladmin 

urlpatterns = [
    path('',views.home,name = 'home'),
    path('vehicle/',views.vehicle,name = 'vehicle'),
    path('vehicle/<int:pk>/details/',views.car_details,name = 'car_details'),
    path('drivers/',views.drivers,name = 'drivers'),
    path('drivers/details/',views.driver_details,name = 'driver_details'),
    path("shop/", views.shop, name="shop"),
    path("shop/details/<slug:slug>/", views.shop_details, name="shop_details"),
    path("contacts/", views.contacts, name="contacts"),
    path('createaccount/',views.createaacount, name='createaacount'),
    path('login/',views.signin, name='signin'),
    path('verify/',views.verify_email, name='verify_email'),
    path('logout/',views.logoutUser, name='logoutUser'),
    path("profile/",views.profile, name="profile"),
    #======================================================


    path('administrator/', views.admin, name='admin'),
    path('blank/', views.blank, name='blank'),
    path('list/admins/', views.list_administrators, name='list_administrators'),
    path('list/users/', views.list_users, name='list_users'),
    path('list/users/details/<int:pk>', views.user_details, name='user_details'),
    path('shops/', views.shops, name='shops'),
    path('shops/details/<int:pk>/', views.shops_details, name='shops_details'),
    path('shops/<int:pk>/', views.unlock_shops, name='unlock_shops'),
    path('published/cars/<int:pk>/', views.published_cars, name='published_cars'),
    path('vehicles/', views.vehicles_list, name='vehicles_list'),
    path('payments/', views.payments, name='payments'),
    path('payments/details/<str:refnumber>', views.payments_details, name='payments_details'),
    path('payments/details/approved/<int:pk>', views.payments_request_approved, name='payments_request_approved'),

    #======================================================
    path('primecars/', views.users, name='users'),
    path('my/registered/shops/', views.myshops, name='myshops'),
    path('my/registered/shops/<slug:slug>/edit/', views.edit_myshops, name='edit_myshops'),
    path('my/registered/shops/<slug:slug>/delete/', views.delete_myshops, name='delete_myshops'),
    path('my/shop/', views.mylistshop, name='mylistshop'),
    path('registered/shops/', views.registered_shops, name='registered_shops'),
    path('registered/shops/<slug:slug>/', views.details_shops, name='details_shops'), 



    path('myshop/details/<slug:slug>/', views.myshop_details, name='myshop_details'),
    path('myshop/payment/details/<slug:slug>/', views.myshop_payment_details, name='myshop_payment_details'),
    path('myshop/payment/request/<slug:slug>/', views.Request_payment, name='Request_payment'),
    path('myshop/payment/submission/<slug:slug>/', views.Submit_payment, name='Submit_payment'),
    path('myshop/payment/transaction/details/<str:tref>/', views.payment_transaction_details, name='payment_transaction_details'),

    path('myshop/drivers/payout/<slug:slug>/', views.drivers_payout, name='drivers_payout'),
    path('myshop/drivers/released/<int:pk>/', views.driver_released_requests, name='driver_released_requests'),



    path('myshop/rent/<str:rentid>/', views.rent_details_shop, name='rent_details_shop'),
    path('myshop/rent/<int:pk>/issues/', views.report_issues, name='report_issues'),
    path('myshop/rent/<int:pk>/issues/deleted/', views.report_issues_deleted, name='report_issues_deleted'),
    path('myshop/rent/<int:pk>/issues/all/deleted/', views.all_report_issues_deleted, name='all_report_issues_deleted'),
    path('myshop/rent/admin/<str:rentid>/', views.rent_details_shop_admin, name='rent_details_shop_admin'),
    path('myshop/vehicles/<slug:slug>/', views.vehicles, name='vehicles'),
    path('myshop/<slug:slug>/vehicles/edit/<int:pk>/', views.edit_vehicles, name='edit_vehicles'),
    path('myshop/<slug:slug>/vehicles/delete/<int:pk>/', views.delete_vehicles, name='delete_vehicles'),
    path('myshop/drivers/<slug:slug>/', views.shopdrivers, name='shopdrivers'),
    path('myshop/drivers/<slug:slug>/list/', views.mydrivers, name='mydrivers'),
    path('myshop/drivers/<slug:slug>/approved/<int:pk>/', views.approved_driver, name='approved_driver'),
    path('myshop/drivers/<slug:slug>/delete/<int:pk>/', views.delete_driver, name='delete_driver'),
    
    


    path('shop/<slug:slug>/unit/<int:pk>/', views.shop_unit, name='shop_unit'), 
    path('registered/vehicles/', views.registered_vehicles, name='registered_vehicles'),
    path('rent/details/<str:rentid>/', views.rent_details, name='rent_details'),
    path('rent/payment/<int:pk>/paid/', views.payment_paid, name='payment_paid'),
    path('rent/payment/<int:pk>/paid/onsite/', views.payment_paid_onsite, name='payment_paid_onsite'),
    path('rent/vehicles/<int:pk>/', views.rent_vehicles, name='rent_vehicles'),
    path('rent/vehicles/<int:renteid>/unit/<int:unit>/edit/', views.rent_vehicles_edit, name='rent_vehicles_edit'),


    path('driver/details/<int:pk>/', views.driverdetails, name='driverdetails'),
    path('shop/mydrive/', views.mydrivingshops, name='mydrivingshops'),
    path('shop/mydrive/<int:pk>/lock/', views.account_lock_driver, name='account_lock_driver'),
    path('shop/mydrive/<int:pk>/removal/', views.account_removal_driver, name='account_removal_driver'),
    path('shop/mydrive/appointment/<int:pk>/', views.mydrivingshops_details, name='mydrivingshops_details'),
    path('shop/mydrive/appointment/<int:pk>/approved/', views.approve_driver_appointment, name='approve_driver_appointment'),
    path('shop/mydrive/appointment/<int:pk>/denied/', views.denied_driver_appointment, name='denied_driver_appointment'),
    path('shop/mydrive/appointment/<int:pk>/cancelled/', views.cancel_driver_appointment, name='cancel_driver_appointment'),
    path('car/rent/approved/<int:pk>/', views.unpaid_rente, name='unpaid_rente'),
    path('car/rent/denied/<int:pk>/', views.denied_rente, name='denied_rente'),
    path('car/rent/cancelled/<int:pk>/', views.cancel_rent, name='cancel_rent'),
    path('car/rent/release/<int:pk>/', views.out_garage, name='out_garage'),
    path('car/rent/returning/<int:pk>/', views.return_garage, name='return_garage'),
    path('car/rent/recieved/<int:pk>/', views.recieved_garage, name='recieved_garage'),
    path('car/rent/refund/<int:pk>/', views.refund_cost, name='refund_cost'),
    path('car/rent/excess/<int:pk>/', views.excess_cost, name='excess_cost'),
    path('car/rent/excess/online/<int:pk>/', views.online_pay_excess, name='online_pay_excess'),
    path('driver/payout/request/<int:pk>/', views.driver_payout_requests, name='driver_payout_requests'),
    path('review/status/<int:pk>/', views.review_status, name='review_status'),
    
    
    #path('features/', views.feature_view, name='features'),
    #path('developers/', views.Developers, name='developers'),
    #path('contact/', views.ContactUS, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
