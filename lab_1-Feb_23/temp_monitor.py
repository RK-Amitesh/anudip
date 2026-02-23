"""
Program: Temperature Monitoring System
---------------------------------
- Find hottest & coldest day
- Replace temps > 45 with 'Heat Alert'
- Count extreme days (>40)
"""

def monitor_temperature(temps):
    hottest = max(temps)
    coldest = min(temps)

    alerts = ["Heat Alert" if t > 45 else t for t in temps]
    extreme_days = len([t for t in temps if t > 40])

    return hottest, coldest, alerts, extreme_days


temperatures = [38, 42, 47, 35, 44, 50]

hottest, coldest, alert_list, extreme = monitor_temperature(temperatures)

print("Hottest:", hottest)
print("Coldest:", coldest)
print("Alerts:", alert_list)
print("Extreme Days:", extreme)