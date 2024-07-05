from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class login_user(models.Model):    
    class Meta: 
        verbose_name="ورود کاربر "  
        verbose_name_plural="ورود کاربر" 
                                                  
    ID_user = models.ForeignKey(User,on_delete=models.CASCADE)
    First_name = models.CharField(max_length=100,null=False,blank=False,verbose_name="نام ")
    Last_name = models.CharField(max_length=100,null=False,blank=False,verbose_name="نام خانوادگی ")
    Phone_number=models.CharField(max_length=11,null=False,blank=False,verbose_name="تلفن ")
    Email= models.EmailField(max_length=254,null=False,blank=False,verbose_name="ایمیل ")
    Passwoord=models.CharField(max_length=50,verbose_name="پسورد ")
    Register_date= models.DateTimeField("date published")

    def __str__(self):
        return '%s - %s - %s - %s - %s - %s '%(self.First_name ,self.Last_name,self.Phone_number,self.Email,self.Passwoord,self.Register_date )
    
 ###################################### login_Admin ##############################################

class login_Admin(models.Model): 
    class Meta: 
        verbose_name="ورود ادمین "  
        verbose_name_plural="ورود ادمین" 

    ID_Admin = models.ForeignKey(User,on_delete=models.CASCADE)
    First_name_Admin = models.CharField(max_length=100,null=False,blank=False,verbose_name="نام ")
    Last_name_Admin = models.CharField(max_length=100,null=False,blank=False,verbose_name=" نام خانوادگی ")
    Phone_number_Admin=models.CharField(max_length=11,null=False,blank=False,verbose_name="تلفن ")
    Email_user_Admin= models.EmailField(max_length=100,null=False,blank=False,verbose_name="ایمیل ")
    Passwoord_user_Admin=models.CharField(max_length=50,verbose_name="پسورد ")
    Register_date_Admin= models.DateTimeField("date published",)
  
 
 
    def __str__(self):
        return '%s - %s - %s - %s - %s - %s'%(self.First_name_Admin,self.Last_name_Admin,self.Phone_number_Admin,self.Email_user_Admin,self.Passwoord_user_Admin,self.Register_date_Admin,)


######################################### PRICE ALIBABA ##########################################
   
class Price_Alibaba(models.Model):
    class Meta: 
        verbose_name="ورود ادمین "  
        verbose_name_plural="ورود ادمین" 
    Price=models.DecimalField(max_digits=10,decimal_places=1,null=False,blank=False,verbose_name="قیمت " )                                  # ghymat mahsool
    Price_discount=models.DecimalField(max_digits=10,decimal_places=1,null=True,blank=True,verbose_name="قیمت تخفیف ")                         # ghymat takhfif mahsool

    def __str__(self) -> str:
        return '%s - %s'% (self.Price,self.Price_discount)
    
######################################## CATEGORY ##########################################

class Category(models.Model): 
    class Meta: 
        verbose_name="دسته ها "  
        verbose_name_plural="دسته ها"                                            
    Name=models.CharField(max_length=100,verbose_name=" نام دسته")
    
    def __str__(self) -> str:
        return '%s'%(self.Name)
    
######################################### ATREBIUTE ##########################################
class Attribute(models.Model):
    class Meta: 
        verbose_name="جزئیات"  
        verbose_name_plural="جزئیات "
    Name=models.CharField(max_length=100,null=False,blank=False,verbose_name="نام  ")            

    def __str__(self) -> str:
        return "{}".format(self.Name)
    


####################################### MODEL CATEGORY/ATTRIBUTE ######################################
class CategoryAttribute(models.Model):  
    class Meta: 
        verbose_name="جزئیات/دسته"  
        verbose_name_plural="جزئیات/دسته "                                                 
    CategoryId=models.ForeignKey("Category",on_delete=models.CASCADE,related_name='Attribute',null=True,blank=True,verbose_name="نام دسته  ")
    AttributeId=models.ForeignKey("Attribute",on_delete=models.CASCADE,verbose_name="نام جزئیات")

    def __str__(self):
        return f'{self.CategoryId.Name}-{self.AttributeId.Name}'
    
