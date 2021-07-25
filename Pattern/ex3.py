# write program to print patterns as per the picture given in below url. 
# develop separate program for each pattern 
# https://i1.faceprep.in/fp/articles/img/46684_1580817324.png

# # 3rd one hollow Inverted Half Pyramid

# 	1	2	3	4	5
# 5	*	*	*	*	*
# 4	*			*	
# 3	*		*		
# 2	*	*			
# 1	*				


row=0
col=0

for row in range(5,0,-1):
    for col in range(row,0,-1):
        if row==4 and col==2:
            print(" ",end=" ")
        elif row==4 and col==3:
            print(" ",end=" ")
        elif row==3 and col==2:
            print(" ",end=" ")
        else:     
            print("*",end=" ")
    print()