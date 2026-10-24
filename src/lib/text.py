
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    try:
        type(text) == str
    except TypeError:
        print("Введите строку")    
    text = text.strip()
    if casefold == True:
        text = text.casefold()
    if casefold == False:
        text = text.lower()
    if yo2e == True:
        text = text.replace("ё", "е")
        text = text.replace("Ё", "Е")
    text = text.replace('\t', ' ')
    text = text.replace('\r', ' ')
    text = text.replace('\n', ' ')
    text = text.strip()
    text = ' '.join(x for x in text.split())
    return text

def tokenize(text: str) -> list[str]:
    try:
        type(text) == str
    except TypeError:
        print("Введите строку")
    text = normalize(text)
    import re
    tokens = re.findall(r"\w+(?:-\w+)*", text)
    return tokens

def count_freq(tokens: list[str]) -> dict[str, int]:
    try:
        type(tokens) == list
    except TypeError:
        print("Введите список")    
    st = sorted(set(tokens))
    res = {key: 0 for key in st}
    for val in tokens:
        res[val] += 1
    return res

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1],x[0]))
    return sorted_items[:n]

if __name__ == '__main__':
    # normalize
    assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
    assert normalize("ёжик, Ёлка") == "ежик, елка"

    # tokenize
    assert tokenize("привет, мир!") == ["привет", "мир"]
    assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
    assert tokenize("2025 год") == ["2025", "год"]

    # count_freq + top_n
    freq = count_freq(["a","b","a","c","b","a"])
    assert freq == {"a":3, "b":2, "c":1}
    assert top_n(freq, 2) == [("a",3), ("b",2)]

    # тай-брейк по слову при равной частоте
    freq2 = count_freq(["bb","aa","bb","aa","cc"])
    assert top_n(freq2, 2) == [("aa",2), ("bb",2)]
    print('Все тесты пройдены!')