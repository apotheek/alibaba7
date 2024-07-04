from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class login_user(models.Model):                                                  
    ID_user = models.ForeignKey(User,on_delete=models.CASCADE)
    First_name = models.CharField(max_length=100,null=False,blank=False)
    Last_name = models.CharField(max_length=100,null=False,blank=False)
    Phone_number=models.CharField(max_length=11,null=False,blank=False)
    Email= models.EmailField(max_length=254,null=False,blank=False)
    Passwoord=models.CharField(max_length=50)
    Register_date= models.DateTimeField("date published")

    def __str__(self):
        return '%s - %s - %s - %s - %s - %s '%(self.First_name ,self.Last_name,self.Phone_number,self.Email,self.Passwoord,self.Register_date )
    
 ###################################### login_Admin ##############################################

class login_Admin(models.Model): 
    ID_Admin = models.ForeignKey(User,on_delete=models.CASCADE)
    First_name_Admin = models.CharField(max_length=100,null=False,blank=False)
    Last_name_Admin = models.CharField(max_length=100,null=False,blank=False)
    Phone_number_Admin=models.CharField(max_length=11,null=False,blank=False)
    Email_user_Admin= models.EmailField(max_length=100,null=False,blank=False)
    Passwoord_user_Admin=models.CharField(max_length=50)
    Register_date_Admin= models.DateTimeField("date published")
  
 
 
    def __str__(self):
        return '%s - %s - %s - %s - %s - %s'%(self.First_name_Admin,self.Last_name_Admin,self.Phone_number_Admin,self.Email_user_Admin,self.Passwoord_user_Admin,self.Register_date_Admin,)


######################################### PRICE ALIBABA ##########################################
   
class Price_Alibaba(models.Model):
    Price=models.DecimalField(max_digits=10,decimal_places=1,null=False,blank=False)                                  # ghymat mahsool
    Price_discount=models.DecimalField(max_digits=10,decimal_places=1,null=True,blank=True)                         # ghymat takhfif mahsool

    def __str__(self) -> str:
        return '%s - %s'% (self.Price,self.Price_discount)
    
######################################## CATEGORY ##########################################

class Category(models.Model):                                            
    Name=models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return '%s'%(self.Name)
    
######################################### ATREBIUTE ##########################################
class Attribute(models.Model):
    Name=models.CharField(max_length=100,null=False,blank=False)            

    def __str__(self) -> str:
        return "{}".format(self.Name)
    


####################################### MODEL CATEGORY/ATTRIBUTE ######################################
class CategoryAttribute(models.Model):                                                                         #kodam dasteh che vizhegihai darad
    CategoryId=models.ForeignKey("Category",on_delete=models.CASCADE,related_name='Attribute',null=True,blank=True)
    AttributeId=models.ForeignKey("Attribute",on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.CategoryId.Name}-{self.AttributeId.Name}'
    
####################################### TRIP (safarha) ###################################################

class Trip(models.Model):
    TripId=models.ForeignKey("Category",on_delete=models.CASCADE)
    TripAttribute=models.ForeignKey("TripAttribute",on_delete=models.CASCADE)
    Attribute=models.ForeignKey(Attribute,on_delete=models.CASCADE)
    Name=models.CharField(max_length=100) 
    Poster=models.ImageField(upload_to="TripImages/",null=True)    # zamani k taraf bekhad ye ax estefadeh koneh upload_to= zamani ke nemikhahim hajm ax hai ke darim fazay ma ra ziad eshghal nakoneh ma yek file ya poosheh ijad mikonim va sar in masir faghat moshakhas mikonim ke az anja bekhanad.

 

    def __str__(self):
        return f'{self.TripId}-{self.Name}'

#######################################  PRODUC/ATTRIBUTE (marboot be safar) ########################################
 
class TripAttribute(models.Model):                                                                        # vizhegi mahsoolato negahdari mikoneh
    TripId=models.ForeignKey("Trip",on_delete=models.CASCADE)
    AttributeId=models.ForeignKey("Attribute",on_delete=models.CASCADE)
    Value=models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.TripId.Name}-{self.AttributeId.Name}'
    
##################################### PASSENGER ############################################################
                                                                                                             # atelaat marboot be mosaferan
class Passenger(models.Model):
    FirstName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    Email=models.EmailField()
    phone=models.CharField(max_length=11,null=False,blank=False)

    def __str__(self) -> str:
        return '%s %s %s %s'%(self.FirstName,self.LastName,self.Email,self.phone)
    
##################################### TIKET ############################################################
                                                                                                             #tedad blit hay har shakhs va etelaat marboot be blit negah midarim.
class Tiket(models.Model):
    Passenger=models.ForeignKey("Passenger",on_delete=models.CASCADE)
    TripId=models.ForeignKey("Trip",on_delete=models.CASCADE)
    SeatNumber=models.CharField(max_length=10,null=True,blank=True)
    quantity=models.PositiveIntegerField()                                                                    #tedad blit



    def __str__(self) -> str:
        return f'{self.Passenger}-{self.TripId.Name}-{self.quantity}'


############################################# FACTOR #######################################################
                                                                                                                     # factor marboot be mosaferan va ghymat kol negah midarim
class Factor(models.Model):
    Passenger=models.ForeignKey("Passenger",on_delete=models.CASCADE)
    TripAttribute=models.ForeignKey("TripAttribute",on_delete=models.CASCADE)
    TotalPraice=models.DecimalField(max_digits=10,decimal_places=2)
    Created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.Passenger}-{self.TOtalPraice}-{self.Created_at}'
    



