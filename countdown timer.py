import time
print ("Want python to act as a countdown timer?")
print ("There you go!")
ask1 = int(input("Enter the time (in seconds) you want to countdown for: "))

for x in range (ask1,0,-1):
    seconds = int(x%60)
    minutes = int(x/60)%60
    hours = int(x/3600)
    print (f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep (1)

print ("TIME'S UP!!!!!!")

# for explanation
# FOR SECONDS: we know that normal division or "/" is used when we want to convert seconds -> minutes or minutes -> hours
# but here the mechanisms are different
# while converting seconds to minutes we have always seen the quotient and quotient always gives us minutes
# but it's reminder gives us seconds!
# FOR MINUTES: now if a user enters a value like 3,745:
# so in minutes line, we convert it into hours normal procedure and get the integer value
# but now if we get value like 62, a minute is not above than 60 so to get minute we divide it "modulussly"
# now we get 2 as reminder which are minutes
# FOR HOURS: simple division by 3,600 as we do
