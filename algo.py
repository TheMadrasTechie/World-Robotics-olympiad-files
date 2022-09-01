from array import *
import numpy
a=numpy.zeros((8, 8))
frst_block = input("enter value")

all_blocks = ['O','O','I','I','S','S','Z','Z','L','L','J','J','T']#,'U','U','U','U','U','U','U']

blocks = ['O','S','I','L','J']


def print_matrix():
    for f in range (0,8):
        print(str(a[7-f]))
    print("\n\n\n\n")    
def O(i,j,val,blks):
    if((val[i][j]==0)and(val[i][j+1]==0)and(val[i+1][j+1]==0)and(val[i+1][j]==0)):
        val[i][j]=1
        val[i][j+1]=1
        val[i+1][j+1]=1
        val[i+1][j]=1
        print(str(i)+"\t"+str(j))
        all_blocks.remove('O')
        print("dd")
        if(((not(i==0))or(not(j==0)))):
             global blocks
             blocks.remove('O')
             if(len(blocks)==0):
                #blocks=all_blocks
                print(str(i)+"\t"+str(j))#all_blk_place(blocks,i,j)
             else:    
                blk_place(blocks,i,j)
        else:    
                blk_place(blocks,i,j)           
def I1(i,j,val,blks):
    if((val[i][j]==0)and(val[i+1][j]==0)and(val[i+2][j]==0)and(val[i+3][j]==0)):
        val[i][j]=2
        val[i+1][j]=2
        val[i+2][j]=2
        val[i+3][j]=2
        all_blocks.remove('I')
        if(((not(i==0))or(not(j==0)))):
            global blocks
            blocks.remove('I')
            if(len(blocks)==0):
                #blocks=all_blocks
                print("haaai")#all_blk_place(blocks,i,j)
            else:    
                blk_place(blocks,i,j)
        else:    
                blk_place(blocks,i,j)
def I2(i,j,val,blks):
    if((val[i][j]==0)and(val[i][j+1]==0)and(val[i][j+2]==0)and(val[i][j+3]==0)):
        val[i][j]=2
        val[i][j+1]=2
        val[i][j+2]=2
        val[i][j+3]=2
        all_blocks.remove('I')
        if(((not(i==0))or(not(j==0)))):
            global blocks
            blocks.remove('I')
            if(len(blocks)==0):
                #blocks=all_blocks
                print("haaai")#all_blk_place(blocks,i,j)
            else:    
                blk_place(blocks,i,j)
        else:    
                blk_place(blocks,i,j)         
                  
def S1(i,j,val,blks):
    if((val[i][j]==0)and(val[i][j+1]==0)and(val[i+1][j+1]==0)and(val[i+1][j+2]==0)):
        val[i][j]=3
        val[i][j+1]=3
        val[i+1][j+1]=3
        val[i+1][j+2]=3
        all_blocks.remove('S')
        if(((not(i==0))or(not(j==0)))):
            global blocks
            blocks.remove('S')
            if(len(blocks)==0):
                #blocks=all_blocks
                print("haaai")#all_blk_place(blocks,i,j)
            else:    
                blk_place(blocks,i,j)
        else:    
                blk_place(blocks,i,j)
                  
def S2(i,j,val,blks):
    if((val[i][j]==0)and(val[i-1][j]==0)and(val[i-1][j+1]==0)and(val[i-2][j+1]==0)):
        val[i][j]=3
        val[i-1][j]=3
        val[i-1][j+1]=3
        val[i-2][j+1]=3
        all_blocks.remove('S')
        if(((not(i==0))or(not(j==0)))):
            global blocks
            blocks.remove('S')
            if(len(blocks)==0):
                #blocks=all_blocks
                print("haaai")#all_blk_place(blocks,i,j)
            else:    
                blk_place(blocks,i,j)
        else:    
                blk_place(blocks,i,j)           
                  
def Z1(i,j,val,blks):
    if((val[i][j]==0)and(val[i][j-1]==0)and(val[i+1][j-1]==0)and(val[i+1][j-2]==0)):
        val[i][j]=4
        val[i][j-1]=4
        val[i+1][j-1]=4
        val[i+1][j-2]=4 
        all_blocks.remove('Z')
        if(((not(i==0))or(not(j==7)))):
            global blocks
            blocks.remove('Z')
            if(len(blocks)==0):
                #blocks=all_blocks
                print("haaai")#all_blk_place(blocks,i,j)
            else:    
                blk_place(blocks,i,j)
        else:    
                blk_place(blocks,i,j)
def Z2(i,j,val,blks):
    if((val[i][j]==0)and(val[i+1][j]==0)and(val[i+1][j+1]==0)and(val[i+2][j+1]==0)):
        val[i][j]=4
        val[i+1][j]=4
        val[i+1][j+1]=4
        val[i+2][j+1]=4
        all_blocks.remove('Z')
        if(((not(i==0))or(not(j==7)))):
            global blocks
            blocks.remove('Z')
            if(len(blocks)==0):
                #blocks=all_blocks
                print("haaai")#all_blk_place(blocks,i,j)
            else:    
                blk_place(blocks,i,j)
        else:    
                blk_place(blocks,i,j)        
