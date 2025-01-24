from Apple import Apple
from Banana import Banana
from Chicken import Chicken
from Dog import Dog
from interfaces import Edible
from interfaces import Weighable
from Fruit import Fruit
from Animal import Animal
from Person import Person
from Favourite import Favourite


if __name__=='__main__':
    a = Apple()
    b = Banana()
    c = Chicken()
    d = Dog()

    item_list = [a, b, c, d]
    for i in item_list:
        if isinstance(i, Edible):
            i.how_to_eat()
        if isinstance(i, Fruit):
            print(f'The price of {i.get_name()} is {i.get_price()}')
        if isinstance(i, Animal):
            i.make_sound()
        print(f'The weight of {i.get_name()} is {i.get_weight()}')
        
    fruit_list = [a,b]
    fruit_list.sort()
    for f in fruit_list:
        print(f'The price of {f.get_name()} is ${f.get_price()}')
        
    print("---------------------------- Favourite --------------------------------")
    
    nick = Person("Nick", "Brantford")
    petar = Person("Petar", "Milton")
    
    nick_fav = Favourite(nick)
    petar_fav = Favourite(petar)
    
    for i in item_list:
        if isinstance(i,Edible):
            nick_fav.add_to_favourite(i)
        if isinstance(i,Animal):
            petar_fav.add_to_favourite(i)
            
    print(f'{nick.get_name()} Favourite Items: ')
    for f in nick_fav.get_favourite_list():
        print(f' - {f.get_name()}')
        
    print(f'{petar.get_name()} Favourite Items: ')
    for f in petar_fav.get_favourite_list():
        print(f' - {f.get_name()}')



 