from array import *
import numpy
def O(i,j,val,blks,all_blks):
    if((val[i][j]==0)and(val[i][j+1]==0)and(val[i+1][j+1]==0)and(val[i+1][j]==0)):
        val[i][j]=1
        val[i][j+1]=1
        val[i+1][j+1]=1
        val[i+1][j]=1
        print(str(i)+"\t"+str(j))
        all_blks.remove('O')
        print("dd")
        if(((not(i==0))or(not(j==0)))):
             global blks
             blks.remove('O')
             #if(len(blks)==0):
                #blks=all_blks
                print(str(i)+"\t"+str(j))#all_blk_place(blks,i,j)
        #     else:    
         #       blk_place(blks,i,j)
        #else:    
         #       blk_place(blks,i,j)           
def I1(i,j,val,blks,all_blks):
    if((val[i][j]==0)and(val[i+1][j]==0)and(val[i+2][j]==0)and(val[i+3][j]==0)):
        val[i][j]=2
        val[i+1][j]=2
        val[i+2][j]=2
        val[i+3][j]=2
        all_blks.remove('I')
        if(((not(i==0))or(not(j==0)))):
            global blks
            blks.remove('I')
            #if(len(blks)==0):
                #blks=all_blks
                print("haaai")#all_blk_place(blks,i,j)
         #   else:    
         #       blk_place(blks,i,j)
        #else:    
          #      blk_place(blks,i,j)
def I2(i,j,val,blks,all_blks):
    if((val[i][j]==0)and(val[i][j+1]==0)and(val[i][j+2]==0)and(val[i][j+3]==0)):
        val[i][j]=2
        val[i][j+1]=2
        val[i][j+2]=2
        val[i][j+3]=2
        all_blks.remove('I')
        if(((not(i==0))or(not(j==0)))):
            global blks
            blks.remove('I')
            #if(len(blks)==0):
                #blks=all_blks
                print("haaai")#all_blk_place(blks,i,j)
           # else:    
            #    blk_place(blks,i,j)
        #else:    
             #   blk_place(blks,i,j)         
                  
def S1(i,j,val,blks,all_blks):
    if((val[i][j]==0)and(val[i][j+1]==0)and(val[i+1][j+1]==0)and(val[i+1][j+2]==0)):
        val[i][j]=3
        val[i][j+1]=3
        val[i+1][j+1]=3
        val[i+1][j+2]=3
        all_blks.remove('S')
        if(((not(i==0))or(not(j==0)))):
            global blks
            blks.remove('S')
            #if(len(blks)==0):
                #blks=all_blks
                print("haaai")#all_blk_place(blks,i,j)
        #    else:    
         #       blk_place(blks,i,j)
        #else:    
         #       blk_place(blks,i,j)
                  
def S2(i,j,val,blks,all_blks):
    if((val[i][j]==0)and(val[i-1][j]==0)and(val[i-1][j+1]==0)and(val[i-2][j+1]==0)):
        val[i][j]=3
        val[i-1][j]=3
        val[i-1][j+1]=3
        val[i-2][j+1]=3
        all_blks.remove('S')
        if(((not(i==0))or(not(j==0)))):
            global blks
            blks.remove('S')
            #if(len(blks)==0):
                #blks=all_blks
                print("haaai")#all_blk_place(blks,i,j)
        #    else:    
         #       blk_place(blks,i,j)
        #else:    
            #    blk_place(blks,i,j)           
                  
def Z1(i,j,val,blks,all_blks):
    if((val[i][j]==0)and(val[i][j-1]==0)and(val[i+1][j-1]==0)and(val[i+1][j-2]==0)):
        val[i][j]=4
        val[i][j-1]=4
        val[i+1][j-1]=4
        val[i+1][j-2]=4 
        all_blks.remove('Z')
        if(((not(i==0))or(not(j==7)))):
            global blks
            blks.remove('Z')
            #if(len(blks)==0):
                #blks=all_blks
                print("haaai")#all_blk_place(blks,i,j)
        #    else:    
          #      blk_place(blks,i,j)
        #else:    
           #     blk_place(blks,i,j)
