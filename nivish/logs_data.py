

def logsFun(station_logs,station_data):
    
    for key1, value1 in station_data.__dict__.items():
        if key1 != 'id' and key1 in station_logs.__dict__:
            setattr(station_logs, key1, value1)
    station_logs.save()
    return "Logs Saved"
