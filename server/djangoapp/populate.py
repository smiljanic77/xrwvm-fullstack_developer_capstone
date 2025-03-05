from .models import CarMake, CarModel

def initiate():
    car_make_data = [
        {"name":"NISSAN", "description":"Great cars. Japanese technology"},
        {"name":"Mercedes", "description":"Great cars. German technology"},
        {"name":"Audi", "description":"Great cars. German technology"},
        {"name":"Kia", "description":"Great cars. Korean technology"},
        {"name":"Toyota", "description":"Great cars. Japanese technology"},
    ]
    car_make_instances = []
    for data in car_make_data:
            car_make_instances.append(CarMake.objects.create(name=data['name'], description=data['description']))
    # Create CarModel instances with the corresponding CarMake instances
    car_model_data = [
      {"name":"Pathfinder", "car_type":"SUV", "year": 2023, "car_make":car_make_instances[0], "dealer_id": 1, "price": 45000.00},
      {"name":"Qashqai", "car_type":"SUV", "year": 2023, "car_make":car_make_instances[0], "dealer_id": 1, "price": 35000.00},
      {"name":"XTRAIL", "car_type":"SUV", "year": 2023, "car_make":car_make_instances[0], "dealer_id": 1, "price": 40000.00},
      {"name":"A-Class", "car_type":"SUV", "year": 2023, "car_make":car_make_instances[1], "dealer_id": 2, "price": 55000.00},
      {"name":"C-Class", "car_type":"SUV", "year": 2023, "car_make":car_make_instances[1], "dealer_id": 2, "price": 65000.00},
      {"name":"E-Class", "car_type":"SUV", "year": 2023, "car_make":car_make_instances[1], "dealer_id": 2, "price": 75000.00},
      {"name":"A4", "car_type":"SUV", "year": 2023, "car_make":car_make_instances[2], "dealer_id": 3, "price": 58000.00},
      {"name":"A5", "car_type":"SUV", "year": 2023, "car_make":car_make_instances[2], "dealer_id": 3, "price": 62000.00},
      {"name":"A6", "car_type":"SUV", "year": 2023, "car_make":car_make_instances[2], "dealer_id": 3, "price": 70000.00},
      {"name":"Sorrento", "car_type":"SUV", "year": 2023, "car_make":car_make_instances[3], "dealer_id": 4, "price": 45000.00},
      {"name":"Carnival", "car_type":"SUV", "year": 2023, "car_make":car_make_instances[3], "dealer_id": 4, "price": 42000.00},
      {"name":"Cerato", "car_type":"Sedan", "year": 2023, "car_make":car_make_instances[3], "dealer_id": 4, "price": 35000.00},
      {"name":"Corolla", "car_type":"Sedan", "year": 2023, "car_make":car_make_instances[4], "dealer_id": 5, "price": 32000.00},
      {"name":"Camry", "car_type":"Sedan", "year": 2023, "car_make":car_make_instances[4], "dealer_id": 5, "price": 38000.00},
      {"name":"Kluger", "car_type":"SUV", "year": 2023, "car_make":car_make_instances[4], "dealer_id": 5, "price": 48000.00},
        # Add more CarModel instances as needed
    ]
    for data in car_model_data:
            CarModel.objects.create(
                name=data['name'],
                car_make=data['car_make'],
                car_type=data['car_type'],
                year=data['year'],
                dealer_id=data['dealer_id'],
                price=data['price']
            )
