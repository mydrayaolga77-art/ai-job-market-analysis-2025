import pandas as pd
import pytest

def test_data_loading():
    """Проверяет, что файл загружается и содержит данные"""
    df = pd.read_csv('AI_Market_Report_2025_cleaned.csv')
    assert not df.empty, "Файл пуст!"
    assert 'salary_usd' in df.columns, "В таблице нет колонки salary_usd"

def test_salary_type():
    """Проверяет, что зарплата — это число"""
    df = pd.read_csv('AI_Market_Report_2025_cleaned.csv')
    # Добавьте здесь логику проверки типов данных
    assert df['salary_usd'].dtype in ['int64', 'float64']
