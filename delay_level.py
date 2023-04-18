def delay_level(delay_time):
    if delay_time == 0:
        return "no delay"
    elif delay_time <= 13:
        return "little delay"
    elif delay_time <= 15:
        return "delayed"
    else:
        return "very delayed"