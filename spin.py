spins = input("How many times did you spin? (Enter a negative number for counter-clockwise spins) ")

#TODO - Edit the degrees calculation here!
degrees = (float(spins) * 360) % 360 # see WB notes below
print("You are facing", degrees, "degrees relative to north")

# when I input 0.25, I should get "90.0 degrees relative to north". WB: 90 / 360 = 0.25, which leaves a remainder of .25 of 360 = 90
# when I input 1, I should get "0.0 degrees relative to north" (back where I started). WB: 360 / 360 = 1, which leaves 0 remainder.
# when I input -2, I should get "0.0 degrees relative to north" (again, back where I started). WB: -720 / 360 = -2, which leaves 0 remainder.
# when I input 1.5, I should get "180.0 degrees relative to north". WB: 540 / 360 = 1.5, which leaves a remainder of 0.5 of 360 = 180
