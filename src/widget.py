def get_similar(words: list[str]) -> list[str]:
    """
    Функция фильтрует список слов
    :param words: список слов
    :return: список слов с одиннаковой буквой в начале и конце
    """
    similar_start_end_words = []
    if words:

        for word in words:
            if word:

                if word[0] == word[-1]:

                    similar_start_end_words.append(word)

        return similar_start_end_words

    return []


# widget
def get_max_multiply(numbers: list[int]) -> int:
    """
    Функция ищет максимальное произведение двух чисел
    :param numbers: список чисел
    :return: масимальное произведение
    """
    nums = sorted(numbers)
    if len(nums) < 2:

        return 0

    if nums[-1] * nums[-2] > nums[0] * nums[1]:

        return nums[-1] * nums[-2]

    return nums[0] * nums[1]
