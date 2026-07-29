import whois

def lookup_domain():
    domain = input("Enter a domain (example: example.com): ").strip()

    try:
        info = whois.whois(domain)

        print("\n----- WHOIS INFORMATION -----")
        print(f"Domain: {domain}")
        print(f"Registrar: {info.registrar}")
        print(f"Creation Date: {info.creation_date}")
        print(f"Expiration Date: {info.expiration_date}")
        print(f"Name Servers: {info.name_servers}")
        print(f"Country: {info.country}")

    except Exception as e:
        print("Lookup failed.")
        print(e)

if __name__ == "__main__":
    lookup_domain()
