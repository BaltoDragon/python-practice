from operator import truediv


def pass_rate(passed, total):  # Процент успешных тестов, округлённый до 2 знаков
    success = passed * 100 / total
    success = round(success, 2)
    return success


def is_build_green(failed, broken):  # True, только если нет ни упавших, ни сломанных
    build_green = failed == 0 and broken == 0
    return build_green


def format_duration(seconds):  # Целые секунды → строка «N мин M сек»
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes} мин {seconds} сек"


def is_within_tolerance(actual, expected,
                        tolerance):  # True, если actual отличается от expected не больше чем на tolerance
    diff = abs(expected - actual)
    return diff <= tolerance