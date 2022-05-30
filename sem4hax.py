import os
course = None
subtopic = None
hax = None

# BELOW ARE GLOBAL FUNCTIONS FOR GENERAL USE OF ALL FUNCTIONS

def printString(size, char):
    output = ""
    for a in range (0, size):
        output += str(char)
    print(output)

def promptContinue():
    option = input("\n\nContinue? (Y/n): ")

    if(option.lower() == "n"):
        return False
    elif(option.lower() == "y"):
        return True

# BELOW ARE FUNCTIONS FOR MAIN MENU/MAIN PAGE

def start():
    mainMenu()

def mainMenu():
    while(True):
        os.system("cls")
        print("Welcome to Jesussy Hax Your Homework~")
        print("-------------------------------------------------------")
        print("Courses: ")
        print("1 -- DCS1104")
        print("2 -- TBA")
        print("X -- Exit Program\n")
        option = input("Please enter an option: ")

        if(option == "1"):
            editBreadcrumbs("course", "DCS1104")
            DCS1104Menu()
        elif(option == "X"):
            os.system("cls")
            break

# BELOW ARE FUNCTIONS FOR BREADCRUMBS (NAVIGATION PATH)

def displayBreadcrumbs():
    global course
    global subtopic
    global hax
    breadcrumb = ""
    if(course is not None):
        breadcrumb += ("Pages -> " + course)
        if(subtopic is not None):
            breadcrumb = breadcrumb + " > " + subtopic
            if(hax is not None):
                breadcrumb = breadcrumb + " > " + hax
    print(breadcrumb)

def editBreadcrumbs(level, value):
    global course
    global subtopic
    global hax
    if(level == "course"):
        course = value
    elif(level == "subtopic"):
        subtopic = value
    elif(level == "hax"):
        hax = value
            

# BELOW ARE FUNCTIONS FOR MENU FOR DCS1104 (STATISTICS AND DATA ANALYTICS)

def DCS1104Menu():
    while(True):
        os.system("cls")
        print("Welcome to Jesussy Hax Your Homework~")
        displayBreadcrumbs()
        print("-------------------------------------------------------")
        print("Subtopic: ")
        print("1 -- Descriptive Statistics:")
        print("\t > Includes frequency, mean, median, mean absolute deviation etc.\n")
        print("2 -- Distance Measures:")
        print("\t > Includes pixel image, Hamming distance, bag of words etc.\n")
        print("X -- Back to previous menu\n")
        option = input("Please enter an option: ")

        if(option == "1"):
            editBreadcrumbs("subtopic", "Descriptive Statistics")
            descriptiveStatisticsMenu()
        elif(option == "2"):
            editBreadcrumbs("subtopic", "Distance Measures")
            distanceMeasuresMenu()
        elif(option == "X"):
            break

# BELOW ARE FUNCTIONS FOR MENU FOR UNIVARIATE ABSOLUTE AND RELATIVE FREQUENCY (SUBMENU UNDER DCS1104)

def descriptiveStatisticsMenu():
    while(True):
        os.system("cls")
        print("Welcome to Jesussy Hax Your Homework~")
        displayBreadcrumbs()
        print("-------------------------------------------------------")
        print("Hax: ")
        print("1 -- Univariate Absolute and Relative Frequency")
        print("\t > Absolute (cumulative) frequency, relative (cumulative) frequency\n")
        print("2 -- Location Univariate Statistics")
        print("\t > Mean, median, mean absolute deviation\n")
        print("X -- Back to previous menu\n")
        option = input("Please enter an option: ")
        
        if(option == "1"):
            editBreadcrumbs("hax", "Univariate Absolute and Relative Frequency")
            univariateFrequency()
        elif(option == "2"):
            editBreadcrumbs("hax", "Location Univariate Statistics")
            locationUniStats()
        elif(option == "X"):
            break

# BELOW ARE FUNCTIONS FOR UNIVARIATE FREQUENCY