def L1(i,j,val,blks):
    if((val[i][j]==0)and(val[i][j+1]==0)and(val[i+1][j]==0)and(val[i+2][j]==0)):
        val[i][j]=5
        val[i][j+1]=5
        val[i+1][j]=5
        val[i+2][j]=5    
        all_blocks.remove('L')                                   
        if(((not(i==0))or(not(j==0)))):
            global blocks
            blocks.remove('L')
            if(len(blocks)==0):
                #blocks=all_blocks
                print("haaai")#all_blk_place(blocks,i,j)
            else:    
                blk_place(blocks,i,j)
        else:    
                blk_place(blocks,i,j)
                  
def L2(i,j,val,blks):
    if((val[i][j]==0)and(val[i][j+1]==0)and(val[i][j+2]==0)and(val[i-1][j]==0)):
        val[i][j]=5
        val[i][j+1]=5
        val[i][j+2]=5
        val[i-1][j]=5    
        all_blocks.remove('L')                                   
        if(((not(i==0))or(not(j==0)))):
            global blocks
            blocks.remove('L')
            if(len(blocks)==0):
                #blocks=all_blocks
                print("haaai")#all_blk_place(blocks,i,j)
            else:    
                blk_place(blocks,i,j)
        else:    
                blk_place(blocks,i,j)
                  
def L3(i,j,val,blks):
    if((val[i][j]==0)and(val[i][j-1]==0)and(val[i-1][j]==0)and(val[i-2][j]==0)):
        val[i][j]=5
        val[i][j-1]=5
        val[i-1][j]=5
        val[i-2][j]=5 
        print("yyy")
        all_blocks.remove('L')
        if(((not(i==0))or(not(j==0)))):
            global blocks
            blocks.remove('L')
            if(len(blocks)==0):
                #blocks=all_blocks
                print("haaai")#all_blk_place(blocks,i,j)
            else:    
                blk_place(blocks,i,j)
        else:    
                blk_place(blocks,i,j)
                  
def L4(i,j,val,blks):
    if((val[i][j]==0)and(val[i+1][j]==0)and(val[i][j-1]==0)and(val[i][j-2]==0)):
        val[i][j]=5
        val[i+1][j]=5
        val[i][j-1]=5
        val[i][j-2]=5 
        all_blocks.remove('L')
        if(((not(i==0))or(not(j==0)))):
            global blocks
            blocks.remove('L')
            if(len(blocks)==0):
                #blocks=all_blocks
                print("haaai")#all_blk_place(blocks,i,j)
            else:    
                blk_place(blocks,i,j)
        else:    
                blk_place(blocks,i,j)
                  
def J1(i,j,val,blks):
    if((val[i][j]==0)and(val[i+1][j]==0)and(val[i+2][j]==0)and(val[i][j-1]==0)):
        val[i][j]=6
        val[i+1][j]=6
        val[i+2][j]=6
        val[i][j-1]=6 
        all_blocks.remove('J')
        if():
            global blocks
            blocks.remove('J')
            if(len(blocks)==0):
                #blocks=all_blocks
                print("haaai")#all_blk_place(blocks,i,j)
            else:    
                blk_place(blocks,i,j)
        else:    
                blk_place(blocks,i,j)
                  
def J2(i,j,val,blks):
    if((val[i][j]==0)and(val[i+1][j]==0)and(val[i][j+1]==0)and(val[i][j+2]==0)):
        val[i][j]=6
        val[i+1][j]=6
        val[i][j+1]=6
        val[i][j+2]=6 
        all_blocks.remove('J')
        if(((not(i==0))or(not(j==7)))):
            global blocks
            blocks.remove('J')
            if(len(blocks)==0):
                #blocks=all_blocks
                print("haaai")#all_blk_place(blocks,i,j)
            else:    
                blk_place(blocks,i,j)
        else:    
                blk_place(blocks,i,j)
                  
def J3(i,j,val,blks):
    if((val[i][j]==0)and(val[i][j+1]==0)and(val[i-1][j]==0)and(val[i-2][j]==0)):
        val[i][j]=6
        val[i][j+1]=6
        val[i-1][j]=6
        val[i-2][j]=6
        global blocks
        all_blocks.remove('J')
        if(((not(i==0))or(not(j==7)))):
            blocks.remove('J')
            if(len(blocks)==0):
                #blocks=all_blocks
                print("haaai")#all_blk_place(blocks,i,j)
            else:    
                blk_place(blocks,i,j)
        else:    
                blk_place(blocks,i,j)
                  
