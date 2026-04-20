import psutil
from background_task import background
from django.core.cache import cache

@background(schedule=1)
def check_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    
    cache.set('current_cpu_load', cpu_percent, timeout=60)
    print(f"CPU Load: {cpu_percent}%")