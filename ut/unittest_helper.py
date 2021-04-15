import inspect


def assert_message(expected, actual):
    test_name = inspect.stack()[2][3]
    return f'Test {test_name} failed. Expected={expected}. Actual={actual}'


def assert_message(scenario, expected, actual):
    return f'Test {scenario} failed. Expected={expected}. Actual={actual}'