def Z2(i,j,val,blks,all_blks):
    if((val[i][j]==0)and(val[i+1][j]==0)and(val[i+1][j+1]==0)and(val[i+2][j+1]==0)):
        val[i][j]=4
        val[i+1][j]=4
        val[i+1][j+1]=4
        val[i+2][j+1]=4
        all_blks.remove('Z')
        if(((not(i==0))or(not(j==7)))):
            global blks
            blks.remove('Z')
            #if(len(blks)==0):
                #blks=all_blks
                print("haaai")#all_blk_place(blks,i,j)
        #    else:    
         #       blk_place(blks,i,j)
        #else:    
         #       blk_place(blks,i,j)        
def L1(i,j,val,blks,all_blks):
    if((val[i][j]==0)and(val[i][j+1]==0)and(val[i+1][j]==0)and(val[i+2][j]==0)):
        val[i][j]=5
        val[i][j+1]=5
        val[i+1][j]=5
        val[i+2][j]=5    
        all_blks.remove('L')                                   
        if(((not(i==0))or(not(j==0)))):
            global blks
            blks.remove('L')
            #if(len(blks)==0):
                #blks=all_blks
                print("haaai")#all_blk_place(blks,i,j)
        #    else:    
         #       blk_place(blks,i,j)
        #else:    
         #       blk_place(blks,i,j)
                  
def L2(i,j,val,blks,all_blks):
    if((val[i][j]==0)and(val[i][j+1]==0)and(val[i][j+2]==0)and(val[i-1][j]==0)):
        val[i][j]=5
        val[i][j+1]=5
        val[i][j+2]=5
        val[i-1][j]=5    
        all_blks.remove('L')                                   
        if(((not(i==0))or(not(j==0)))):
            global blks
            blks.remove('L')
            #if(len(blks)==0):
                #blks=all_blks
                print("haaai")#all_blk_place(blks,i,j)
        #    else:    
         #       blk_place(blks,i,j)
        #else:    
         #       blk_place(blks,i,j)
                  
def L3(i,j,val,blks,all_blks):
    if((val[i][j]==0)and(val[i][j-1]==0)and(val[i-1][j]==0)and(val[i-2][j]==0)):
        val[i][j]=5
        val[i][j-1]=5
        val[i-1][j]=5
        val[i-2][j]=5 
        print("yyy")
        all_blks.remove('L')
        if(((not(i==0))or(not(j==0)))):
            global blks
            blks.remove('L')
            #if(len(blks)==0):
                #blks=all_blks
                print("haaai")#all_blk_place(blks,i,j)
         #   else:    
          #      blk_place(blks,i,j)
        #else:    
         #       blk_place(blks,i,j)
                  
def L4(i,j,val,blks,all_blks):
    if((val[i][j]==0)and(val[i+1][j]==0)and(val[i][j-1]==0)and(val[i][j-2]==0)):
        val[i][j]=5
        val[i+1][j]=5
        val[i][j-1]=5
        val[i][j-2]=5 
        all_blks.remove('L')
        if(((not(i==0))or(not(j==0)))):
            global blks
            blks.remove('L')
            #if(len(blks)==0):
                #blks=all_blks
                print("haaai")#all_blk_place(blks,i,j)
        #    else:    
         #       blk_place(blks,i,j)
        #else:    
         #       blk_place(blks,i,j)
                  
def J1(i,j,val,blks,all_blks):
    if((val[i][j]==0)and(val[i+1][j]==0)and(val[i+2][j]==0)and(val[i][j-1]==0)):
        val[i][j]=6
        val[i+1][j]=6
        val[i+2][j]=6
        val[i][j-1]=6 
        all_blks.remove('J')
        if(((not(i==0))or(not(j==7)))):
            global blks
            blks.remove('J')
            #if(len(blks)==0):
                #blks=all_blks
                print("haaai")#all_blk_place(blks,i,j)
            #else:    
             #   blk_place(blks,i,j)
        #else:    
         #       blk_place(blks,i,j)
                  
def J2(i,j,val,blks,all_blks):
    if((val[i][j]==0)and(val[i+1][j]==0)and(val[i][j+1]==0)and(val[i][j+2]==0)):
        val[i][j]=6
        val[i+1][j]=6
        val[i][j+1]=6
        val[i][j+2]=6 
        all_blks.remove('J')
        if(((not(i==0))or(not(j==7)))):
            global blks
            blks.remove('J')
            #if(len(blks)==0):
                #blks=all_blks
                print("haaai")#all_blk_place(blks,i,j)
        #    else:    
         #       blk_place(blks,i,j)
        #else:    
         #       blk_place(blks,i,j)
                  