def J4(i,j,val,blks):
    if((val[i][j]==0)and(val[i-1][j]==0)and(val[i][j-1]==0)and(val[i][j-2]==0)):
        val[i][j]=6
        val[i-1][j]=6
        val[i][j-1]=6
        val[i][j-2]=6
        all_blocks.remove('J')
        if(((not(i==0))or(not(j==7)))):
            global blocks
            blocks.remove('J')
            if(len(blocks)==0):
                #blocks=all_blocks
                print("haaai")#all_blk_place(blocks,i,j)
            else:    
                blk_place(blocks,i,j)
        else:    
                blk_place(blocks,i,j)
                  
def T1(i,j,val,blks):
    if((val[i][j]==0)and(val[i+1][j]==0)and(val[i][j-1]==0)and(val[i][j+1]==0)):
        val[i][j]=7
        val[i+1][j]=7
        val[i][j-1]=7
        val[i][j+1]=7
        all_blocks.remove('T')
        if(((not(i==0))or(not(j==0)))):
            global blocks
            blocks.remove('T')
            if(len(blocks)==0):
                #blocks=all_blocks
                print("haaai")#all_blk_place(blocks,i,j)
            else:    
                blk_place(blocks,i,j)
        else:    
                blk_place(blocks,i,j)
                  
def T2(i,j,val,blks):
    if((val[i][j]==0)and(val[i+1][j]==0)and(val[i-1][j]==0)and(val[i][j+1]==0)):
        val[i][j]=7
        val[i+1][j]=7
        val[i-1][j]=7
        val[i][j+1]=7
        all_blocks.remove('T')
        if(((not(i==0))or(not(j==0)))):
            global blocks
            blocks.remove('T')
            if(len(blocks)==0):
                #blocks=all_blocks
                print("haaai")#all_blk_place(blocks,i,j)
            else:    
                blk_place(blocks,i,j)
        else:    
                blk_place(blocks,i,j)
                  
def T3(i,j,val,blks):
    if((val[i][j]==0)and(val[i-1][j]==0)and(val[i][j+1]==0)and(val[i][j-1]==0)):
        val[i][j]=7
        val[i-1][j]=7
        val[i][j+1]=7
        val[i][j-1]=7
        all_blocks.remove('T')
        if(((not(i==0))or(not(j==0)))):
            global blocks
            blocks.remove('T')
            if(len(blocks)==0):
                #blocks=all_blocks
                print("haaai")#all_blk_place(blocks,i,j)
            else:    
                blk_place(blocks,i,j)
        else:    
                blk_place(blocks,i,j)
                  
def T4(i,j,val,blks):
    if((val[i][j]==0)and(val[i][j-1]==0)and(val[i-1][j]==0)and(val[i+1][j]==0)):
        val[i][j]=7
        val[i][j-1]=7
        val[i-1][j]=7
        val[i+1][j]=7
        all_blocks.remove('T')
        if(((not(i==0))or(not(j==0)))):
            global blocks
            blocks.remove('T')
            if(len(blocks)==0):
                #blocks=all_blocks
                print("haaai")#all_blk_place(blocks,i,j)
            else:    
                blk_place(blocks,i,j)
        else:    
                blk_place(blocks,i,j)

def O_val(i,j,val):
    if((not(i>6))and(not(j>6))):
       if((val[i][j]==0)and(val[i][j+1]==0)and(val[i+1][j+1]==0)and(val[i+1][j]==0)):
          return 2
       else:    
          return 0
    else:
        return 0      
def I1_val(i,j,val):
    if((not(i>4))and(not(j>7))):

       if((val[i][j]==0)and(val[i+1][j]==0)and(val[i+2][j]==0)and(val[i+3][j]==0)):
           return 1
       else:
           return 0    
    else: 
        return 0       
def I2_val(i,j,val):
    if((not(i>7))and(not(j>4))):
      if((val[i][j]==0)and(val[i][j+1]==0)and(val[i][j+2]==0)and(val[i][j+3]==0)):
        return 4
      else:
        return 0  
    else:
        return 0
def S1_val(i,j,val):
    if((not(i>6))and(not(j>5))):
       if((val[i][j]==0)and(val[i][j+1]==0)and(val[i+1][j+1]==0)and(val[i+1][j+2]==0)):
          return 2
       else:
          return 0
    else:
          return 0    
def S2_val(i,j,val):    
    if((not(i<2))and(not(j>6))):

        if((val[i][j]==0)and(val[i-1][j]==0)and(val[i-1][j+1]==0)and(val[i-2][j+1]==0)):
           return 1
        else:
           return 0
    else:
        return 0       
def Z1_val(i,j,val):
    if((not(i>6))and(not(j<2))):
       if((val[i][j]==0)and(val[i][j-1]==0)and(val[i+1][j-1]==0)and(val[i+1][j-2]==0)):
         return 2
       else:
         return 0
    else:
        return 0
def Z2_val(i,j,val):
    if((not(i>5))and(not(j>6))):
      if((val[i][j]==0)and(val[i+1][j]==0)and(val[i+1][j+1]==0)and(val[i+2][j+1]==0)):
        return 1 
      else:
        return 0
    else: 
        return 0    
