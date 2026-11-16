# Multi-Terminal Lab & Infrastructure Deployment Automator

A lightweight, multi-threaded Python automation utility designed to audit network reachability and streamline bulk software/environment provisioning across large-scale computer labs and server racks.

## Real-World Use Case
Built out of hands-on infrastructure deployment experience configuring offline Python and Machine Learning environments (OpenCV, TensorFlow, Scikit-learn, Pandas) across **69+ workstation terminals** simultaneously.

## Key Features
- **Concurrent Subnet Auditing:** Uses Python `ThreadPoolExecutor` to verify Layer-3 connectivity across dozens of nodes in seconds.
- **Layer-1/Layer-3 Diagnostics:** Flags unreachable terminals to isolate faulty Cat6 patch cables, switch port issues, or powered-off nodes before deployment.
- **Automated Audit Logging:** Generates timestamped deployment logs (`deployment_audit_log.txt`) for infrastructure compliance and troubleshooting.

## Tech Stack
- **Language:** Python 3.x (`subprocess`, `concurrent.futures`, `platform`)
- **Environment:** Linux CLI & Windows Enterprise Workstations
