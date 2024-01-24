import json
from datetime import datetime


def process_results(competitors_path, results_path, output_path='final_results.json'):

    with open(competitors_path, 'r', encoding='utf-8-sig') as file:
        competitors_data = json.load(file)

    with open(results_path, 'r', encoding='utf-8-sig') as file:
        results_data = file.readlines()

    results_list = []

    print("Занятое место\tНагрудный номер\tИмя\tФамилия\tРезультат")

    for result_line in results_data:
        parts = result_line.strip().split()
        number = parts[0]
        name = competitors_data[number]['Name']
        surname = competitors_data[number]['Surname']
        time_str = parts[2]
        time_format = '%H:%M:%S,%f'
        time_obj = datetime.strptime(time_str, time_format)
        formatted_time = time_obj.strftime('%M:%S,%f')[:-3]

        result = {
            'Нагрудный номер': number,
            'Имя': name,
            'Фамилия': surname,
            'Результат': formatted_time
        }

        results_list.append(result)

    sorted_results = sorted(results_list, key=lambda x: datetime.strptime(x['Результат'], '%M:%S,%f'))

    for i, result in enumerate(sorted_results):
        print(f"{i+1}\t{result['Нагрудный номер']}\t{result['Имя']}\t{result['Фамилия']}\t{result['Результат']}")

    final_results_dict = {str(i+1): sorted_results[i] for i in range(len(sorted_results))}

    with open(output_path, 'w', encoding='utf-8') as file:
        json.dump(final_results_dict, file, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    process_results(
        competitors_path=r'C:\Users\Paynil\Downloads\22-01-2024-Paynil-main\22-01-2024-Paynil-main\competitors2.json',
        results_path=r'C:\Users\Paynil\Downloads\22-01-2024-Paynil-main\22-01-2024-Paynil-main\results_RUN.txt'
    )