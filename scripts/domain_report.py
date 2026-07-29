"""
domain_report.py

Creates a simple domain investigation report.
"""

import csv
import socket


def generate_report():

    print("=" * 50)
    print("Domain Investigation Report")
    print("=" * 50)

    file = "../data/sample_domains.csv"

    try:

        with open(file, "r") as csv_file:

            reader = csv.DictReader(csv_file)


            for row in reader:

                domain = row["Domain"]

                print("\nDomain:", domain)

                try:

                    ip = socket.gethostbyname(domain)

                    print("IP Address:", ip)

                except:

                    print("Unable to resolve")


    except FileNotFoundError:

        print("sample_domains.csv missing")


if __name__ == "__main__":
    generate_report()
