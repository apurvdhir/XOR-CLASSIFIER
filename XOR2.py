import numpy as np
import matplotlib.pyplot as plt

def sig(z):
    return 1/(1+np.exp(-z))

x1 = [1,1,0,0]
x2 = [1,0,1,0]
Yd = [0,1,1,0]

w3 = [0.5,0.9]
w4 = [0.4,1.0]
w5 = [-1.2,-1.1]

b3 = 0.8
b4 = -0.1
b5 = 0.3
a=0.1
count = 0 
epoch = 1

msq_li = list()
while epoch < 50000:
    sqerr = list()
    for i in range(0,4):
         z1 = (w3[0]*x1[i]+w3[1]*x2[i])-b3
         z2 = (w4[0]*x1[i]+w4[1]*x2[i])-b4
         
         y3 = sig(z1)
         y4 = sig(z2)
         
         z3 = (w5[0]*y3+w5[1]*y4)-b5
        
         Ya = sig(z3)

         e = Yd[i] - Ya

         err_grad5 = Ya*(1-Ya)*e
         err_grad3 = y3*(1-y3)*err_grad5*w5[0]  
         err_grad4 = y4*(1-y4)*err_grad5*w5[1]

         del_w35 =  a*err_grad5*y3
         del_w45 =  a*err_grad5*y4

         del_w13 =  a*err_grad3*x1[i]
         del_w23 =  a*err_grad3*x2[i]

         del_w14 =  a*err_grad4*x1[i]
         del_w24 =  a*err_grad4*x2[i]

         w3[0] += del_w13
         w3[1] += del_w23

         w4[0] += del_w14
         w4[1] += del_w24

         w5[0] += del_w35
         w5[1] += del_w45

         b3 = b3 + (a*(-1)*err_grad3)
         b4 = b4 + (a*(-1)*err_grad4)
         b5 = b5 + (a*(-1)*err_grad5)

         #count += 1
         #print(count)
         err = e*e
         
         sqerr.append(err)
        

       
    msq = sum(sqerr)/i
    msq_li.append(msq)
    if msq < 0.001:
        break
    else:
        epoch += 1 
print(epoch)    

print(w3)
#print(w4)
#print(w5)

#print(b3,b4,b5)
print(sqerr)
#print(msq_li)
X_axis = np.linspace(0,epoch,num=epoch)

plt.plot(X_axis,msq_li)
plt.show()




