from django.urls import path
from textileapp import views
urlpatterns=[
    path('index/',views.index_page,name='index'),
path('add/',views.add_categories,name='add'),
path('save/',views.save_category,name='save'),
path('display/',views.display_category,name='display'),
path('edit/<int:cat_id>',views.edit_categ,name='edit'),
path('update/<int:data_id>',views.update_reg,name='update'),
path('add_product/',views.add_product,name='add_product'),
path('view_product/',views.view_product,name='view_product'),
path('save_product/',views.save_products,name='save_product'),
path('edit_product/<int:product_id>',views.edit_products,name='edit_product'),
path('delete_product/<int:product_id>',views.delete_product,name='delete_product'),
path('update_product/<int:data_id>',views.update_product,name='update_product'),
path('adminpage/',views.admin_page,name='adminpage'),
path('admin_login/',views.admin_login,name='admin_login'),
path('admin_logout/',views.admin_logout,name='admin_logout'),
path('view_contact/',views.view_contact,name='view_contact'),
path('delete_contact/<int:contact_id>',views.delete_contact,name='delete_contact')

]