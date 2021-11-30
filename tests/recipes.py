# PUTF21 Final Project - Rebecca Bang

from time import sleep
import pandas as pd
import os

path2 = os.path.dirname(os.path.realpath(__file__))
df = pd.read_csv(path2 + '\\data\\recipes.csv')

class RecipeList(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(
                RecipeList, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def pick_recipe(self, wine_type):
        return Recipes.pick_recipe(wine_type)

class Recipes(object):
    def __init__(self, num):
        self.num = num

    def name1(self):
        s = df['name1'].fillna('N/A')
        return s[self.num]

    def time(self):
        s = df['time']
        return s[self.num]

    def unit(self):
        s = df['unit']
        return s[self.num]

    def notes(self):
        s = df['notes'].fillna('N/A')
        return s[self.num]

    def desc(self):
        print(f"{__class__.name1(self)}\n")
        sleep(0.5)
        
        s = df['filename']
        x = s[self.num]
        f = open(f"{path2}\\data\\{x}",'r')
        Lines = f.readlines()

        count = 0
        for line in Lines:
            count += 1
            print(f"Step {count}:   {line.strip()}")
            sleep(0.5)
        f.close()

        print(f"\n{'Cooking time: '}{__class__.time(self)} {__class__.unit(self)}")
        sleep(0.5)
        print(f"{'Notes: '}{__class__.notes(self)}\n")
        sleep(0.5)

    @staticmethod
    def pick_recipe(option):
        while True:
            print(f"{'=' * 50}\n"+"-- List of recipes --\n")
            df2 = df[['id','name1']]
            print(df2.to_string(index=False, header=None))
            selection = input("\n(Press 'q' to quit)\nEnter your selection: ")
            if selection == 'q':
                break
            else:
                print(f"{'=' * 50}\n")
                y = int(selection)-1
                x = Recipes(y)
                x.desc()

def main():
    while True:
        print(f"{'=' * 50}\n"+"-- List of recipes --\n")
        df2 = df[['id','name1']]
        print(df2.to_string(index=False, header=None))
        selection = input("\n(Press 'q' to quit)\nEnter your selection: ")
        if selection == 'q':
            break
        else:
            print(f"{'=' * 50}\n")
            y = int(selection)-1
            x = Recipes(y)
            x.desc()

if __name__ == "__main__":
    main()
