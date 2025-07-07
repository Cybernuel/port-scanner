import socket
import concurrent.futures
import time

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((ip, port))
        return port
    except:
        return None
    finally:
        sock.close()


def scan_ports(ip, start_port=1, end_port=1024):
    open_ports = []

    print(f"Scanning {ip} from port {start_port} to {end_port}...\n")
    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = {executor.submit(scan_port, ip, port): port for port in range(start_port, end_port + 1)}
        for future in concurrent.futures.as_completed(futures):
            port = future.result()
            if port:
                open_ports.append(port)

    duration = round(time.time() - start_time, 2)
    print(f"\n✅ Scan complete in {duration} seconds.")
    print("🔓 Open Ports:", open_ports if open_ports else "None found")

if __name__ == "__main__":
    target_ip = input("Enter IP to scan: ")
    scan_ports(target_ip, int(input("Enter Start Port: ")), int(input("Enter End Port: ")))

