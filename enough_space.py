def enough(cap, on, wait):
    if on+wait<=cap:
        return 0
    else:
        return on+wait-cap

enough(100, 60, 50)