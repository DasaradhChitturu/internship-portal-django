def calculate_net_salary(gross_salary, deductions):
    return gross_salary - deductions


def test_calculate_net_salary():
    result = calculate_net_salary(50000, 8000)

    assert result == 42000

def test_calculate_net_salary_with_zero_deductions():
    result = calculate_net_salary(30000, 0)

    assert result == 30000

def test_calculate_net_salary_when_deductions_equal_gross():
    result = calculate_net_salary(20000, 20000)

    assert result == 0

def calculate_net_salary(gross_salary, deductions):
    if gross_salary < 0:
        raise ValueError("Gross salary cannot be negative.")

    if deductions < 0:
        raise ValueError("Deductions cannot be negative.")

    if deductions > gross_salary:
        raise ValueError("Deductions cannot exceed gross salary.")

    return gross_salary - deductions

import pytest


def test_calculate_net_salary_with_excessive_deductions():
    with pytest.raises(
        ValueError,
        match="Deductions cannot exceed gross salary."
    ):
        calculate_net_salary(30000, 35000)