def L1_val(i,j,val): 
    if((not(i>5))and(not(j>6))):
       if((val[i][j]==0)and(val[i][j+1]==0)and(val[i+1][j]==0)and(val[i+2][j]==0)):
          return 2 
       else:
          return 0 
    else:
        return 0       
def L2_val(i,j,val):
    if((not(i<1))and(not(j>5))):
       if((val[i][j]==0)and(val[i][j+1]==0)and(val[i][j+2]==0)and(val[i-1][j]==0)):
          return 3
       else:
          return 0
    else:
        return 0      
def L3_val(i,j,val):
    if((not(i<2))and(not(j>7))):
      if((val[i][j]==0)and(val[i][j-1]==0)and(val[i-1][j]==0)and(val[i-2][j]==0)):
          return 2
      else:
          return 0
    else:
       return 0      
def L4_val(i,j,val):
    if((not(i>6))and(not(j<2))):
      if((val[i][j]==0)and(val[i+1][j]==0)and(val[i][j-1]==0)and(val[i][j-2]==0)):
         return 3
      else:
        return 0 
    else: 
        return 0   
def J1_val(i,j,val):
    if((not(i>5))and(not(j<1))):
      if((val[i][j]==0)and(val[i+1][j]==0)and(val[i+2][j]==0)and(val[i][j-1]==0)):
        return 2
      else:
        return 0
    else:
        return 0    
def J2_val(i,j,val):
    if((not(i>6))and(not(j>5))):
       if((val[i][j]==0)and(val[i+1][j]==0)and(val[i][j+1]==0)and(val[i][j+2]==0)):
         return 3
       else:
         return 0
    else:
         return 0     
def J3_val(i,j,val):
    if((not(i<2))and(not(j>6))):
      if((val[i][j]==0)and(val[i][j+1]==0)and(val[i-1][j]==0)and(val[i-2][j]==0)):
        return 2
      else:
        return 0
    else:
        return 0    
def J4_val(i,j,val):
    if((not(i<1))and(not(j<2))):
      if((val[i][j]==0)and(val[i-1][j]==0)and(val[i][j-1]==0)and(val[i][j-2]==0)):
         return 3
      else:
         return 0
    else:
       return  0   
def T1_val(i,j,val):
    if((not(i>6))and((1<=j<=6))):
       if((val[i][j]==0)and(val[i+1][j]==0)and(val[i][j-1]==0)and(val[i][j+1]==0)):
          return 3
       else:
          return 0
    else:
        return 0      
def T2_val(i,j,val):
    if((1<=i<=6)and(not(j>6))):
       if((val[i][j]==0)and(val[i+1][j]==0)and(val[i-1][j]==0)and(val[i][j+1]==0)):
          return 2
       else:
          return 0
    else:
        return 0      
def T3_val(i,j,val):
    if((not(i<1))and((1<=j<=6))):
       if((val[i][j]==0)and(val[i-1][j]==0)and(val[i][j+1]==0)and(val[i][j-1]==0)):
          return 3
       else:
          return 0
    else:      
        return 0
def T4_val(i,j,val):
    if(((1<=i<=6))and(not(j>1))):
       if((val[i][j]==0)and(val[i][j-1]==0)and(val[i-1][j]==0)and(val[i+1][j]==0)):
          return 2
       else:
          return 0
    else: 
        return 0
#o,i,s,z,l,j,t=0,0,0,0,0,0,0
# o=0
# i=0
# s=0
# z=0
# l=0
# j=0
# t=0
def I_main(q,w,val):

    i_val_1=I1_val(q,w,val)
    i_val_2=I2_val(q,w,val)
    if(i_val_2>i_val_1):
        return i_val_2
    elif(i_val_1>i_val_2):
        return i_val_1    
    else: 
        return 0    
def S_main(q,w,val):

    i_val_1=S1_val(q,w,val)
    i_val_2=S2_val(q,w,val)
    if(i_val_2>i_val_1):
        return i_val_2
    elif(i_val_1>i_val_2):
        return i_val_1        
    else: 
        return 0
def Z_main(q,w,val):

    i_val_1=Z1_val(q,w,val)
    i_val_2=Z2_val(q,w,val)
    if(i_val_2>i_val_1):
        return i_val_2
    elif(i_val_1>i_val_2):
        return i_val_1        
    else: 
        return 0
def L_main(q,w,val):

    l_val_1=L1_val(q,w,val)
    l_val_2=L2_val(q,w,val)
    l_val_3=L3_val(q,w,val)
    l_val_4=L4_val(q,w,val)
    if((l_val_1>l_val_2)and(l_val_1>l_val_3)and(l_val_1>l_val_4)):
        return l_val_1 ,1
    elif((l_val_2>l_val_1)and(l_val_2>l_val_3)and(l_val_2>l_val_4)):
        return l_val_2 ,2   
    elif((l_val_3>l_val_1)and(l_val_3>l_val_2)and(l_val_3>l_val_4)):
        return l_val_3,3
    elif((l_val_4>l_val_1)and(l_val_4>l_val_2)and(l_val_4>l_val_3)):
        return l_val_4  ,4      
    else: 
        return 0,0
