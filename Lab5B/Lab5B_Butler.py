
# Disclaimer for approximation
print("DISCLAIMER: All calculations are approximated as points are approximated from stress diagram.")
# Input Variable needed:
strainValue = float(input("Please enter your stress value from 0 - 0.30: "))  #(this will be from 0.0 – 0.30)

## Additional Variables:
# Input point values: These values are estimated based on the graph in handout
Oo = 0  # (x and y values of O are the same, removed one for redundancy)
Ay = 42
Ax = 0.01
Cy = 43
Cx = 0.06
Dy = 60
Dx = 0.18
Ey = 50
Ex = 0.26

# Booleans: (will not be indented in code, just for clarification of PDF)
isElastic = (Oo <= strainValue < Ax)
isPlastic = (Ax <= strainValue < Cx)
isHardening = (Cx <= strainValue < Dx)
isNecking = (Dx <= strainValue < Ex)
isBroke = (strainValue >= Ex)

# Calculate slopes:
slopeOA = (Ay - Oo) / (Ax - Oo)
slopeAC = (Cy - Ay) / (Cx - Ax)
slopeCD = (Dy - Cy) / (Dx - Cx)
slopeDE = (Ey - Dy) / (Ex - Dx)

# if statements will run function based on stress input
# function based on y = m (x - x(1)) + y(1)
# function will equal the Stress output
if isElastic:
    functionOA = slopeOA * (strainValue - Oo) + Oo
    print("The modulus of elasticity (Young's Modulus) is the relationship between stress and strain for a bar in"
          " simple tension/compression. It is represented as the linear portion of the graph.")
    print("The Stress (KSI) is %0.1f." % functionOA)
elif isPlastic:
    functionAC = slopeAC * (strainValue - Ax) + Ay
    print("The stress (KSI) is %0.1f." % functionAC)
elif isHardening:
    functionCD = slopeCD * (strainValue - Cx) + Cy
    print("The stress (KSI) is %0.1f." % functionCD)
elif isNecking:
    functionDE = slopeDE * (strainValue - Dx) + Dy
    print("The stress (KSI) is %0.1f." % functionDE)
elif isBroke:
    print("The iron broke when the stress reached 0.26 as it approached a stress of 50ksi!")
else:
    print("That value is not within the parameters of strain!")
