
def filter_words(word_list):
    filtered_list = [word for word in word_list if len(word) >= 4]
    sorted_list = sorted(filtered_list)
    return sorted_list

words = ["яблоко", "стол", "книга", "дом", "кот", "автомобиль", "компьютер"]
filtered_words = filter_words(words)
print(filtered_words)
