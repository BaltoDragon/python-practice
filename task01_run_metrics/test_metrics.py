import metrics


def test_pass_rate_positive():
    assert metrics.pass_rate(45, 50) == 90.0


def test_pass_rate_float_percent():
    assert metrics.pass_rate(1, 3) == 33.33


def test_pass_rate_zero_passed():
    assert metrics.pass_rate(0, 10) == 0


def test_pass_rate_is_result_float():
    assert type(metrics.pass_rate(1, 3)) == type(33.33)


def test_pass_rate_input_float():
    assert type(metrics.pass_rate(1.0, 3.0)) == type(33.33)


def test_is_build_green_true():
    assert metrics.is_build_green(0, 0)


def test_is_build_green_false_zero_failed():
    assert not metrics.is_build_green(0, 2)


def test_is_build_green_false_zero_broken():
    assert not metrics.is_build_green(1, 0)


def test_format_duration_zero_time():
    assert metrics.format_duration(0) == "0 мин 0 сек"


def test_format_duration_correct_time():
    assert metrics.format_duration(125) == "2 мин 5 сек"


def test_format_duration_zero_minutes():
    assert metrics.format_duration(59) == "0 мин 59 сек"


def test_format_duration_zero_seconds():
    assert metrics.format_duration(120) == "2 мин 0 сек"


def test_is_within_tolerance_true():
    assert metrics.is_within_tolerance(10.2, 10.0, 0.5)


def test_is_within_tolerance_false():
    assert not metrics.is_within_tolerance(9.4, 10.0, 0.5)


def test_is_within_tolerance_true_high_precision():
    result_function = metrics.is_within_tolerance(1.0000000023, 1.0000000011, 0.000000002)
    assert result_function


def test_is_within_tolerance_false_high_precision():
    result_function = metrics.is_within_tolerance(12, 1.0000000011, 0.000000002)
    assert not result_function


def test_is_within_tolerance_false_reverse():
    assert not metrics.is_within_tolerance(-9.4, -10.0, 0.5)


def test_is_within_tolerance_true_reverse():
    assert metrics.is_within_tolerance(-10.2, -10.0, 0.5)


def test_is_within_tolerance_int():
    assert not metrics.is_within_tolerance(10, 11, 0.5)


def test_is_within_tolerance_limit_value_1():
    assert metrics.is_within_tolerance(1.1, 1.0, 0.1)


def test_is_within_tolerance_limit_value_2():
    assert metrics.is_within_tolerance(10.5, 10.0, 0.5)


def test_is_within_tolerance_hard_diff():
    assert not metrics.is_within_tolerance(10.9, 1.0, 0.5)
