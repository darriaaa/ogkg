#Регіональний пошук. Метод 2-d дерева.

import matplotlib.pyplot as plt 

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def build_kd_tree(points, depth=0):
    if not points:  # Перевірка, чи список точок не пустий
        return None

    axis = depth % 2  # Вибираємо координату для розділення (0 - x, 1 - y) залеж від грибини дерева
    points.sort(key=lambda point: getattr(point, ['x', 'y'][axis]))  # Сортуємо точки за вибраною координатою

    median = len(points) // 2  # Знаходимо медіану для подальшого розділення
    node = points[median]  # Створюємо вузол дерева з точкою, яка знаходиться при медіані

    # Рекурсивно будуємо ліве та праве піддерево
    node.left = build_kd_tree(points[:median], depth + 1)
    node.right = build_kd_tree(points[median + 1:], depth + 1)

    return node  

def search_region(node, region, depth=0):
    if node is None:  # Якщо вузол порожній, повертаємо пустий список
        return []

    axis = depth % 2  # Вибираємо координату для порівняння (0 - x, 1 - y)
    if region[0][axis] <= getattr(node, ['x', 'y'][axis]) <= region[1][axis]:
        # Перевіряємо, чи точка потрапляє у вказаний регіон по відповідній координаті
        result = [node]  # Якщо так, додаємо точку до результату
    else:
        result = []  # Якщо ні, результат порожній

    # Рекурсивно продовжуємо пошук у відповідних піддеревах
    if getattr(node, ['x', 'y'][axis]) > region[0][axis]:
        result += search_region(node.left, region, depth + 1)
    if getattr(node, ['x', 'y'][axis]) < region[1][axis]:
        result += search_region(node.right, region, depth + 1)

    # Фільтруємо результат, залишаючи лише точки, що повністю знаходяться всередині регіону
    result = [point for point in result if region[0][0] <= point.x <= region[1][0] and region[0][1] <= point.y <= region[1][1]]

    return result  # Повертаємо список точок, які знаходяться у регіоні

def plot_points(points, region=None):
    x = [point.x for point in points]  # Отримуємо координати x точок
    y = [point.y for point in points]  # Отримуємо координати y точок

    # Візуалізуємо точки на графіку
    plt.scatter(x, y, color='blue', label='Точки')

    # Якщо передано регіон, візуалізуємо його також
    if region:
        x_region = [region[0][0], region[1][0], region[1][0], region[0][0], region[0][0]]
        y_region = [region[0][1], region[0][1], region[1][1], region[1][1], region[0][1]]
        plt.plot(x_region, y_region, color='red', linestyle='--', label='Регіон')

    # Налаштовуємо осі та заголовок графіку
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Дводольне дерево та регіон')

    # Додаємо легенду та сітку
    plt.legend()
    plt.grid(True)

    # Показуємо графік
    plt.show()

def main():
    points = [Point(2, 3), Point(5, 4), Point(9, 6), Point(4, 7), Point(8, 1), Point(7, 2), Point(5, 5), Point(0, 0)]  # Створюємо список точок
    root = build_kd_tree(points)  # Побудова дводольного дерева зі списку точок

    region = [(3, 2), (8, 5)]  # Вказуємо прямокутний регіон для пошуку
    points_in_region = search_region(root, region)  # Виконуємо регіональний пошук у заданому регіоні

    plot_points(points, region)  # Візуалізуємо точки та вказаний регіон

    print("Точки у заданому регіоні:")
    for point in points_in_region:
        print(f"({point.x}, {point.y})")  # Виводимо точки, що знаходяться у заданому регіоні

if __name__ == "__main__":
    main()
