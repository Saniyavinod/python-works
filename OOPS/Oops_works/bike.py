class bike:
    name=str
    brand=str
    price=int

    def __init__(self,name,brand,price):
        self.name=name
        self.brand=brand
        self.price=price

    def __str__(self):
        return self.name
        

class showroom:
    name=str
    place=str
    bikes=list

    def __init__(self,name,place):
        self.name=name
        self.place=place
        self.bikes=[]

    def add_vehicle(self,bike):
        self.bikes.append(bike)

    def list_vehicle(self):
        for b in self.bikes:
            print(b)






hunter_instance=bike("hunter","honda",100000)
himalaya_instance=bike("himalayan","jeep",218880)
dominar_instance=bike("dominar","do",293903)
honda_instance=bike("honda","dh",8830300)


showroom_instance=showroom("popular","kakkanad")
showroom_instance.add_vehicle(hunter_instance)
showroom_instance.add_vehicle(dominar_instance)

showroom_instance.list_vehicle()


showroom_instance2=showroom("fjjf","kannur")
showroom_instance2.add_vehicle(himalaya_instance)
showroom_instance2.add_vehicle(dominar_instance)
showroom_instance2.list_vehicle()