def J_main(q,w,val):

    l_val_1=J1_val(q,w,val)
    l_val_2=J2_val(q,w,val)
    l_val_3=J3_val(q,w,val)
    l_val_4=J4_val(q,w,val)
    if((l_val_1>l_val_2)and(l_val_1>l_val_3)and(l_val_1>l_val_4)):
        return l_val_1,1
    elif((l_val_2>l_val_1)and(l_val_2>l_val_3)and(l_val_2>l_val_4)):
        return l_val_2  ,2  
    elif((l_val_3>l_val_1)and(l_val_3>l_val_2)and(l_val_3>l_val_4)):
        return l_val_3,3
    elif((l_val_4>l_val_1)and(l_val_4>l_val_2)and(l_val_4>l_val_3)):
        return l_val_4  ,4   
    else: 
        return 0,0
def T_main(q,w,val):

    l_val_1=T1_val(q,w,val)
    l_val_2=T2_val(q,w,val)
    l_val_3=T3_val(q,w,val)
    l_val_4=T4_val(q,w,val)
    if((l_val_1>l_val_2)and(l_val_1>l_val_3)and(l_val_1>l_val_4)):
        return l_val_1,1
    elif((l_val_2>l_val_1)and(l_val_2>l_val_3)and(l_val_2>l_val_4)):
        return l_val_2,2    
    elif((l_val_3>l_val_1)and(l_val_3>l_val_2)and(l_val_3>l_val_4)):
        return l_val_3,3
    elif((l_val_4>l_val_1)and(l_val_4>l_val_2)and(l_val_4>l_val_3)):
        return l_val_4,4                           
    else: 
        return 0,0
def val_cmpr(o,i,s,z,l,j,t):
    if((o>i)and(o>s)and(o>z)and(o>l)and(o>j)and(o>t)):
        return o ,'O'
    elif((i>o)and(i>s)and(i>z)and(i>l)and(i>j)and(i>t)):
        return i , 'I'
    elif((s>o)and(s>i)and(s>z)and(s>l)and(s>j)and(s>t)):  
        return s , 'S'
    elif((z>o)and(z>i)and(z>s)and(z>l)and(z>j)and(z>t)):
        return z , 'Z'
    elif((l>o)and(l>i)and(l>s)and(l>z)and(l>j)and(l>t)):        
        return l , 'L'
    elif((j>o)and(j>i)and(j>s)and(j>z)and(j>l)and(j>t)):
        return j , 'J'
    elif((t>o)and(t>i)and(t>s)and(t>z)and(t>l)and(t>j)):      
        return t , 'T'
    else:
        return o , 'A'    
def get_ind_blocks(val):
    o='A'
    i='A'  
    s='A'
    z='A'
    l='A'
    j='A'
    t='A'
    for x in range(0,len(val)):
           # print(val[x])
            if(val[x]=='O'):
                o='O'
                #print("O\t"+str(o))
            elif(val[x]=='I'):    
                i='I'
                #print("I\t"+str(i))
            elif(val[x]=='S'):        
                s='S'
                #print("S\t"+str(s))
            elif(val[x]=='Z'):        
                z='Z'
                #print("Z\t"+str(z))
            elif(val[x]=='L'):        
                l='L'
                #print("L\t"+str(l))
            elif(val[x]=='J'):        
                j='J'
                #print("J\t"+str(j))
            elif(val[x]=='T'):        
                 t='T'
    return    o,i,s,z,l,j,t

def points_val(i,j):
    f=0
    for gt in range(0,8):
        if(not(a[i][gt]==0)):
            f=i
    return f,f+3
