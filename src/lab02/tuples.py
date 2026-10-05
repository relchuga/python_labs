def format_record(rec: tuple[str, str, float]) -> str:
    if len(rec) != 3:
        raise ValueError("Нужно ввести 3 данных")
    fio, group, gpa = rec
    if not (0.0 <= gpa <= 5.0):
        raise ValueError("gpa должен быть в диапазоне от 0.0 до 5.0")
    words = fio.strip().split()
    if len(words) > 2:
        norm_fio = words[0].capitalize() + ' ' + '.'.join(name.upper()[0] for name in words[1:]) + '.'
    else:
        norm_fio = words[0].capitalize() + ' ' + words[1].upper()[0] + '.'
    group = group.strip()
    norm_gpa = f'{gpa:.2f}'
    return f'{norm_fio}, гр. {group}, GPA {norm_gpa}'
print(f'("  сидорова  анна   сергеевна ", "ABB-01", 3.999) -> {format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999))}')
