import argparse
import csv
from dbfread import DBF


def main():
    parser = argparse.ArgumentParser(
        description="Фильтрация и конвертация DBF файлов в CSV."
    )
    
    parser.add_argument(
        "-i", "--input", required=True, help="Путь к исходному файлу DBF",
    )
    parser.add_argument(
        "-o", "--output", required=True, help="Путь для сохранения CSV файла",
    )
    
    parser.add_argument(
        "-f", "--field", help="Имя поля (колонки) DBF, по которому выполняется поиск",
    )
    
    parser.add_argument(
        "-q", "--query", nargs="+",
        help="Ключевое слово или список слов для поиска (через пробел)",
    )
    parser.add_argument(
        "-s", "--sort", help="Имя поля (колонки), по которой нужно отсортировать результат", 
    )
    parser.add_argument(
        "-e", "--encoding",
        default="cp866",
        help="Кодировка DBF файла (по умолчанию: cp866)",
    )
    
    args = parser.parse_args()
    
    
    if args.query and not args.field:
        parser.error(
            "Аргумент --query (-q) требует указания пола через ключ --field (-f)."
        )
        
    print(f"Чтение файла {args.input}...")
    table = DBF(args.input, encoding=args.encoding)
    
    search_queries = [q.lower() for q in args.query] if args.query else []
    filtered_records = []
    
    for record in table:
        if search_queries and args.field:
            field_value = str(record.get(args.field, "")).lower()
            
            if not any(query in field_value for query in search_queries):
                continue
            
        filtered_records.append(record)
        
    if args.sort:
        if filtered_records and args.sort in filtered_records[0]:
            print(f"Сортировка по полю '{args.sort}'...")
            filtered_records.sort(
                key=lambda x: (
                    x.get(args.sort) is None,
                    str(x.get(args.sort, "")).lower()
                )
            )
        else:
            print(
                f"Предупреждение! Поле '{args.sort}' для сортировки не найдено в файле"
            )
            
    with open (
        args.output, mode="w", newline="", encoding="utf-8-sig"
    ) as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=table.field_names)
        writer.writeheader()
        writer.writerows(filtered_records)
        
    print(f"Готово! Записей сохранено: {len(filtered_records)} в файл {args.output}")
    
    
if __name__ == "__main__":
    main()