def blk_place(blk,motu,dotu):
    print(blk)
    print(all_blocks)
    o,i,s,z,l,j,t= get_ind_blocks(blk)
    o_val=0
    i_val=0  
    s_val=0
    z_val=0
    l_val=0
    j_val=0
    t_val=0
    lm=0
    jm=0
    tm=0
    for q in range(0,8):
        for w in range(0,8):
            if(o=='O'):
                o_val=O_val(q,w,a)
                #print("O\t"+str(o))
            if(i=='I'):    
                i_val=I_main(q,w,a)
                #print("I\t"+str(i))
            if(s=='S'):        
                s_val=S_main(q,w,a)
                #print("S\t"+str(s))
            if(z=='Z'):        
                z_val=Z_main(q,w,a)
                #print("Z\t"+str(z_val))
            if(l=='L'):        
                l_val,lm=L_main(q,w,a)
                #print("L\t"+str(m))
            if(j=='J'):        
                j_val,jm=J_main(q,w,a)
                #print(str(j_val)+"dd\t"+str(m))
                #print("J\t"+str(j))
            if(t=='T'):        
                 t_val,tm=T_main(q,w,a)     
                 #print("T\t"+str(t))
            
            value,alphabet    =val_cmpr(o_val,i_val,s_val,z_val,l_val,j_val,t_val)
            global blocks
            if(len(blocks)==1):
                for wit in range(0,(len(all_blocks)-1)):                     
                  if((value==o_val)and(alphabet==all_blocks[wit])and(alphabet==blocks[0])and(alphabet==o)):
                     #print("O")   
                     O(q,w,a,blocks)
                     break
                  elif((value==i_val)and(alphabet==all_blocks[wit])and(alphabet==blocks[0])and(alphabet==i)):
                      # print("i")    
                      # print(str(i))
                       if(i_val==4):
                         I2(q,w,a,blocks)
                       elif(i_val==1): 
                         I1(q,w,a,blocks)
                       break  
                  elif((value==s_val)and(alphabet==all_blocks[wit])and(alphabet==blocks[0])and(alphabet==s)):
                        print("s")
                        print(str(s))
                        if(s_val==2):
                          S1(q,w,a,blocks)
                        elif(s_val==1):
                          S2(q,w,a,blocks)          
                        break  
                  elif((value==z_val)and(alphabet==all_blocks[wit])and(alphabet==blocks[0])and(alphabet==z)):
                        print("zhh11h") 
                        if(z_val==2):
                           Z1(q,w,a,blocks)
                           break
                        elif(z_val==1):
                           Z2(q,w,a,blocks)  
                           break   
                  elif((value==l_val)and(alphabet==all_blocks[wit])and(alphabet==blocks[0])and(alphabet==l)):
                        print("l\t"+str(l_val)+"\t"+str(lm)) 
                        if((l_val==2)and(lm==1)):
                           L1(q,w,a,blocks)
                        elif((l_val==3)and(lm==2)):
                           L2(q,w,a,blocks)    
                        elif((l_val==2)and(lm==3)):
                           L3(q,w,a,blocks)    
                        elif((l_val==3)and(lm==4)):
                           L4(q,w,a,blocks)          
                        break   
                  elif((value==j_val)and(alphabet==all_blocks[wit])and(alphabet==blocks[0])and(alphabet==j)):
                        print("j") 
                        #print(str(j)+"\t"+str(m))
                        if((j_val==2)and(jm==1)):
                           J1(q,w,a,blocks)
                        elif((j_val==3)and(jm==2)):
                           J2(q,w,a,blocks)    
                        elif((j_val==2)and(jm==3)):
                           J3(q,w,a,blocks)    
                        elif((j_val==3)and(jm==4)):
                           J4(q,w,a,blocks)                  
                        break   
                  elif((value==t_val)and(alphabet==all_blocks[wit])and(alphabet==blocks[0])and(alphabet==t)):
                        print("t") 
                        if((t_val==2)and(tm==1)):
                           T1(q,w,a,blocks)
                        elif((t_val==3)and(tm==2)):
                           T2(q,w,a,blocks)    
                        elif((t_val==2)and(tm==3)):
                           T3(q,w,a,blocks)    
                        elif((t_val==3)and(tm==4)):
                           T4(q,w,a,blocks)                             
                        break
            else:    
              for ghat in range(0,(len(all_blocks)-1)):                     
                for hat in range(0,(len(blocks)-1)):                  
                  #print(blocks[hat]+"\t"+str(ghat)+"\t"+all_blocks[ghat])
                  #print(all_blocks[ghat])
                  if((value==o_val)and(alphabet==all_blocks[ghat])and(alphabet==blocks[hat])and(alphabet==o)):
                     #print("O")   
                     O(q,w,a,blocks)
                     break
                  elif((value==i_val)and(alphabet==all_blocks[ghat])and(alphabet==blocks[hat])and(alphabet==i)):
                      # print("i")    
                      # print(str(i))
                       if(i_val==4):
                         I2(q,w,a,blocks)
                       elif(i_val==1): 
                         I1(q,w,a,blocks)
                       break  
                  elif((value==s_val)and(alphabet==all_blocks[ghat])and(alphabet==blocks[hat])and(alphabet==s)):
                        print("s")
                        #print(str(s))
                        if(s_val==2):
                          S1(q,w,a,blocks)
                        elif(s_val==1):
                          S2(q,w,a,blocks)          
                        break  
                  elif((value==z_val)and(alphabet==all_blocks[ghat])and(alphabet==blocks[hat])and(alphabet==z)):
                        print("zhhh") 
                        if(z_val==2):
                           Z1(q,w,a,blocks)
                        elif(z_val==1):
                           Z2(q,w,a,blocks)  
                        break   
                  elif((value==l_val)and(alphabet==all_blocks[ghat])and(alphabet==blocks[hat])and(alphabet==l)):
                        #print("l\t"+str(l_val)+"\t"+str(lm)) 
                        if((l_val==2)and(lm==1)):
                           L1(q,w,a,blocks)
                        elif((l_val==3)and(lm==2)):
                           L2(q,w,a,blocks)    
                        elif((l_val==2)and(lm==3)):
                           L3(q,w,a,blocks)    
                        elif((l_val==3)and(lm==4)):
                           L4(q,w,a,blocks)          
                        break   
                  elif((value==j_val)and(alphabet==all_blocks[ghat])and(alphabet==blocks[hat])and(alphabet==j)):
                        print("j") 
                        #print(str(j)+"\t"+str(m))
                        if((j_val==2)and(jm==1)):
                           J1(q,w,a,blocks)
                        elif((j_val==3)and(jm==2)):
                           J2(q,w,a,blocks)    
                        elif((j_val==2)and(jm==3)):
                           J3(q,w,a,blocks)    
                        elif((j_val==3)and(jm==4)):
                           J4(q,w,a,blocks)                  
                        break   
                  elif((value==t_val)and(alphabet==all_blocks[ghat])and(alphabet==blocks[hat])and(alphabet==t)):
                        print("t") 
                        if((t_val==2)and(tm==1)):
                           T1(q,w,a,blocks)
                        elif((t_val==3)and(tm==2)):
                           T2(q,w,a,blocks)    
                        elif((t_val==2)and(tm==3)):
                           T3(q,w,a,blocks)    
                        elif((t_val==3)and(tm==4)):
                           T4(q,w,a,blocks)                             
                        break
                        