def univariateFrequency():
    while(True):
        os.system("cls")
        print("Welcome to Jesussy Hax Your Homework~")
        displayBreadcrumbs()
        print("-------------------------------------------------------")

        colName = input("Enter the name of the column: ")
        n = int(input("Number of rows: "))
        
        absCumFreq = 0
        relCumFreq = 0
        tableArr = [[],[],[],[],[]]
        tempArr = []

        for count in range(0, n):
            if(count != n-1):
                listVal = input("Row #" + str(count + 1) + ": ")    
            else:
                listVal = input("Row #" + str(count + 1) + " (END): ")
            
            tempArr.append(float(listVal))

        tempArr.sort()

        for a in range (0, len(tempArr)):
            if(tempArr[a] not in tableArr[0]):
                tableArr[0].append(tempArr[a])
        
        for b in range (0, len(tableArr[0])):
            absFreq = tempArr.count(tableArr[0][b])
            relFreq = round(absFreq/n*100, 3)
            absCumFreq += absFreq
            relCumFreq = round(absCumFreq/n*100, 3)
            tableArr[1].append(absFreq)
            tableArr[2].append(str(relFreq) + "%")
            tableArr[3].append(absCumFreq)
            tableArr[4].append(str(relCumFreq) + "%")

        formatStr = "| {:^10} | {:^20} | {:^20} | {:^30} | {:^30} |"
        string = formatStr.format(colName, "Absolute Frequency", "Relative Frequency", "Absolute Cumulative Frequency", "Relative Cumulative Frequency")
        printString(len(string), "-")
        print(string)
        
        for c in range (0, len(tableArr[0])):
            string = formatStr.format(tableArr[0][c], tableArr[1][c], tableArr[2][c], tableArr[3][c], tableArr[4][c])
            printString(len(string), "-")
            print(string)
        
        printString(len(string), "-")
        
        if(promptContinue()):
            continue
        else:
            break

# BELOW ARE FUNCTIONS FOR LOCATION UNIVARIATE STATISTICS

def locationUniStats():
    import math
    while(True):
        os.system("cls")
        print("Welcome to Jesussy Hax Your Homework~")
        displayBreadcrumbs()
        print("-------------------------------------------------------")
        n = int(input("Number of rows: "))
        numArr = []

        arrTotal = 0
        madTotal = 0
        stdTotal = 0

        for count in range(0, n):
            if(count != n-1):
                listVal = input("Row #" + str(count + 1) + ": ")    
            else:
                listVal = input("Row #" + str(count + 1) + " (END): ")
            
            numArr.append(float(listVal))

        numArr.sort()

        for a in range(0, n):
            arrTotal += numArr[a]

        minVal = numArr[0]
        maxVal = numArr[n-1]
        meanVal = arrTotal/n
        modeVal = max(set(numArr), key = numArr.count)

        q1pos = (n+1)/4
        medianPos = (n+1)/2
        q3pos = (n+1) * 3/4

        def calcQuartile(pos):
            if(isinstance(pos, int)):
                val = numArr[pos - 1]
            else:
                if(pos > 1):
                    val = numArr[math.floor(pos)-1] + (((pos - math.floor(pos)) * (numArr[math.floor(pos)] - numArr[math.floor(pos)-1])))
                else:
                    val = (pos - math.floor(pos)) * numArr[math.floor(pos)]
            return val

        q1Val = calcQuartile(q1pos)
        medianVal = calcQuartile(medianPos)
        q3Val = calcQuartile(q3pos)

        for a in range(0, n):
            madTemp = abs(numArr[a] - meanVal)
            madTotal = madTotal + madTemp
            
            stdTemp = abs(numArr[a] - meanVal) ** 2
            stdTotal = stdTotal + stdTemp

        amplitudeVal = maxVal - minVal
        IQRVal = q3Val - q1Val
        madVal = round(madTotal/(n - 1), 2)
        stdVal = round(math.sqrt(stdTotal/(n-1)), 2)

        def removeFloatingPoint(value):
            if(value == math.floor(value)):
                return str(int(value))
            else:
                return str(value)

        print("\nMinimum: " + removeFloatingPoint(minVal))
        print("Maximum: " + removeFloatingPoint(maxVal))
        print("Mean/Average: " + removeFloatingPoint(meanVal))
        print("Mode: " + removeFloatingPoint(modeVal) + "\n")
        print("1st Quartile Position: " + removeFloatingPoint(q1pos))
        print("Median Position: " + removeFloatingPoint(medianPos))
        print("3rd Quartile Position: " + removeFloatingPoint(q3pos) + "\n")
        print("1st Quartile: " + removeFloatingPoint(q1Val))
        print("Median: " + removeFloatingPoint(medianVal))
        print("3rd Quartile: " + removeFloatingPoint(q3Val) + "\n")

        print("Amplitude: " + removeFloatingPoint(amplitudeVal))
        print("Interquartile Range: " + removeFloatingPoint(IQRVal))
        print("MAD: " + removeFloatingPoint(madVal))
        print("Standard Deviation: " + removeFloatingPoint(stdVal))

        if(promptContinue()):
            continue
        else:
            break
        
