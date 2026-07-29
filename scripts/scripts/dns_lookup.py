import socket

def dns_lookup():
    domain = input("Enter a domain: ").strip()

    try:
        ip = socket.gethostbyname(domain)

        print("\nDNS Results")
        print("----------------------")
        print("Domain:", domain)
        print("IP Address:", ip)

    except socket.gaierror:
        print("Unable to resolve domain.")

if __name__ == "__main__":
    dns_lookup()
