
"""
whois_lookup.py

Performs a WHOIS lookup on a user-provided domain.

Requires:
    pip install python-whois
"""

import whois


def lookup_domain():
    print("=" * 50)
    print("WHOIS Lookup")
    print("=" * 50)

    domain = input("\nEnter a domain (example: python.org): ").strip()

    if not domain:
        print("No domain entered.")
        return

    try:
        result = whois.whois(domain)

        print("\nWHOIS INFORMATION")
        print("-" * 50)
        print(f"Domain: {domain}")
        print(f"Registrar: {result.registrar}")
        print(f"Creation Date: {result.creation_date}")
        print(f"Expiration Date: {result.expiration_date}")
        print(f"Updated Date: {result.updated_date}")
        print(f"Name Servers: {result.name_servers}")
        print(f"Country: {result.country}")

    except Exception as error:
        print("\nLookup failed.")
        print(error)


if __name__ == "__main__":
    lookup_domain()
