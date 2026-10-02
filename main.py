import requests
import json

def dish_fetch(num):
    response = requests.get("https://api-colombia.com/api/v1/TypicalDish")

    platos = response.json()
    
    if 1 <= num <= len(platos):
        return platos[num - 1]
    return {}

def main():
    print("Bienvenido al restaurante Doña Teresita. Por facor escoga los Platos disponibles:")
    
    response = requests.get("https://api-colombia.com/api/v1/TypicalDish")
    platos = response.json()
    
    for i, plato in enumerate(platos, 1):
        print(f"{i}. {plato['name']}")
    
    opcion = int(input("Elige el número de un plato sumercé: "))
    resultado = dish_fetch(opcion)
    print("Excelente elección paisano, en un momento lo estaremos atendiendo:" , resultado)

if __name__ == "__main__":
    main()