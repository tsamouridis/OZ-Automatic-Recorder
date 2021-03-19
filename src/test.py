# def setEnd(day,startH, startMin, durH, durMin):
#         """
#         setEnd method

#         Sets the time the Recording schould be stopped
#         """
#         endH = 0
#         endMin = 0
#         borrow = 0
#         if startMin + durMin >= 60:
#             borrow +=1
#             endMin = (startMin+durMin)-60
#         else:
#             endMin = startMin+durMin
#         endH = startH + durH + borrow

#         if endH == 24 and borrow == 1:
#             endH=1
#             if borrow == 1:
#                 day+=1
#         if endH == 25:
#             endH = 1
#         return [day, endH, endMin]

def setEnd(day, startH, startMin, durH, durMin):
        """
        setEnd method

        Sets the time the Recording schould be stopped
        """
        endH = 0
        endMin = 0
        borrow = 0
        if startMin + durMin >= 60:
            borrow +=1
            endMin = (startMin+durMin)-60
        else:
            endMin = startMin+durMin
        endH = startH + durH + borrow
        if endH == 24:
            endH = 0
        elif endH >= 25:
            endH = endH-24
        if endH<startH:
            day+=1
        return [day,endH, endMin]

a = setEnd(1,21,59,4,1)
print(a)