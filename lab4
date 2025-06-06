import heapq

class Car:
    def __init__(self, car_id, model, price, rating):
        self.id = car_id
        self.model = model
        self.price = price
        self.rating = rating

    def __repr__(self):
        return f"ID: {self.id} | {self.model} | ${self.price} | Rating: {self.rating}"


class CarShowroom:
    def __init__(self):
        self.cars = {}
        self.price_heap = []
        self.rating_heap = []

    def add_car(self, car_id, model, price, rating):
        if car_id in self.cars:
            print("Машина з таким ID вже існує.")
            return
        car = Car(car_id, model, price, rating)
        self.cars[car_id] = car
        heapq.heappush(self.price_heap, (-price, car_id))
        heapq.heappush(self.rating_heap, (-rating, car_id))
        print("Машину додано.")

    def delete_car(self, car_id):
        if car_id not in self.cars:
            print("Такої машини не існує.")
            return
        del self.cars[car_id]
        print("Машину видалено.")

    def get_most_expensive(self):
        while self.price_heap:
            _, car_id = self.price_heap[0]
            if car_id in self.cars:
                return self.cars[car_id]
            heapq.heappop(self.price_heap)
        return None

    def get_highest_rated(self):
        while self.rating_heap:
            _, car_id = self.rating_heap[0]
            if car_id in self.cars:
                return self.cars[car_id]
            heapq.heappop(self.rating_heap)
        return None

    def list_cars(self):
        if not self.cars:
            print("Немає жодної машини.")
        for car in self.cars.values():
            print(car)


def main():
    showroom = CarShowroom()

    while True:
        print("\n===== АВТОСАЛОН CLI =====")
        print("1. Додати машину")
        print("2. Видалити машину")
        print("3. Найдорожча машина")
        print("4. Найвищий рейтинг")
        print("5. Всі машини")
        print("6. Вийти")

        choice = input("Обери опцію (1-6): ")

        if choice == '1':
            car_id = input("ID машини: ")
            model = input("Модель: ")
            try:
                price = int(input("Ціна: "))
                rating = float(input("Рейтинг (0-5): "))
            except ValueError:
                print("Невірний формат чисел.")
                continue
            showroom.add_car(car_id, model, price, rating)

        elif choice == '2':
            car_id = input("Введи ID машини для видалення: ")
            showroom.delete_car(car_id)

        elif choice == '3':
            car = showroom.get_most_expensive()
            print("Найдорожча машина:", car if car else "Немає машин.")

        elif choice == '4':
            car = showroom.get_highest_rated()
            print("Машина з найвищим рейтингом:", car if car else "Немає машин.")

        elif choice == '5':
            showroom.list_cars()

        elif choice == '6':
            print("Вихід з програми.")
            break

        else:
            print("Невірна опція. Спробуй ще раз.")


if __name__ == "__main__":
    main()
