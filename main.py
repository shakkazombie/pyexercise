"""
[+] Zakładamy, że mamy trzy rodzaje samolotów na lotnisku.

[+] Każdy samolot ma określoną max. liczbę pasażerów oraz spalanie paliwa na kilometr przelotu.

airplanes = {
   'alfa': {
       'passengers_count': 30,
       'fuel_liters_per_1km': 10
   },
   'beta': {
       'passengers_count': 40,
       'fuel_liters_per_1km': 12
   },
   'gamma': {
       'passengers_count': 50,
       'fuel_liters_per_1km': 15
   }
}


[+] Istnieje lista z zamówieniami

na przeloty o określonych danych:
- długość odcinka
- typ samolotu
- ilość osób z rezerwacją miejsca.


orders = [
   {'distance_km': 10000, 'airplane_type': 'beta', 'passangers': 20},
   {'distance_km': 30000, 'airplane_type': 'gamma', 'passangers': 120}
]


Napisz program do przydzielania miejsc w samolotach osobom
i wypisujący na terminalu przedziały
(ile pelnych samolotów zostało wykorzystanych do realizacji zamówień, jakich samolotow brakuje).




Język programowania dowolny (oprócz języków sztucznych t.j. np: Brainfuck).

Ew. jeśli nie wiesz, jak zacząć zaproponuj, opisz rozwiązanie - jak podchodziłbyś do realizacji takiego kodu/programu i dlaczego.
"""

airplanes = {
    'alfa': {
        'passengers_count': 30,
        'fuel_liters_per_1km': 10
    },
    'beta': {
        'passengers_count': 40,
        'fuel_liters_per_1km': 12
    },
    'gamma': {
        'passengers_count': 50,
        'fuel_liters_per_1km': 15
    }
}

orders = [
    {'distance_km': 10000, 'airplane_type': 'beta', 'passangers': 20},
    {'distance_km': 30000, 'airplane_type': 'gamma', 'passangers': 120}
]

for order in orders:
    order_airplane_type = order['airplane_type']
    passengers_in_airplane = airplanes[order_airplane_type]['passengers_count']
    passengers_in_order = order['passangers']
    passangers_fill = passengers_in_order / passengers_in_airplane
    print (f"w samolocie typu: {order_airplane_type} mamy alokacje pasazerami: {passangers_fill}")    
    print (passangers_fill % passengers_in_order)