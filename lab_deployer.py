import subprocess
import platform
import datetime
import concurrent.futures

# Target lab terminals (Sample IP range)
TARGET_HOSTS = [f"192.168.1.{i}" for i in range(101, 170)]  # 69 Terminals

LOG_FILE = "deployment_audit_log.txt"

def check_host_status(ip):
    """Pings a terminal to verify Layer-3 network reachability."""
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", "-W", "1", ip] if param == "-c" else ["ping", param, "1", "-w", "1000", ip]
    
    try:
        output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return ip, (output.returncode == 0)
    except Exception:
        return ip, False

def log_event(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {message}"
    print(entry)
    with open(LOG_FILE, "a") as f:
        f.write(entry + "\n")

def run_lab_audit():
    log_event("Starting Multi-Terminal Lab Connectivity & Deployment Audit (69 Nodes)...")
    online_nodes = []
    offline_nodes = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        results = executor.map(check_host_status, TARGET_HOSTS)
        for ip, is_up in results:
            if is_up:
                online_nodes.append(ip)
                log_event(f"[ONLINE]  {ip} - Ready for automated package provisioning.")
            else:
                offline_nodes.append(ip)
                log_event(f"[OFFLINE] {ip} - Unreachable (Check Layer-1 cabling / NIC).")

    log_event(f"Audit Complete | Online: {len(online_nodes)} | Offline: {len(offline_nodes)}")

if __name__ == "__main__":
    run_lab_audit()
