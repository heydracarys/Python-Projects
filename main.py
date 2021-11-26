# Twenty random cards are placed in a row all face down. A turn consists of taking two adjacent cards where the left
# one is face up and the right one can be face up or face down and flipping them both. 
# Show that this process must terminate. (with all the cards facing up).


def turnOver(a):
    for i in range(len(a)-1):
      if  a[i]=='1':
            a[i]='0'
            if a[i+1]=='0':
                a[i+1]='1'        
            else:
                a[i+1]='0'

    return a
# 0 Denotes Card is facing up
# 1 Denotes Card is facing down
SOC=list("11111111111111111111")
print(SOC)
while (SOC!=turnOver(SOC.copy())):
    SOC=turnOver(SOC.copy())

print(SOC)




