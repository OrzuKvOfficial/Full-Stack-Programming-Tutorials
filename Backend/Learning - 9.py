import psutil

def check_connected_devices():
    devices = psutil.disk_partitions()
    for device in devices:
        print(f"Device: {device.device}, Mountpoint: {device.mountpoint}")

check_connected_devices()
