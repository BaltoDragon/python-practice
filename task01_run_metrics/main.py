import metrics

total_tests = int(input("Общее количество тестов: "))
passed_test = int(input("Из них passed: "))
failed_test = int(input("Из них failed: "))
broken_test = int(input("Из них broken: "))
time_sec = int(input("Время выполнения, секунды: "))

success_test = metrics.pass_rate(passed_test, total_tests)
build_green = metrics.is_build_green(failed_test, broken_test)
duration_text = metrics.format_duration(time_sec)

print()
print(f"Прогон: {total_tests} тестов, успешно {success_test}%")
print(f"Сборка зелёная: {build_green}")
print(f"Длительность: {duration_text}")
