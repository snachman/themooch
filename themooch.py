def scaramuccis(first, second, roundto=100):
    diff = (second - first)
    seconds = diff.total_seconds()
    minutes = seconds / 60
    hours = minutes / 60
    days = hours / 24
    scaramuccis = days/11
    return round(scaramuccis, roundto)
