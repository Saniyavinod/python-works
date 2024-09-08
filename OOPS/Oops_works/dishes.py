class dishes:
    name=str
    continent=str
    price=int


    def __init__(self,name,continent,price):
        self.name=name
        self.continent=continent
        self.price=price


    def __str__(self):
        return self.name
    

class resturant:
    place=str
    items=list


    def __init__(self,place):
        self.place=place
        self.items=[]

    def add_dish(self,item):
        self.items.append(item)   

    def list_dish(self):

        for b in self.items:
            print(b)


# define before adding to the resturant instance
biriyani_instance=dishes("biriyani","asia",200)
kimchi_instance=dishes("kimchi","korea",4000)
kfc_instance=dishes("kfc","america",500)



resturant_instance=resturant("Kasaba")

resturant_instance.add_dish(biriyani_instance)
resturant_instance.add_dish(kfc_instance)

resturant_instance.list_dish()










