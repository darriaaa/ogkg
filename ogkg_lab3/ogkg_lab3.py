import math  
import matplotlib.pyplot as plt  
import random  

# Функція для обчислення відстані між двома точками
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Функція для знаходження найближчої пари точок
def closest_pair(points):
    n = len(points)

    # Якщо менше або рівно дві точки, повертаємо їх та їх відстань
    if n <= 1:
        return None, None, math.inf
    elif n == 2:
        return points[0], points[1], distance(points[0], points[1])

    # Сортуємо точки за їх x-координатою
    sorted_points = sorted(points, key=lambda x: x[0])

    # Розділяємо точки на ліву та праву підмножини
    mid = n // 2
    left_points = sorted_points[:mid]
    right_points = sorted_points[mid:]

    # Рекурсивно знаходимо найближчі пари на кожній підмножині
    left_closest = closest_pair(left_points)
    right_closest = closest_pair(right_points)

    # Вибираємо найменшу знайдену відстань між пар підмножин
    if left_closest[2] < right_closest[2]:
        closest_pair_result = left_closest
    else:
        closest_pair_result = right_closest

    # Знаходимо точки, які можуть бути ближче до роздільної лінії
    strip = []
    for point in sorted_points:
        if abs(point[0] - sorted_points[mid][0]) < closest_pair_result[2]:
            strip.append(point)

    # Перевіряємо чи є точки у полосі, які мають меншу відстань між собою
    strip_closest = closest_strip(strip, closest_pair_result[2])

    # Повертаємо найближчу пару
    if strip_closest[2] < closest_pair_result[2]:
        return strip_closest
    else:
        return closest_pair_result

# Функція для знаходження найближчих пар точок у полосі
def closest_strip(strip, d):
    min_distance = d
    min_pair = None, None

    for i in range(len(strip)):
        for j in range(i+1, len(strip)):
            if strip[j][1] - strip[i][1] >= min_distance:
                break
            elif distance(strip[i], strip[j]) < min_distance:
                min_distance = distance(strip[i], strip[j])
                min_pair = strip[i], strip[j]

    return min_pair[0], min_pair[1], min_distance

# Генерація випадкових точок
def generate_points(num_points, min_val, max_val):
    points = []
    for _ in range(num_points):
        x = random.uniform(min_val, max_val)
        y = random.uniform(min_val, max_val)
        points.append((x, y))
    return points

# Графічне відображення точок та найближчої пари
def plot_closest_pair(points, closest_pair):
    x = [point[0] for point in points]
    y = [point[1] for point in points]

    plt.scatter(x, y)
    plt.plot([closest_pair[0][0], closest_pair[1][0]], [closest_pair[0][1], closest_pair[1][1]], color='red')
    plt.text(closest_pair[0][0], closest_pair[0][1], '1', fontsize=12, ha='right')
    plt.text(closest_pair[1][0], closest_pair[1][1], '2', fontsize=12, ha='right')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Closest Pair of Points')
    plt.show()

# Головна функція
def main():
    num_points = 100 # Кількість випадкових точок
    min_val = 0  # Мінімальне значення координат
    max_val = 100  # Максимальне значення координат
    points = generate_points(num_points, min_val, max_val) 
    closest_pair_result = closest_pair(points)  
    print("Найближча пара точок:", closest_pair_result[:2])
    print("Відстань між ними:", closest_pair_result[2])
    plot_closest_pair(points, closest_pair_result) 

if __name__ == "__main__":
    main()  
