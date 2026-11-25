import metrics

total_tests = int(input("Общее количество тестов: "))
passed_tests = int(input("Из них passed: "))
failed_tests = int(input("Из них failed: "))
broken_tests = int(input("Из них broken: "))
time_sec = int(input("Время выполнения, секунды: "))

success_test = metrics.pass_rate(passed_tests, total_tests)
build_green = metrics.is_build_green(failed_tests, broken_tests)
duration_text = metrics.format_duration(time_sec)

print()
print(f"Прогон: {total_tests} тестов, успешно {success_test}%")
print(f"Сборка зелёная: {build_green}")
print(f"Длительность: {duration_text}")