def all_blk_place(blk,motu,dotu):
    print(blk)
    print(all_blocks)
    o,i,s,z,l,j,t= get_ind_blocks(blk)
    o_val=0
    i_val=0  
    s_val=0
    z_val=0
    l_val=0
    j_val=0
    t_val=0
    m=0
    print(z)
    for q in range(0,8):
        for w in range(0,8):
            if(o=='O'):
                o_val=O_val(q,w,a)
                #print("O\t"+str(o))
            if(i=='I'):    
                i_val=I_main(q,w,a)
                #print("I\t"+str(i))
            if(s=='S'):        
                s_val=S_main(q,w,a)
                #print("S\t"+str(s))
            if(z=='Z'):        
                z_val=Z_main(q,w,a)
                #print("Z\t"+str(z_val))
            if(l=='L'):        
                l_val,m=L_main(q,w,a)
                #print("L\t"+str(l))
            if(j=='J'):        
                j_val,m=J_main(q,w,a)
                #print(str(j_val)+"dd\t"+str(m))
                #print("J\t"+str(j))
            if(t=='T'):        
                 t_val,m=T_main(q,w,a)     
                 #print("T\t"+str(t))
            
            value,alphabet    =val_cmpr(o_val,i_val,s_val,z_val,l_val,j_val,t_val)
            global blocks
            if(len(blocks)==1):
                for wit in range(0,(len(all_blocks)-1)):                     
                  if((value==o_val)and(alphabet==all_blocks[wit])and(alphabet==blocks[0])and(alphabet==o)):
                     #print("O")   
                     O(q,w,a,blocks)
                     break
                  elif((value==i_val)and(alphabet==all_blocks[wit])and(alphabet==blocks[0])and(alphabet==i)):
                      # print("i")    
                      # print(str(i))
                       if(i_val==4):
                         I2(q,w,a,blocks)
                       elif(i_val==1): 
                         I1(q,w,a,blocks)
                       break  
                  elif((value==s_val)and(alphabet==all_blocks[wit])and(alphabet==blocks[0])and(alphabet==s)):
                        print("s")
                        print(str(s))
                        if(s_val==2):
                          S1(q,w,a,blocks)
                        elif(s_val==1):
                          S2(q,w,a,blocks)          
                        break  
                  elif((value==z_val)and(alphabet==all_blocks[wit])and(alphabet==blocks[0])and(alphabet==z)):
                        print("zhh11h") 
                        if(z_val==2):
                           Z1(q,w,a,blocks)
                           break
                        elif(z_val==1):
                           Z2(q,w,a,blocks)  
                           break   
                  elif((value==l_val)and(alphabet==all_blocks[wit])and(alphabet==blocks[0])and(alphabet==l)):
                        print("l") 
                        if((l_val==2)and(m==1)):
                           L1(q,w,a,blocks)
                        elif((l_val==3)and(m==2)):
                           L2(q,w,a,blocks)    
                        elif((l_val==2)and(m==3)):
                           L3(q,w,a,blocks)    
                        elif((l_val==3)and(m==4)):
                           L4(q,w,a,blocks)          
                        break   
                  elif((value==j_val)and(alphabet==all_blocks[wit])and(alphabet==blocks[0])and(alphabet==j)):
                        print("j") 
                        #print(str(j)+"\t"+str(m))
                        if((j_val==2)and(m==1)):
                           J1(q,w,a,blocks)
                        elif((j_val==3)and(m==2)):
                           J2(q,w,a,blocks)    
                        elif((j_val==2)and(m==3)):
                           J3(q,w,a,blocks)    
                        elif((j_val==3)and(m==4)):
                           J4(q,w,a,blocks)                  
                        break   
                  elif((value==t_val)and(alphabet==all_blocks[wit])and(alphabet==blocks[0])and(alphabet==t)):
                        print("t") 
                        if((t_val==2)and(m==1)):
                           T1(q,w,a,blocks)
                        elif((t_val==3)and(m==2)):
                           T2(q,w,a,blocks)    
                        elif((t_val==2)and(m==3)):
                           T3(q,w,a,blocks)    
                        elif((t_val==3)and(m==4)):
                           T4(q,w,a,blocks)                             
                        break
            else:    
              for ghat in range(0,(len(all_blocks)-1)):                     
                for hat in range(0,(len(blocks)-1)):                  
                  #print(blocks[hat]+"\t"+str(ghat)+"\t"+all_blocks[ghat])
                  #print(all_blocks)
                  if((value==o_val)and(alphabet==all_blocks[ghat])and(alphabet==blocks[hat])and(alphabet==o)):
                     #print("O")   
                     O(q,w,a,blocks)
                     break
                  elif((value==i_val)and(alphabet==all_blocks[ghat])and(alphabet==blocks[hat])and(alphabet==i)):
                      # print("i")    
                      # print(str(i))
                       if(i_val==4):
                         I2(q,w,a,blocks)
                       elif(i_val==1): 
                         I1(q,w,a,blocks)
                       break  
                  elif((value==s_val)and(alphabet==all_blocks[ghat])and(alphabet==blocks[hat])and(alphabet==s)):
                       # print("s")
                        print(str(s))
                        if(s_val==2):
                          S1(q,w,a,blocks)
                        elif(s_val==1):
                          S2(q,w,a,blocks)          
                        break  
                  elif((value==z_val)and(alphabet==all_blocks[ghat])and(alphabet==blocks[hat])and(alphabet==z)):
                        print("zhhh") 
                        if(z_val==2):
                           Z1(q,w,a,blocks)
                        elif(z_val==1):
                           Z2(q,w,a,blocks)  
                        break   
                  elif((value==l_val)and(alphabet==all_blocks[ghat])and(alphabet==blocks[hat])and(alphabet==l)):
                        print("l") 
                        if((l_val==2)and(m==1)):
                           L1(q,w,a,blocks)
                        elif((l_val==3)and(m==2)):
                           L2(q,w,a,blocks)    
                        elif((l_val==2)and(m==3)):
                           L3(q,w,a,blocks)    
                        elif((l_val==3)and(m==4)):
                           L4(q,w,a,blocks)          
                        break   
                  elif((value==j_val)and(alphabet==all_blocks[ghat])and(alphabet==blocks[hat])and(alphabet==j)):
                        print("j") 
                        #print(str(j)+"\t"+str(m))
                        if((j_val==2)and(m==1)):
                           J1(q,w,a,blocks)
                        elif((j_val==3)and(m==2)):
                           J2(q,w,a,blocks)    
                        elif((j_val==2)and(m==3)):
                           J3(q,w,a,blocks)    
                        elif((j_val==3)and(m==4)):
                           J4(q,w,a,blocks)                  
                        break   
                  elif((value==t_val)and(alphabet==all_blocks[ghat])and(alphabet==blocks[hat])and(alphabet==t)):
                        print("t") 
                        if((t_val==2)and(m==1)):
                           T1(q,w,a,blocks)
                        elif((t_val==3)and(m==2)):
                           T2(q,w,a,blocks)    
                        elif((t_val==2)and(m==3)):
                           T3(q,w,a,blocks)    
                        elif((t_val==3)and(m==4)):
                           T4(q,w,a,blocks)                             
                        break

        
        
#block_cmp(blocks)

# for x in range(0,8):
#   for y in range(0,8):
#       O(x,y,frst_block)
#       print(str(a[x][y]))
if(frst_block=='O'):
    O(0,0,a,blocks)
    blk_place(blocks,0,0)
if(frst_block=='I'):
    I1(0,0,a,blocks)
    blk_place(blocks,0,0)
if(frst_block=='S'):
    S1(0,0,a,blocks)
    blk_place(blocks,0,0)
if(frst_block=='Z'):
    Z1(0,7,a,blocks)    
    blk_place(blocks,0,0)
if(frst_block=='L'):
    L1(0,0,a,blocks)
    blk_place(blocks,0,0)
if(frst_block=='J'):
    J1(0,7,a,blocks)     
    blk_place(blocks,0,0)   


print_matrix()
# for ty6 in range (0,15):
#     print(str(a[14-ty6]))     


# for m in range(0,8):
#     for n in range(0,8):
#       if(m==0):
#           if((a[m][n]==0)):
#               v=a
#               block_det(v)
#       else:
#         break 

# name = input("enter value")
# print(name)
#OSZILJT
         
