import socket

def dns_lookup():
    print("===================================")
    print(" DNS Lookup Tool")
    print("===================================\n")

    domain = input("Enter a domain (example: google.com): ").strip()

    try:
        hostname = socket.gethostbyname_ex(domain)

        print("\nDNS Lookup Results")
        print("----------------------------")
        print(f"Domain: {domain}")
        print(f"Official Hostname: {hostname[0]}")
        print(f"Aliases: {hostname[1]}")
        print(f"IP Addresses:")

        for ip in hostname[2]:
            print(f" - {ip}")

    except socket.gaierror:
        print("\nError: Unable to resolve the domain.")
        print("Check the spelling or your internet connection.")

if __name__ == "__main__":
    dns_lookup()