# BELOW ARE FUNCTIONS FOR MENU FOR DISTANCE MEASURES (SUBMENU UNDER DCS1104)

def distanceMeasuresMenu():
    while(True):
        os.system("cls")
        print("Welcome to Jesussy Hax Your Homework~")
        displayBreadcrumbs()
        print("-------------------------------------------------------")
        print("Hax: ")
        print("1 -- Pixel Image Distance (Pixel Matrix, Vector)")
        print("\t > Input matrix of pixels to get pixel distance and vector\n")
        print("2 -- Bag of Words")
        print("\t > Input two sentences to get distance between them\n")
        print("3 -- Hamming Distance")
        print("\t > Input two words of the same length to get distance between them\n")
        print("4 -- Edit Distance")
        print("\t > Input two words of different length to get distance between them\n")
        print("X -- Back to previous menu\n")
        option = input("Please enter an option: ")
        
        if(option == "1"):
            editBreadcrumbs("hax", "Pixel Image Distance")
            pixelImage()
        elif(option == "2"):
            editBreadcrumbs("hax", "Bag of Words")
            bagOfWords()
        elif(option == "3"):
            editBreadcrumbs("hax", "Hamming Distance")
            hammingDistance()
        elif(option == "4"):
            editBreadcrumbs("hax", "Edit Distance")
            editDistance()
        elif(option == "X"):
            break

# BELOW ARE FUNCTIONS FOR PIXEL IMAGE DISTANCE CALCULATION

def pixelImage():
    while(True):
        os.system("cls")
        print("Welcome to Jesussy Hax Your Homework~")
        displayBreadcrumbs()
        print("-------------------------------------------------------")
        xlen = int(input("Please input horizontal length of pixel image: "))
        ylen = int(input("Please input vertical length of pixel image: "))

        print("Please input 1 for filled pixel and 0 for empty pixel.\n---------------------------------\n")

        pixelImg1 = []
        pixelImg2 = []
        difference = 0

        for count in range (0, 2):
            print("Please enter pixel image " + str(count+1))
            for y in range (0, ylen):
                row = input()
                if(len(row) == xlen):
                    if(count == 0):
                        pixelImg1.append(list(row))
                    elif(count == 1):
                        pixelImg2.append(list(row))
                else:
                    print("Failed.")
                    break


        for y in range (0, ylen):
            for x in range(0, xlen):
                if(pixelImg1[y][x] != pixelImg2[y][x]):
                    difference += 1

        print("Difference: " + str(difference))

        if(promptContinue()):
            continue
        else:
            break

# BELOW ARE FUNCTIONS FOR BAG OF WORDS

