import shutil

def get_disk_usega(path='/'):
    total, used, free = shutil.disk_usage(path)

    to_gb = 2**32
    return {
        "total": total / to_gb,
        "used": used / to_gb,
        "free": free / to_gb,
        "percent_used": (used / total) * 100
    }
