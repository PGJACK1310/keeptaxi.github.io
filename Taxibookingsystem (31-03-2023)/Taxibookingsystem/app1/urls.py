
from django.urls import path
from .views import Index,SignIn,SignUp,search,taxibookingdetails,getbookeddetails,logout,DriverSignUp,DriverDetails,DriverSignIn,driverapproval,driverlogout,myorder,driverbookingapproval,history
urlpatterns = [
    path('',Index,name='index'),
    path('signin/',SignIn,name='signin'),
    path('signup/',SignUp,name='signup'),
    path('driversignup/',DriverSignUp,name='driversignup'),
    path('driversignin/',DriverSignIn,name='driversignin'),
    path('search/',search,name='search'),
    path('taxibookingdetails/<int:id>/',taxibookingdetails,name='taxibookingdetails'),
    path('getbookingdetails/',getbookeddetails,name='getbookingdetails'),
    path('logout/',logout,name='logout'),
    path('driverlogout/',driverlogout,name='driverlogout'),
    path('driverapproval/',driverapproval,name='driverapproval'),
    path('myorder/',myorder,name='myorder'),
    path('driverbookingapproval/<int:id>/',driverbookingapproval,name='driverbookingapproval'),
    path('history/',history,name='history'),
    path('driver/',DriverDetails,name='driver'),
   
]
