import metrics


def test_pass_rate_positive():
    test_passed = 45
    test_total = 50
    test_success = 90.0
    result_success = metrics.pass_rate(test_passed, test_total)
    assert result_success == test_success


def test_pass_rate_float_percent():
    test_passed = 1
    test_total = 3
    test_success = 33.33
    result_success = metrics.pass_rate(test_passed, test_total)
    assert result_success == test_success


def test_pass_rate_zero_passed():
    test_passed = 0
    test_total = 10
    test_success = 0
    result_success = metrics.pass_rate(test_passed, test_total)
    assert result_success == test_success


def test_pass_rate_is_result_float():
    test_passed = 1
    test_total = 3
    test_success = 33.33
    result_success = metrics.pass_rate(test_passed, test_total)
    assert type(result_success) == type(test_success)


def test_pass_rate_input_float():
    test_passed = 1.0
    test_total = 3.0
    test_success = 33.33
    result_success = metrics.pass_rate(test_passed, test_total)
    assert type(result_success) == type(test_success)


def test_is_build_green_true():
    result_test = True
    result_function = metrics.is_build_green(0, 0)
    assert result_function == result_test


def test_is_build_green_false_zero_failed():
    result_test = False
    result_function = metrics.is_build_green(0, 2)
    assert result_function == result_test


def test_is_build_green_false_zero_broken():
    result_test = False
    result_function = metrics.is_build_green(1, 0)
    assert result_function == result_test

def test_format_duration_zero_time():
    result_string = "0 мин 0 сек"
    result_function = metrics.format_duration(0)
    assert result_function == result_string


def test_format_duration_correct_time():
    result_string = "2 мин 5 сек"
    result_function = metrics.format_duration(125)
    assert result_function == result_string


def test_format_duration_zero_minutes():
    result_string = "0 мин 59 сек"
    result_function = metrics.format_duration(59)
    assert result_function == result_string


def test_format_duration_zero_seconds():
    result_string = "2 мин 0 сек"
    result_function = metrics.format_duration(120)
    assert result_function == result_string