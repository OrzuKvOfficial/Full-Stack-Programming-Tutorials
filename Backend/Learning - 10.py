import platform
import psutil

def get_system_info():
    info = {
        "Operatsion tizim": platform.system(),
        "Tizim versiyasi": platform.version(),
        "Arxitektura": platform.architecture()[0],
        "Protsessor": platform.processor(),
        "Jismoniy yadrolar": psutil.cpu_count(logical=False),
        "Umumiy yadrolar": psutil.cpu_count(logical=True),
        "RAM hajmi (GB)": round(psutil.virtual_memory().total / (1024**3), 2),
        "Disk hajmi (GB)": round(psutil.disk_usage('/').total / (1024**3), 2)
    }
    return info

if __name__ == "__main__":
    system_info = get_system_info()
    for key, value in system_info.items():
        print(f"{key}: {value}")
