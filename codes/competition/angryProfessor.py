# def lateOrNot(n, k):
#     pass
s = '04:59:59AM'
hr = int(s[:2])
minutes = s[3:5]
seconds = s[6:8]
hrClock = s[8:]
print(hr, minutes, seconds, hrClock)
if hrClock.upper() == "PM":
    if hr != 12:
        hr += 12
else:
    if hr != 12:
        if hr < 10:
            hr = f"0{hr}"

milTime = f"{hr}:{minutes}:{seconds}"
print(milTime)