def J3(i,j,val,blks,all_blks):
    if((val[i][j]==0)and(val[i][j+1]==0)and(val[i-1][j]==0)and(val[i-2][j]==0)):
        val[i][j]=6
        val[i][j+1]=6
        val[i-1][j]=6
        val[i-2][j]=6
        global blks
        all_blks.remove('J')
        if(((not(i==0))or(not(j==7)))):
            blks.remove('J')
            #if(len(blks)==0):
                #blks=all_blks
                print("haaai")#all_blk_place(blks,i,j)
        #    else:    
         #       blk_place(blks,i,j)
        #else:    
         #       blk_place(blks,i,j)
                  
def J4(i,j,val,blks,all_blks):
    if((val[i][j]==0)and(val[i-1][j]==0)and(val[i][j-1]==0)and(val[i][j-2]==0)):
        val[i][j]=6
        val[i-1][j]=6
        val[i][j-1]=6
        val[i][j-2]=6
        all_blks.remove('J')
        if(((not(i==0))or(not(j==7)))):
            global blks
            blks.remove('J')
            #if(len(blks)==0):
                #blks=all_blks
                print("haaai")#all_blk_place(blks,i,j)
        #    else:    
         #       blk_place(blks,i,j)
        #else:    
         #       blk_place(blks,i,j)
                  
def T1(i,j,val,blks,all_blks):
    if((val[i][j]==0)and(val[i+1][j]==0)and(val[i][j-1]==0)and(val[i][j+1]==0)):
        val[i][j]=7
        val[i+1][j]=7
        val[i][j-1]=7
        val[i][j+1]=7
        all_blks.remove('T')
        if(((not(i==0))or(not(j==0)))):
            global blks
            blks.remove('T')
            #if(len(blks)==0):
                #blks=all_blks
                print("haaai")#all_blk_place(blks,i,j)
        #    else:    
         #       blk_place(blks,i,j)
        #else:    
         #       blk_place(blks,i,j)
                  
def T2(i,j,val,blks,all_blks):
    if((val[i][j]==0)and(val[i+1][j]==0)and(val[i-1][j]==0)and(val[i][j+1]==0)):
        val[i][j]=7
        val[i+1][j]=7
        val[i-1][j]=7
        val[i][j+1]=7
        all_blks.remove('T')
        if(((not(i==0))or(not(j==0)))):
            global blks
            blks.remove('T')
            #if(len(blks)==0):
                #blks=all_blks
                print("haaai")#all_blk_place(blks,i,j)
        #    else:    
         #       blk_place(blks,i,j)
        #else:    
         #       blk_place(blks,i,j)
                  
def T3(i,j,val,blks,all_blks):
    if((val[i][j]==0)and(val[i-1][j]==0)and(val[i][j+1]==0)and(val[i][j-1]==0)):
        val[i][j]=7
        val[i-1][j]=7
        val[i][j+1]=7
        val[i][j-1]=7
        all_blks.remove('T')
        if(((not(i==0))or(not(j==0)))):
            global blks
            blks.remove('T')
            #if(len(blks)==0):
                #blks=all_blks
                print("haaai")#all_blk_place(blks,i,j)
        #    else:    
         #       blk_place(blks,i,j)
        #else:    
         #       blk_place(blks,i,j)
                  
def T4(i,j,val,blks,all_blks):
    if((val[i][j]==0)and(val[i][j-1]==0)and(val[i-1][j]==0)and(val[i+1][j]==0)):
        val[i][j]=7
        val[i][j-1]=7
        val[i-1][j]=7
        val[i+1][j]=7
        all_blks.remove('T')
        if(((not(i==0))or(not(j==0)))):
            global blks
            blks.remove('T')
            #if(len(blks)==0):
                #blks=all_blks
                print("haaai")#all_blk_place(blks,i,j)
        #    else:    
         #       blk_place(blks,i,j)
        #else:    
#                blk_place(blks,i,j)