####################################### TRIP (safarha) ###################################################

class Trip(models.Model):
    class Meta: 
        verbose_name="سفر"  
        verbose_name_plural="سفر" 
    TripId=models.ForeignKey("Category",on_delete=models.CASCADE,verbose_name="دسته")
    TripAttribute=models.ForeignKey("TripAttribute",on_delete=models.CASCADE,verbose_name=" جزئیات سفر")
    Attribute=models.ForeignKey(Attribute,on_delete=models.CASCADE,verbose_name="جزئیات")
    Name=models.CharField(max_length=100,verbose_name=" نام") 
    Poster=models.ImageField(upload_to="TripImages/",null=True,verbose_name="پوستر")    # zamani k taraf bekhad ye ax estefadeh koneh upload_to= zamani ke nemikhahim hajm ax hai ke darim fazay ma ra ziad eshghal nakoneh ma yek file ya poosheh ijad mikonim va sar in masir faghat moshakhas mikonim ke az anja bekhanad.

 

    def __str__(self):
        return f'{self.TripId}-{self.Name}'

#######################################  PRODUC/ATTRIBUTE (marboot be safar) ########################################
 
class TripAttribute(models.Model):
    class Meta: 
        verbose_name="جزئیات سفر"  
        verbose_name_plural="جزئیات سفر"                                                                         # vizhegi mahsoolato negahdari mikoneh
    TripId=models.ForeignKey("Trip",on_delete=models.CASCADE,verbose_name="سفر")
    AttributeId=models.ForeignKey("Attribute",on_delete=models.CASCADE,verbose_name="جزئیات")
    Value=models.CharField(max_length=255,verbose_name="مقدار")

    def __str__(self) -> str:
        return f'{self.TripId.Name}-{self.AttributeId.Name}'
    
##################################### PASSENGER ############################################################
                                                                                                             # atelaat marboot be mosaferan
class Passenger(models.Model):
    class Meta: 
        verbose_name="مسافر"  
        verbose_name_plural="مسافر" 
    FirstName=models.CharField(max_length=100,verbose_name="نام")
    LastName=models.CharField(max_length=100,verbose_name="نام خانوادگی")
    Email=models.EmailField(verbose_name="ایمیل")
    phone=models.CharField(max_length=11,null=False,blank=False,verbose_name="تلفن")

    def __str__(self) -> str:
        return '%s %s %s %s'%(self.FirstName,self.LastName,self.Email,self.phone)
    
##################################### TIKET ############################################################
                                                                                                             #tedad blit hay har shakhs va etelaat marboot be blit negah midarim.
class Tiket(models.Model):
    class Meta: 
        verbose_name="بلیط"  
        verbose_name_plural="بلیط" 
    Passenger=models.ForeignKey("Passenger",on_delete=models.CASCADE,verbose_name="نام مسافر")
    TripId=models.ForeignKey("Trip",on_delete=models.CASCADE,verbose_name="سفر")
    SeatNumber=models.CharField(max_length=10,null=True,blank=True,verbose_name="شماره صندلی")
    quantity=models.PositiveIntegerField(verbose_name="تعداد")                                                                    #tedad blit



    def __str__(self) -> str:
        return f'{self.Passenger}-{self.TripId.Name}-{self.quantity}'


############################################# FACTOR #######################################################
                                                                                                                     # factor marboot be mosaferan va ghymat kol negah midarim
class Factor(models.Model):
    class Meta: 
        verbose_name="فاکتور"  
        verbose_name_plural="فاکتور" 
    Passenger=models.ForeignKey("Passenger",on_delete=models.CASCADE,verbose_name="نام مسافر")
    TripAttribute=models.ForeignKey("TripAttribute",on_delete=models.CASCADE,verbose_name="جزئیات سفر")
    TotalPraice=models.DecimalField(max_digits=10,decimal_places=2,verbose_name="قیمت")
    Created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.Passenger}-{self.TotalPraice}-{self.Created_at}'
    



