def tstamp_to_id(tstamp):
    date, time = tstamp.split(" ")
    date = date.split("-")
    time = time.split(":")
    date.pop(0)
    date.extend(time)
    return "".join(date)


print(tstamp_to_id("10/2/2022 21:01:53"))
