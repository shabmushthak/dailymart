from django.urls import path
from.import views
urlpatterns = [
    path('categorydata',views.categorydata,name='categorydata'),
    path('table_category',views.table_category,name='table_category'),
    path('add_category',views.add_category,name='add_category'),
    path('update/<int:id>',views.update,name='update'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('dlt/<int:id>',views.dlt,name='dlt'),

    path('add_product',views.add_product,name='add_product'),
    path('table_product',views.table_product,name='table_product'),
    path('productdata',views.productdata,name='productdata'),
    path('dltpro/<int:id>',views.dltpro,name='dltpro'),
    path('editpro/<int:id>',views.editpro,name='editpro'),
    path('updateproduct/<int:id>',views.updateproduct,name='updateproduct'),  

    path('admin_home',views.admin_home,name='admin_home'),  

    path('order_table',views.order_table,name='order_table'),  
    path('dltorder/<int:id>',views.dltorder,name='dltorder'),  
]