# write program to print patterns as per the picture given in below url. 
# develop separate program for each pattern 
# https://i1.faceprep.in/fp/articles/img/46684_1580817324.png

# 1st one Half Pyramid

row=0
col=0

for row in range(0,5):
    for col in range(0,row+1):
        row+=1
        print("*",end=' ')
    print()
    