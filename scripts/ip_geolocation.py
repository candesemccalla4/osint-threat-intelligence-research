"""
ip_geolocation.py

Retrieves basic information about a user-provided IP address.

Requires:
pip install requests
"""

import requests


def lookup_ip():

    print("=" * 50)
    print("IP Geolocation Lookup")
    print("=" * 50)

    ip = input("\nEnter an IP address: ")

    url = f"https://ipapi.co/{ip}/json/"

    try:
        response = requests.get(url, timeout=10)

        data = response.json()

        print("\nResults")
        print("-" * 50)
        print("IP Address:", data.get("ip"))
        print("City:", data.get("city"))
        print("Region:", data.get("region"))
        print("Country:", data.get("country_name"))
        print("Organization:", data.get("org"))

    except Exception as error:
        print("Error:", error)


if __name__ == "__main__":
    lookup_ip()
