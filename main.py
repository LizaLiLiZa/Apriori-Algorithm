def apriori_func(reference_elements, r):
    result_elements = ""
    for i in range(1, len(reference_elements)):
        # Делим индексы на левую (x) и правую (y) части
        x_indices = reference_elements[:i]
        y_indices = reference_elements[i:]

        # Используем списковые включения для формирования x и y
        x = [r[j] for j in x_indices]
        y = [r[j] for j in y_indices]

        count_x = count_xy = 0

        # Проход по данным и проверка поддержки для x и xy
        for transaction in data:
            if set(x).issubset(transaction):
                count_x += 1
                if set(y).issubset(transaction):
                    count_xy += 1

        # Подсчет поддержки и уверенности
        if count_x and count_xy:
            support_x = (count_x / len(data)) * 100
            support_xy = (count_xy / len(data)) * 100
            confidence_x = (support_xy / support_x) * 100

            # Условие для печати правил и добавления в проверенные элементы
            if support_x >= min_support and confidence_x >= min_confidence:
                if [set(x), set(y)] not in elements_checked:
                    print(f"({x} --> {y}) s = {support_x:.2f}% c = {confidence_x:.2f}%")
                    result_elements += ''.join(map(str, reference_elements))
                    elements_checked.append([set(x), set(y)])

    return result_elements


def combination_func(elements, k):
    if len(elements) < k:
        return

    array_count = list(range(k))
    result_elements = ""

    while array_count[0] < len(elements):
        if len(set(array_count)) == k:
            result_elements += apriori_func(array_count, elements)

        # Обновляем индексы для следующей комбинации
        array_count[-1] += 1
        for i in range(k - 1, 0, -1):
            if array_count[i] >= len(elements):
                array_count[i] = 0
                array_count[i - 1] += 1

        if array_count[0] >= len(elements):
            break

    # Преобразуем результат в новый список элементов
    result_indices = list(map(int, set(result_elements)))
    elements_new = [elements[i] for i in result_indices if i < len(elements)]
    
    if elements_new:
        combination_func(elements_new, k + 1)


# Входные данные
data = [
    ["П", "С", "М", "К"],
    ["С", "Ш", "К"],
    ["М", "П", "С", "Ш", "К"],
    ["Ш", "К", "С"],
    ["Ш", "М", "П"],
    ["М", "П"],
    ["П", "С", "М"],
    ["Ш", "С", "М", "К"],
    ["С", "М", "П"],
    ["Ш", "М"]
]
min_support = 40
min_confidence = 80

elements_checked = []

if __name__ == "__main__":
    # Получаем уникальные элементы из данных
    elements = list(set(item for sublist in data for item in sublist))
    print(elements)
    combination_func(elements, 2)
