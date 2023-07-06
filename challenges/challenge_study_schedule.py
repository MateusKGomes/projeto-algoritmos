def study_schedule(permanence_period, target_time):
    best_period = 0
    if not isinstance(target_time, int):
        return None
    for period in permanence_period:
        if not isinstance(period[0], int) or not isinstance(period[1], int):
            return None
        if period[0] <= target_time <= period[1]:
            best_period += 1
    return best_period