def bagOfWords():
    while(True):
        os.system("cls")
        print("Welcome to Jesussy Hax Your Homework~")
        displayBreadcrumbs()
        print("-------------------------------------------------------")
        punctuation = ["?", ",", "!", "."]
        valueA = ["A"]
        valueB = ["B"]
        bagOfWords = [""]

        sentence1 = input("Please enter sentence 1: ")
        sentence2 = input("Please enter sentence 2: ")

        print("A = " + sentence1)
        print("B = " + sentence2)

        for x in range (0, len(punctuation)):
            sentence1 = sentence1.replace(punctuation[x], "")
            sentence2 = sentence2.replace(punctuation[x], "")

        sentence1 = sentence1.split(" ")
        sentence2 = sentence2.split(" ")

        for a in range (0, len(sentence1)):
            sentence1[a] = sentence1[a].lower()
            if(sentence1[a] not in bagOfWords):
                bagOfWords.append(sentence1[a])
            
        for b in range (0, len(sentence2)):
            sentence2[b] = sentence2[b].lower()
            if(sentence2[b] not in bagOfWords):
                bagOfWords.append(sentence2[b])

        for c in range (1, len(bagOfWords)):
            valueA.append(sentence1.count(bagOfWords[c]))
            valueB.append(sentence2.count(bagOfWords[c]))

        table = [bagOfWords, valueA, valueB]
        formatStr = "{:^2}"
        print("\n")

        for e in range (0, 3):
            string = ""
            formatStr = "| {:^3} |"
            string += formatStr.format(table[e][0])
            for d in range (1, len(bagOfWords)):
                formatStr = " {:^" + str(len(table[0][d]) + 2) + "} |"
                string += formatStr.format(table[e][d])
            printString(len(string), "-")
            print(string)
        
        printString(len(string), "-")
        
        if(promptContinue()):
            continue
        else:
            break

# BELOW ARE FUNCTIONS FOR HAMMING DISTANCE

def hammingDistance():
    while(True):
        os.system("cls")
        print("Welcome to Jesussy Hax Your Homework~")
        displayBreadcrumbs()
        print("-------------------------------------------------------")
        distance = 0

        word1 = input("Please enter word 1: ")
        word2 = input("Please enter word 2: ")

        if(len(word1) != len(word2)):
            print("\nPlease enter valid words that have the same character count.")
        else:
            for a in range (0, 3):
                formatStr = "| {:^8} |"
                if(a != 2):
                    string = ""
                    string += formatStr.format(("Word " + str(a+1)))
                    for b in range (0, len(word1)):
                        formatStr = " {:^3} |"
                        if(a == 0):
                            string += (formatStr.format(word1[b]))
                        else:
                            string += (formatStr.format(word2[b]))
                else:
                    string = ""
                    string += formatStr.format("Distance")
                    for b in range (0, len(word1)):
                        formatStr = " {:^3} |"
                        if(word1[b] != word2[b]):
                            string += (formatStr.format("1"))
                            distance += 1
                        else:
                            string += (formatStr.format("0"))
            
                printString(len(string), "-")
                print(string)

            
            printString(len(string), "-")
            print("\nTotal Hamming Distance: " + str(distance))

            if(promptContinue()):
                continue
            else:
                break

        
# BELOW ARE FUNCTIONS FOR EDIT DISTANCE

def editDistance():
    while(True):
        os.system("cls")
        print("Welcome to Jesussy Hax Your Homework~")
        displayBreadcrumbs()
        print("-------------------------------------------------------")
        distance = 0

        word1 = input("Please enter word 1: ")
        word2 = input("Please enter word 2: ")

        if(len(word1) == len(word2)):
            print("\nPlease enter valid words that have a different character count.")
            break
        else:
            if(len(word1) > len(word2)):
                while(len(word1) > len(word2)):
                    word2 += " "
            else:
                while(len(word2) > len(word1)):
                    word1 += " "

                for a in range (0, 3):
                    formatStr = "| {:^15} |"
                    if(a != 2):
                        string = ""
                        string += formatStr.format(("Word " + str(a+1)))
                        for b in range (0, len(word1)):
                            formatStr = " {:^3} |"
                            if(a == 0):
                                string += (formatStr.format(word1[b]))
                            else:
                                string += (formatStr.format(word2[b]))
                    else:
                        string = ""
                        string += formatStr.format("Distance")
                        for b in range (0, len(word1)):
                            formatStr = " {:^3} |"
                            if(word1[b] != word2[b]):
                                string += (formatStr.format("1"))
                                distance += 1
                            else:
                                string += (formatStr.format("0"))
                
                    printString(len(string), "-")
                    print(string)

                
                printString(len(string), "-")
                print("\nTotal Hamming Distance: " + str(distance))

                if(promptContinue()):
                    continue
                else:
                    break

start()