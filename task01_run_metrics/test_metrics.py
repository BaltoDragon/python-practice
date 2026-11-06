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