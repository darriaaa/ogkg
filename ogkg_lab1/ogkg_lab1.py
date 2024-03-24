import matplotlib.pyplot as plt


def localize_point(point, partition):

    """
    Функція для локалізації точки на планарному розбитті методом ланцюгів.
    :param point: Координати точки у форматі (x, y).
    :param partition: Список ланцюгів у форматі [[(x1, y1), (x2, y2), ..., (xn, yn)], ...].
    :return: Номер ланцюга, у якому знаходиться точка. Якщо точка не належить жодному ланцюгу, повертає None.
    """
    
    # Визначення функції для перевірки чи знаходиться точка всередині ланцюга
    def is_inside(point, chain):
        crossings = 0
        n = len(chain)
        for i in range(n):
            x1, y1 = chain[i]
            x2, y2 = chain[(i + 1) % n]
            if y1 == y2:  # Якщо відрізок горизонтальний, пропускаємо його
                continue
            if min(y1, y2) < point[1] <= max(y1, y2):
                x_intersection = (point[1] - y1) * (x2 - x1) / (y2 - y1) + x1  # Знаходимо x-координату точки перетину прямої відрізка з горизонтальним променем
                if x_intersection > point[0]:  # Якщо x-координата перетину більша за x-координату точки, збільшуємо лічильник перетинів
                    crossings += 1
        return crossings % 2 == 1  # Повертаємо True, якщо кількість перетинів непарна (точка всередині), інакше - False
    
    # Проходимось по всіх ланцюгах і перевіряємо, чи знаходиться точка всередині кожного ланцюга
    for i, chain in enumerate(partition):
        if is_inside(point, chain):
            return i  # Якщо точка знаходиться всередині ланцюга
    return None  # Якщо точка не належить жодному ланцюгу


def plot_partition(point, partition, localized_chain_index=None):
    """
    Функція для візуалізації планарного розбиття разом з точкою.

    """
    plt.figure(figsize=(8, 6))

    for chain in partition:
        x, y = zip(*chain)
        plt.plot(x + (x[0],), y + (y[0],), 'k-')

    plt.plot(point[0], point[1], 'ro')

    if localized_chain_index is not None:
        chain = partition[localized_chain_index]
        centroid_x = sum(x for x, _ in chain) / len(chain)
        centroid_y = sum(y for _, y in chain) / len(chain)
        plt.text(centroid_x, centroid_y, f"Ланцюг {localized_chain_index + 1}", fontsize=12, color='blue')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Локалізація точки на планарному розбитті')
    plt.grid(True)
    plt.axis('equal')
    plt.show()



# Приклад використання 1
point_to_localize = (2, 3)
partition = [[(1, 1), (4, 1), (4, 4), (1, 4)], [(5, 1), (8, 1), (8, 4), (5, 4)]]

localized_chain_index = localize_point(point_to_localize, partition)
plot_partition(point_to_localize, partition, localized_chain_index)

localized_chain_index = localize_point(point_to_localize, partition)
if localized_chain_index is not None:
    print(f"Точка лежить в ланцюзі під номером {localized_chain_index + 1}.")  # Виводимо номер ланцюга, якщо точка виявлена всередині
else:
    print("Точка не належить жодному ланцюгу.")  # Виводимо повідомлення, якщо точка не знайдена всередині жодного ланцюга

# Приклад 2
point_to_localize = (6, 3)
partition = [[(1, 1), (4, 1), (4, 4), (1, 4)], [(5, 1), (8, 1), (8, 4), (5, 4)]]

localized_chain_index = localize_point(point_to_localize, partition)
if localized_chain_index is not None:
    print(f"Точка лежить в ланцюзі під номером {localized_chain_index + 1}.")
else:
    print("Точка не належить жодному ланцюгу.")

localized_chain_index = localize_point(point_to_localize, partition)
plot_partition(point_to_localize, partition, localized_chain_index)


# Приклад 3
point_to_localize = (7, 3)
partition = [[(1, 1), (4, 1), (4, 4), (1, 4)], [(5, 1), (8, 1), (8, 4), (5, 4)], [(6, 3), (9, 3), (9, 6), (6, 6)]]

localized_chain_index = localize_point(point_to_localize, partition)
if localized_chain_index is not None:
    print(f"Точка лежить в ланцюзі під номером {localized_chain_index + 1}.")
else:
    print("Точка не належить жодному ланцюгу.")

localized_chain_index = localize_point(point_to_localize, partition)
plot_partition(point_to_localize, partition, localized_chain_index)
