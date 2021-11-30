# PUTF21 Final Project - Rebecca Bang

#from numpy import int64, float64
import pandas as pd
import os
from recipes import *
import pytest

path2 = os.path.dirname(os.path.realpath(__file__))
df = pd.read_csv(path2 + '\\data\\recipes.csv', encoding='utf8')

def test_name_exists():
    """Test recipe name is not missing"""
    name = df['name1'].isnull().values.any()
    assert name == False

def test_filename():
    """Test filename values are *.txt"""
    file = df['filename'].values.any()
    assert file.endswith('.txt') == True

def test_lines():
    """Test number of steps in each recipe is greater than 1"""
    col = df['filename']
    for val in col:
        count = 0

        with open(f"{path2}\\data\\{val}",'r') as file:
            for line in file:
                if line.strip():
                    count += 1
        assert count > 1


# future implementations
# - looking for corrupted characters from character languages
