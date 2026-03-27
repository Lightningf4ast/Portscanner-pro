COMMON = {
    21: "FTP",
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP-ALT"
}

def get_service(port):
    return COMMON.get(port, "Unknown")
