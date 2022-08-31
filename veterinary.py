

class Client: 
    def _init_(self,clientName,cellphone,direction,ticket,pet):
        self.name = clientName
        self.cellphone = cellphone
        self.direction = direction
        self.ticket = ticket
        self.petName=pet
    def CreateClient():
        return "Cliente Creado"


    def searchClient (pNombre):
        return "Cliente Creado" +pNombre

    def ticketCliente(pNombre):
        return "Se facturo al cliente" +pNombre+"$256556"
    
    
class Pet (Client):
    def _init_(self,clientName,cellphone,direction,ticket,pet,namePet,sintoms,food,antibiotics,veterenary):
        super().__init__(clientName,cellphone,direction,ticket,pet)
        self.petName=namePet
        self.sintoms=sintoms
        self.food=food
        self.antibiotics=antibiotics
        self.veterenary =veterenary
        
    def createPet():
        return "Pet Creado"


    def searchPet (pNamePet):
        return "Mascota encontrada" +pNamePet

    def giveFoodPet(pNamepet,food,pNumber):
        return "Useted ha ingresado" + pNamePet + "Comida:" + pNumber + " a la mascota"    
    
class Antibiotics(Pet):
    def _init_(self,namePet,sintoms,food,antibiotics,veterenary,nameAntibiotic,antibioticBrand,antibioticAvailable,description,antibioticAmount):
        super().__init__(namePet,sintoms,food,antibiotics,veterenary)
        self.nameAntibiotics=nameAntibiotic
        self.antibioticbrand=antibioticBrand
        self.antibioticAvailable=antibioticAvailable
        self.description=description
        self.antibioticAmaount= antibioticAmount
        
    def giveAntibiotic():
    insert = int(input("Insert one coin at a time: ").strip())


    antibitics = 50
    total = antibitic- insert

    while insert < antibitoic:
        print("Amount due: ", total)
        return
    if insert == antibitotic:
        print("Change Owed: ", total)
        return
    else:
        print("Please insert the correct amount of: ", antibiotics)   
        
    
    def createAntibitic():
        return "Creado Antibitco"


    def searcAntibitic (pNameAntibiotic):
        return "Antribitic:" +pNameAnntibitic

class Veterenary(Pet):
    def _init_(self,namePet,sintoms,food,antibiotics,veterenary,veterenaryName,veterenaryRoom,veterenaryEspeciality,veterenaryCellphone,veterenarySchedule):    
     super().__init__(namePet,sintoms,food,antibiotics,veterenary)
     self.veterenaryName = veterenaryName
     self.veterenaryRoom = veterenaryRoom
     self.veterenaryEspeciality = veterenaryEspeciality
     self.veterenaryCellphone = veterenaryCellphone
     self.veterenarySchedule = veterenarySchedule
       
    def createVeterenary():
        return "Veterenary Created"


    def searcVeterenary (pNameVeterenary):
        return "Veterenary:" + pNameVeterenary
    
    def callVeterinary(pNameVaeterenary,pVetemnerayRoom)
        return "Tienes un llamado de emeregencia en " + pVeterenaryRoom+ "DR" +p
            
            
      

class Food(Pet):
    def _init_(self,namePet,sintoms,food,antibiotics,veterenary,foodName,foodBrand,foodConsume,foodAvailable,foodPetType):
     super().__init__(namePet,sintoms,food,antibiotics,veterenary)  
     self.foodName = foodName
     self.foodBrand = foodBrand
     self.foodConsume = foodConsume 
     self.foodAvailable = foodAvailable
     self.foodPetType = foodPetType 
    
    def createFood():
        return "Food is created"


    def searcAntibitic (pNameFood):
        return "Food" +foodName
            
    def giveFood():
    insert = int(input("Insert one coin at a time: ").strip())


    dogfood = 50
    total = dogfood- insert

    while insert < dogfood:
        print("Amount due: ", total)
        return
    if insert == dogfood:
        print("Change Owed: ", total)
        return
    else:
        print("Please insert the correct amount of: ", dogfood)   
        
    
    

    


