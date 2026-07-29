"""
ioc_parser.py

Reads Indicators of Compromise from iocs.csv
"""

import csv
import os


def read_iocs():

    print("=" * 50)
    print("IOC Parser")
    print("=" * 50)

    file_path = "../data/iocs.csv"

    try:

        with open(file_path, "r") as file:

            reader = csv.DictReader(file)

            for row in reader:

                print("\nIOC Type:", row["IOC Type"])
                print("Value:", row["Value"])
                print("Description:", row["Description"])
                print("-" * 40)


    except FileNotFoundError:

        print("iocs.csv not found")


if __name__ == "__main__":
    read_iocs()
