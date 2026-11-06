from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx
json_to_csv("data/samples/people.json","data/out/people.csv")
csv_to_json("data/samples/cities.csv", "data/out/cities.json")
csv_to_xlsx("data/samples/people.csv", "data/out/people.xlsx")