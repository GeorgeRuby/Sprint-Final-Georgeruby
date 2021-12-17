# Purpose - To write a program for One Stop Insurance company that calculates,
#           stores, invoices, and reports policy information for its customers.
# Author - George Ruby
# Date - Nov 26th, 2021
import datetime
def calcForDoll(forDoll):
    forDollStr = "${:,.2f}".format(forDoll)
    forDollPad = "{:>11}".format(forDollStr)

    return forDollPad


f = open("OSICDef.dat", "r")
POL_NUM = int(f.readline())
BASIC_RATE = float(f.readline())
ADD_CAR_DIS = float(f.readline())
EXT_LIA = float(f.readline())
GLASS_COV = float(f.readline())
LOANER_CAR = float(f.readline())
HST_RATE = float(f.readline())
PROC_FEE = float(f.readline())

# Inputs
def Name_Validation(Name):
    """ Function to Validate a Name for Input: Allowing Spaces, - and '"""
    for Char in Name:
        if ("A" <= Char <= "Z" or "a" <= Char <= "z" or Char == " "
                or Char == "-" or Char == "'"):
            continue
        else:
            return False
    return True
while True:
    while True:
        custFirstName = input("Enter the customers first name: ").title()
        if custFirstName == "":
            print("Customer first name cannot be blank")
        else:
            break
    while True:
        custLastName = input("Enter the customers last name: ").title()
        if custLastName == "":
            print("Customer last name cannot be blank")
        else:
            break

    stAdd = input("Enter the customers street address: ")
    city = input("Enter the customers city: ")

    while True:
        allowedChar = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
        prov = input("Enter the customers province(XX): ").upper()
        if len(prov) != 2 or set(prov[0]).issubset(allowedChar) == False or set(prov[1]).issubset(allowedChar) == False:
            print("invalid entry - province must be in the format (XX)")
        else:
            break

    while True:
        allowedChar = set("ABCDEFGHIJKLMONPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
        allowedNum = set("1234567890")

        postal = input("Postal Code (A1A1A1): ").upper()

        if set(postal[0]).issubset(allowedChar) == False or set(postal[1]).issubset(
                allowedNum) == False or set(postal[2]).issubset(allowedChar) == False or set(
                postal[3]).issubset(allowedNum) == False or set(postal[4]).issubset(
                allowedChar) == False or set(postal[5]).issubset(allowedNum) == False:
            print("Invalid entry - Postal code must be in the format (A1A1A1)")
        else:
            cust_postal = postal[0:3] + " " + postal[3:6]
            cust_postal = cust_postal.upper()
            break

    while True:

        phoneNum = input("Enter the customer phone number (##########): ")

        if phoneNum == "" or len(phoneNum) != 10 or phoneNum.isdigit() == False:
            print("invalid entry - phone number cannot be blank and must be in the format (##########)")
        else:
            phoneNum = "(" + phoneNum[0:3] + ")" + phoneNum[3:6] + "-" + phoneNum[6:10]
            break

    while True:
        polDateStr = input("Enter the policy date (YYYY-MM-DD): ")

        if polDateStr[0:4].isdigit() == True and polDateStr[5:7].isdigit() == True \
                and polDateStr[8:10].isdigit() == True and polDateStr[4] == "-" and \
                polDateStr[7] == "-" and polDateStr != "":
            break
        else:
            print("Policy date must be in the format (YYYY-MM-DD)")
    polDateObj = datetime.datetime.strptime(polDateStr, "%Y-%m-%d")
    polDateObjMon = polDateObj.day
    print(polDateObjMon)
    while True:
        firstPaymentDate = input("Is the policy date after the 25th of the month(Y/N):").upper()
        if firstPaymentDate == "Y":
            firstPaymentDate = polDateObj + datetime.timedelta(days=30)
        elif firstPaymentDate == "N":
            firstPaymentDate = polDateObj + datetime.timedelta(days=5)
        else:
            print("Invalid entry - must be a Y or an N")
        break
    polDate = polDateObj.strftime("%Y-%b-%d")

    firstPaymentDateStr = firstPaymentDate.strftime("%Y-%b-%d")

    numCarsIns = int(input("Enter the number of cars insured: "))

    extraLia = input("Does the customer want extra liability(Y/N): ").upper()

    while True:
        if extraLia == "Y":
            extraLia = EXT_LIA * numCarsIns
        elif extraLia == "N":
            extraLia = 0
        else:
            break
    glassCov = input("Does the customer want glass coverage(Y/N): ").upper()
    while True:
        if glassCov == "Y":
            glassCov = GLASS_COV * numCarsIns
        elif glassCov == "N":
            glassCov = 0
        else:
            break

    loanerCar = input("Does the customer want a loaner car(Y/N): ").upper()

    while True:
        if loanerCar == "Y":
            loanerCar = LOANER_CAR * numCarsIns
        elif loanerCar == "N":
            loanerCar = 0
        else:
            break

    payType = input("Does the customer want to pay in full or monthly(F/M): ")

    # Calculations
    while True:
        insPrem = 0
        if numCarsIns == 1:
            insPrem = BASIC_RATE
        elif numCarsIns > 1:
            insPrem = BASIC_RATE + (BASIC_RATE - (BASIC_RATE * ADD_CAR_DIS)) * (numCarsIns - 1)
        else:
            break

        totalExtraCost = extraLia + glassCov + loanerCar

        totalInsPrem = totalExtraCost + insPrem

        hst = totalInsPrem * HST_RATE

        totalCost = totalInsPrem + hst

        monPay = (totalCost + PROC_FEE) / 12

        #Outputs

        print()
        print("       ONE STOP INSURANCE COMPANY")
        print("             POLICY INVOICE")
        print("="*40)
        print("Customer  ")
        print(f"Details: {custFirstName} {custLastName}")
        print(f"         PH#-{phoneNum}")
        print(f"         {stAdd}")
        print(f"         {city} {prov + ','} {postal}")
        print("="*40)
        print(f"Policy Number: {str(POL_NUM) + custFirstName[0] + custLastName[0]}")
        print(f"Policy Date:   {polDate}")
        print(f"Payment Date:  {firstPaymentDateStr}")
        print("="*40)
        print(f"Extra Liability:             {calcForDoll(extraLia)}")
        print(f"Glass Coverage:              {calcForDoll(glassCov)}")
        print(f"Loaner Car:                  {calcForDoll(loanerCar)}")
        print(" "*30, "-"*9)
        print(f"Insurance Premium:           {calcForDoll(insPrem)}")
        print(f"Total Extra Costs:           {calcForDoll(totalExtraCost)}")
        print(f"Total Insurance Premium:     {calcForDoll(totalInsPrem)}")
        print(" "* 30, "-" * 9)
        print(f"HST:                         {calcForDoll(hst)}")
        print(f"Total Cost:                  {calcForDoll(totalCost)}")
        print(" " * 30, "-" * 9)
        print(f"Monthly Payments:            {calcForDoll(monPay)}")
        print()

        f = open("Policies.dat", "a")
        f.write("{}, ".format(str(POL_NUM)))
        f.write("{}, ".format(str(custFirstName)))
        f.write("{}, ".format(str(custLastName)))
        f.write("{}, ".format(str(stAdd)))
        f.write("{}, ".format(str(city)))
        f.write("{}, ".format(str(prov)))
        f.write("{}, ".format(str(postal)))
        f.write("{}, ".format(str(phoneNum)))
        f.write("{}, ".format(str(numCarsIns)))
        f.write("{}, ".format(str(insPrem)))
        f.write("{}, ".format(str(totalInsPrem)))
        f.write("{}, ".format(str(totalExtraCost)))
        f.write("{}, ".format(str(extraLia)))
        f.write("{}, ".format(str(glassCov)))
        f.write("{}, ".format(str(loanerCar)))
        f.write("{}, ".format(str(payType)))
        f.write("{}, ".format(str(hst)))
        f.write("{}, ".format(str(monPay)))
        f.write("{}\n".format(str(totalCost)))
        f.close()
        POL_NUM += 1

        f = open("OSICDef.dat", "w")
        f.write("{}\n".format(str(POL_NUM)))
        f.write("{}\n".format(str(BASIC_RATE)))
        f.write("{}\n".format(str(ADD_CAR_DIS)))
        f.write("{}\n".format(str(EXT_LIA)))
        f.write("{}\n".format(str(GLASS_COV)))
        f.write("{}\n".format(str(LOANER_CAR)))
        f.write("{}\n".format(str(HST_RATE)))
        f.write("{}\n".format(str(PROC_FEE)))
        f.close()
        break

    cont = input("Do you wish to make another entry(Y/N): ").upper()
    if cont == "N":
        print("Policy processed and saved")
    break

# Purpose - To create a detailed report for all of the policy listings
# Author - George Ruby
# Date - Nov 27th, 2021

def calcForDoll(forDoll):
    forDollStr = "${:,.2f}".format(forDoll)
    forDollPad = "{:>11}".format(forDollStr)

    return forDollPad


print()
print("                        ONE STOP INSURANCE COMPANY")
print("                          DETAILED POLICY REPORT")
print()
print("POLICY    CUSTOMER                          INSURANCE       EXTRA        TOTAL")
print("NUMBER      NAME                             PREMIUM        COSTS       PREMIUM")
print("="*80)

POL_NUMAcc = 0
insPremAcc = 0
totalExtraCostAcc = 0
totalInsPremAcc = 0

f = open("Policies.dat", "r")

for CustLine in f:
    CustData = CustLine.split(",")
    POL_NUM = CustData[0].strip()
    custFirstName = CustData[1].strip()
    custLastName = CustData[2].strip()
    stAdd = CustData[3].strip()
    city = CustData[4].strip()
    prov = CustData[5].strip()
    postal = CustData[6].strip()
    phoneNum = CustData[7].strip()
    numCarsIns = int(CustData[8].strip())
    insPrem = float(CustData[9].strip())
    totalInsPrem = float(CustData[10].strip())
    totalExtraCost = float(CustData[11].strip())
    extraLia = float(CustData[12].strip())
    glassCov = float(CustData[13].strip())
    loanerCar = float(CustData[14].strip())
    payType = CustData[15].strip()
    hst = float(CustData[16].strip())
    monPay = float(CustData[17].strip())
    totalCost = float(CustData[18].strip())

    print(f"{POL_NUM}     {custFirstName + ' ' +custLastName:24}         {calcForDoll(insPrem)}  {calcForDoll(totalExtraCost)}   {calcForDoll(totalInsPrem)}")

    POL_NUMAcc += 1
    insPremAcc += insPrem
    totalExtraCostAcc += totalExtraCost
    totalInsPremAcc += totalInsPrem

f.close()

print("="*80)
print(f"Policies Listed: {POL_NUMAcc:<4}                     {calcForDoll(insPremAcc)}  {calcForDoll(totalExtraCostAcc)}   {calcForDoll(totalInsPremAcc)}")
print()
print("End of detailed policy listing")

# Purpose - To create an exception report for the monthly payment listings
# Author - George Ruby
# Date - Nov 27th, 2021
import datetime
curDate = datetime.datetime.now()

def calcForDoll(forDoll):
    forDollStr = "${:,.2f}".format(forDoll)
    forDollPad = "{:>11}".format(forDollStr)

    return forDollPad

print()
print("                        ONE STOP INSURANCE COMPANY")
print(f"                 MONTHLY PAYMENT LISTINGS AS OF: {curDate:%d-%b-%y}")
print()
print("POLICY    CUSTOMER                   TOTAL                   TOTAL       MONTHLY")
print("NUMBER      NAME                    PREMIUM        HST       COSTS       PAYMENT")
print("="*80)

POL_NUMAcc = 0
totalInsPremAcc = 0
hstAcc = 0
totalCostAcc = 0
monPayAcc = 0

f = open("Policies.dat", "r")

for CustLine in f:
    CustData = CustLine.split(",")
    POL_NUM = CustData[0].strip()
    custFirstName = CustData[1].strip()
    custLastName = CustData[2].strip()
    stAdd = CustData[3].strip()
    city = CustData[4].strip()
    prov = CustData[5].strip()
    postal = CustData[6].strip()
    phoneNum = CustData[7].strip()
    numCarsIns = int(CustData[8].strip())
    insPrem = float(CustData[9].strip())
    totalInsPrem = float(CustData[10].strip())
    totalExtraCost = float(CustData[11].strip())
    extraLia = float(CustData[12].strip())
    glassCov = float(CustData[13].strip())
    loanerCar = float(CustData[14].strip())
    payType = CustData[15].strip()
    hst = float(CustData[16].strip())
    monPay = float(CustData[17].strip())
    totalCost = float(CustData[18].strip())

    if payType == "m":
        print(f"{POL_NUM}     {custFirstName + ' ' + custLastName:<24}{calcForDoll(totalInsPrem)} {calcForDoll(hst)} {calcForDoll(totalCost)} {calcForDoll(monPay)}")
        POL_NUMAcc += 1

    totalInsPremAcc += totalInsPrem
    hstAcc += hst
    totalCostAcc += totalCost
    monPayAcc += monPay

f.close()

print("="*80)
print(f"Total policies: {POL_NUMAcc:<4}             {calcForDoll(totalInsPremAcc)} {calcForDoll(hstAcc)} {calcForDoll(totalCostAcc)} {calcForDoll(monPayAcc)}")
print()
print("End of monthly payment listings")
