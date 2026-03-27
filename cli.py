import asyncio
from core.scanner_async import scan_range
from core.service import get_service
from core.exporter import save_txt, save_json

ip = input("Target IP: ")
start = int(input("Start Port: "))
end = int(input("End Port: "))

ports = asyncio.run(scan_range(ip, start, end, 0.5))

results = []

for p in ports:
    service = get_service(p)
    print(f"[OPEN] {p} ({service})")

    results.append({
        "port": p,
        "service": service
    })

save_txt(results)
save_json(results)
