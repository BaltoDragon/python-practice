import metrics

total_test = int(input("Общее количество тестов: "))
passed_test = int(input("Количество успешных тестов: "))

success_test = metrics.pass_rate(passed_test, total_test)

print(f"Прогон: {total_test} тестов, успешно {success_test}%")