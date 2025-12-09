def main():
    products = {
        "Телефон": frozenset({"техника", "электроника"}),
        "Самурайский меч": frozenset({"редкое", "оружие"}),
        "Холодильник": frozenset({"бытовое", "техника"}),
        "Золотой самородок": frozenset({"редкое", "драгоценности"}),
    }

    def find_by_category(category):
        """Возвращает set товаров, содержащих указанную категорию"""
        result = set()
        for product, categories in products.items():
            if category in categories:
                result.add(product)
        return result

    def add_product():
        """Добавление нового товара"""
        name = input("Введите название товара: ").strip()
        if not name:
            print("Название товара не может быть пустым!")
            return

        if name in products:
            print("Такой товар уже существует!")
            return

        categories_input = input("Введите категории через запятую: ").strip()
        if not categories_input:
            print("Нужно указать хотя бы одну категорию!")
            return

        categories = {cat.strip() for cat in categories_input.split(",") if cat.strip()}
        products[name] = frozenset(categories)
        print(f"Товар '{name}' успешно добавлен!")

    def show_all_products():
        """Вывод всех товаров"""
        if not products:
            print("Список товаров пуст.")
            return


        sorted_products = sorted(products.items(), key=lambda item: len(item[0]))

        print("\n" + "=" * 50)
        print("СПИСОК ТОВАРОВ (отсортировано по длине названия):")
        print("=" * 50)

        for product, categories in sorted_products:
            print(f"{product}: {', '.join(sorted(categories))}")
        print("=" * 50)

    def find_by_category_menu():
        """Поиск товаров по категории"""
        category = input("Введите категорию для поиска: ").strip()
        if not category:
            print("Категория не может быть пустой!")
            return

        found_products = find_by_category(category)

        if found_products:
            print(f"\nТовары в категории '{category}':")
            for product in sorted(found_products):
                print(f"  - {product}")
        else:
            print(f"Товаров в категории '{category}' не найдено.")


    while True:
        print("\n" + "=" * 50)
        print("магазин")
        print("=" * 50)
        print("1. Добавить товар")
        print("2. Вывести все товары")
        print("3. Найти товары по категории")
        print("4. Выйти")
        print("=" * 50)

        choice = input("Выберите действие (1-4): ").strip()

        if choice == "1":
            add_product()
        elif choice == "2":
            show_all_products()
        elif choice == "3":
            find_by_category_menu()
        elif choice == "4":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите от 1 до 4.")


if __name__ == "__main__":
    main()




