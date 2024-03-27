from django.urls import path
from.import views
urlpatterns = [
    path('cat_card',views.cat_card,name='cat_card'),
    path('pro_card/<str:category>',views.pro_card,name='pro_card'),

    path('cont',views.cont,name='cont'),
    path('contactdata',views.contactdata,name='contactdata'),
    path('contact_table',views.contact_table,name='contact_table'),
    path('dltcontact/<int:id>',views.dltcontact,name='dltcontact'),

     path('reg',views.reg,name='reg'),
    path('dlt1/<int:id>',views.dlt1,name='dlt1'),
    path('register_table',views.register_table,name='register_table'),
    path('registerdata',views.registerdata,name='registerdata'),

    path('logingdata',views.logingdata,name='logingdata'),
    path('loging',views.loging,name='loging'),
    path('userlogout',views.userlogout,name='userlogout'),

    path('home/',views.home,name='home'),

    path('view_more_pro/<int:id>',views.view_more_pro,name='view_more_pro'),

    path('checkout1',views.checkout1,name='checkout1'),
    path('cart1',views.cart1,name='cart1'),

    path('about',views.about,name='about'),
    
    path('cartdata/<int:id>',views.cartdata,name='cartdata'),

    path('delete2/<int:id>',views.delete2,name='delete2'),

    path('checkoutdata',views.checkoutdata,name='checkoutdata'),

    path('suc',views.suc,name='suc'),
]