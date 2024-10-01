from django.urls import path
from webapp import views
urlpatterns = [
    path('home/',views.home_page,name='home'),
path('about_us/',views.about_us,name='about_us'),
path('contact_us/',views.contact,name='contact_us'),
path('save_contact/',views.save_contact,name='save_contact'),
path('all_product/',views.all_product,name='all_product'),
path('single_product/<int:pro_id>',views.single_product,name='single_product'),
path('filtered_product/<cat_id>',views.filtered_product,name='filtered_product'),
path('',views.login_user,name='login_user'),
path('sign_user/',views.sign_user,name='sign_user'),
path('user_logout/',views.user_logout,name='user_logout'),
path('save_user/',views.save_user,name='save_user'),
path('user_login/',views.user_login,name='user_login'),
path('cart_page/',views.cart_page,name='cart_page'),
path('save_cart/',views.save_cart,name='save_cart'),
path('cartdelete/<int:delid>',views.delete_cart,name='cartdelete'),
path('check_out/',views.check_out,name='check_out'),
path('save_order/',views.save_order,name='save_order'),
path('payment_page/',views.payment_page,name='payment_page')

]

