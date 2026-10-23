def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    try:
        type(text) == str
    except TypeError:
        print("Введите строку")    
    text = text.strip()
    if casefold == True:
        text = text.casefold()
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
    dicc = count_freq(freq)
    res = []
    for key, value in dicc.items():
        res.append((key,value))
    return res[:n]
