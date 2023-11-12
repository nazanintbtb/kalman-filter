import random
import numpy as np
import matplotlib.pyplot as plt

import struct

def bin2float(b): #binary to float
    h = int(b, 2).to_bytes(8, byteorder="big")
    return struct.unpack('>d', h)[0]


def float2bin(f):# float to binary
    [d] = struct.unpack(">Q", struct.pack(">d", f))
    return f'{d:064b}'
def run_time_faulty_kalman(fault):# insert runtime fault to kalman filter
  nsample=100
  t = np.linspace(0, 10, 100)
  dt = 1.0/10
  x0=0
  vtrue= 10
  Xtrue=x0+t*vtrue
  
  phi = np.array([[1.0, dt], [0.0, 1.0]])
  Q = np.array([[0.0, 0.0], [0, 0]])
  P=np.array([[1.0,0.0],[0.0,1.0]])
  M=np.array([[1.0,0.0]]) 
  R=np.array([1.0])
  Xk_prev=np.array([0.0,0.5]) 
  Xk=[]
  z1=[]
  Xk_buffer=[]
  noise=np.random.normal(0, 10,100)
  for k in range(nsample) :
    z=10*t[k]+ x0 +noise[k]
    z1.append(z)
    rand0 = random.random()
    rand1 = random.random()
    rand2 = random.random()
    rand3 = random.random()
    
    if(((k==3)or(k==60) )& ((fault==1) & (rand0<= 0.5))):
        a=random.choice(random.choice(P))
        andis=np.where(P == a)
        andis=np.array(andis)
        a1=andis[0]
        b=andis[1]
        print("P_A",a)
        P[a1[0]][b[0]]=single_bit_flip_fault(a)

    if(((k==3)or(k==60) )& ((fault==3) & (rand0<= 0.5))):
        a=random.choice(random.choice(P))
        andis=np.where(P == a)
        andis=np.array(andis)
        a1=andis[0]
        b=andis[1]
        print("P_A",a)
        P[a1[0]][b[0]]=Zeero_all_bit_fault(a)

    if(((k==3) or(k==67))& ((fault==2) & (rand0<= 0.5))):
        val_a=random.choice(random.choice(P))
        andis=np.where(P == val_a)
        andis=np.array(andis)
        a1=andis[0]
        b=andis[1]
        print("P_A",val_a)
        P[a1[0]][b[0]]=Double_bit_flip_fault(val_a)
  
    if(((k==6)or(k==87) )&((fault==1) & (rand1 >= 0.5))):
        a=random.choice(random.choice(M))
        andis=np.where(M == a)
        andis=np.array(andis)
        a1=andis[0]
        b=andis[1]
        print("M",a)
        M[a1[0]][b[0]]=single_bit_flip_fault(a)

    if(((k==6)or(k==87) )&((fault==3) & (rand1 >= 0.5))):
        a=random.choice(random.choice(M))
        andis=np.where(M == a)
        andis=np.array(andis)
        a1=andis[0]
        b=andis[1]
        print("M",a)
        M[a1[0]][b[0]]=Zeero_all_bit_fault(a)

    p_pred=np.dot(np.dot(phi, P), phi.T) + Q
    if(((k==4)or(k==40))& ((fault==1) & (rand2<= 0.5))):
      a=random.choice(random.choice(p_pred))
      andis=np.where(p_pred == a)
      andis=np.array(andis)
      a1=andis[0]
      b=andis[1]
      print("ppred_a",a)
      p_pred[a1[0]][b[0]]=single_bit_flip_fault(a)

    if(((k==4)or(k==40))& ((fault==3) & (rand2<= 0.5))):
      a=random.choice(random.choice(p_pred))
      andis=np.where(p_pred == a)
      andis=np.array(andis)
      a1=andis[0]
      b=andis[1]
      print("ppred_a",a)
      p_pred[a1[0]][b[0]]=Zeero_all_bit_fault(a)
    if(((k==4)or(k==70))& ((fault==2) & (rand2<= 0.5))):
      val_a=random.choice(random.choice(p_pred))
      andis=np.where(p_pred == val_a)
      andis=np.array(andis)
      a1=andis[0]
      b=andis[1]
      print("ppred_a",val_a)
      p_pred[a1[0]][b[0]]=Double_bit_flip_fault(val_a)
    S=np.dot(np.dot(M, p_pred), M.T) + R
    
    K = np.dot(np.dot(p_pred,  M.T), np.linalg.inv(S))
    if((k==4)& ((fault==1) & (rand2>= 0.5))):
      a=random.choice(random.choice(K))
      andis=np.where(K == a)
      andis=np.array(andis)
      a1=andis[0]
      b=andis[1]
      print("k_a",a)
      K[a1[0]][b[0]]=single_bit_flip_fault(a)

    if((k==4)& ((fault==2) & (rand2>= 0.5))):
      a=random.choice(random.choice(K))
      andis=np.where(K == a)
      andis=np.array(andis)
      a1=andis[0]
      b=andis[1]
      print("k_a",a)
      K[a1[0]][b[0]]=Double_bit_flip_fault(a)

    if((k==4)& ((fault==3) & (rand2>= 0.5))):
      a=random.choice(random.choice(K))
      andis=np.where(K == a)
      andis=np.array(andis)
      a1=andis[0]
      b=andis[1]
      print("k_a",a)
      K[a1[0]][b[0]]=Zeero_all_bit_fault(a)
    P=p_pred -(np.dot(np.dot(K, M), p_pred))
    Xk=np.dot(phi, Xk_prev) + np.dot(K,z-np.dot(np.dot(M, phi), Xk_prev))
    if(((k==4))& ((fault==1) & (rand3>= 0.5))):
      a=random.choice(Xk)
      andis=np.where(Xk == a)
      andis=np.array(andis)
      a1=andis[0]
      print("xk-a",a)
      Xk[a1[0]]=single_bit_flip_fault(a)

    if(((k==4))& ((fault==3) & (rand3>= 0.5))):
      a=random.choice(Xk)
      andis=np.where(Xk == a)
      andis=np.array(andis)
      a1=andis[0]
      print("xk-a",a)
      Xk[a1[0]]=Zeero_all_bit_fault(a)  
    if(((k==4))& ((fault==2) & (rand3>= 0.5))):
      a=random.choice(Xk)
      andis=np.where(Xk == a)
      andis=np.array(andis)
      a1=andis[0]
      print("xk-a",a)
      Xk[a1[0]]=Double_bit_flip_fault(a)  
    Xk_buffer.append(Xk)
    Xk_prev=Xk

  plt.plot(range(len(z1)), z1, label = 'noise measurment')
  plt.plot(range(len(Xtrue)), Xtrue, label = 'true measurment')
  Xk_buffer=np.array(Xk_buffer)
  plt.plot(range(len(Xk_buffer)),Xk_buffer[:, 0], label = 'kalman predict')#mehvare x=time mehvare y= makan 
  plt.savefig("correct.jpg")
  plt.legend()
  plt.show()

def single_bit_flip_fault(value): # single bit fault for run time fault inject
  binarydata=float2bin(value)
  random_index=random.randrange(len(binarydata)-1)
  l_bin=list(binarydata)
  if(l_bin[random_index]=="0"):
    l_bin[random_index]="1"
  else:
    l_bin[random_index]="0"
  value="".join(l_bin)
  value=bin2float(value)
  return float(value)
 
def Double_bit_flip_fault(val):# doble bit  fault for runtime inject fault
  binarydata=float2bin(val)
  random_index1=random.randrange(len(binarydata)-1)
  random_index2=random.randrange(len(binarydata)-1)
  while(random_index2==random_index1):
    random_index2=random.randrange(len(binarydata)-1)
    if(random_index2!=random_index1):
      break
  l_bin=list(binarydata)
  if(l_bin[random_index1]=="0"):
    l_bin[random_index1]="1"
  else:
    l_bin[random_index1]="0"

  if(l_bin[random_index2]=="0"):
    l_bin[random_index2]="1"
  else:
    l_bin[random_index2]="0"
  val="".join(l_bin)
  val=bin2float(val)
  return float(val)

def Zeero_all_bit_fault(value): # zero all bit for runtime inject fault
  binarydata=float2bin(value)
  l_bin=""
  for i in range(len(binarydata)):
   l_bin+="0"
  value=bin2float(l_bin)
  return float(value)
   
def add_line_faulty(): # add line  instruction for compile time inject fault
  f = open("add_line_faulty.py", "w")
  with open("filter.py") as v:
      lines = v.readlines()
  count = 0
  for line in lines:
    rand = random.random()
  
    if((line.find("for k in range(nsample)")!=-1) or (line.find("for i in range(nsample)")!=-1)):
      f.write(line)
      if(rand<=0.5):
        f.write("    k+=1\n")
      else:
        f.write("    k-=1\n")
    elif(line.find("correct")!=-1):
      line=line.replace("correct", "add_line_faulty")
      f.write(line)
    else:
      f.write(line)
  f.close()
  v.close()
  !python add_line_faulty.py

def change_operand_fault(): # change operand for compile time fault injection
  f = open("operand_faulty.py", "w")
  with open("filter.py") as v:
      lines = v.readlines()
  count = 0
  for line in lines:
    rand = random.random()
  
  
    if((rand<=0.5) & (line.find("+")!=-1)&(line.find("z=10*t[k]+ x0 +noise[k]")==-1)&(line.find("Xtrue=x0+t*vtrue")==-1)):
        line=line.replace("+", "-")
        f.write(line)
    elif((rand<=0.5) & (line.find("-")!=-1)&(line.find("z=10*t[k]+ x0 +noise[k]")==-1)&(line.find("Xtrue=x0+t*vtrue")==-1)):
        line=line.replace("-", "+")
        f.write(line)
    elif(line.find("correct")!=-1):
        line=line.replace("correct", "operand_faulty")
        f.write(line)
    else:
      f.write(line)
  f.close()
  v.close()
  !python operand_faulty.py

if __name__ == '__main__':
  #single_bit_flip=1
  #double_bit_flip_fault=2
  #zero_all_bit_fault=3
  #add_line=4
  #change_operand=5
  fault = input("Enter your number for inject fault\n1=single bit flip\n2=double bit flip\n3=zero all bit fault\n4=add_line\n5= change_operand: ")

  fault=int(fault)
  if(fault==0):
    run_time_faulty_kalman(0)
  if(fault==1):
    run_time_faulty_kalman(1)
  if(fault==2):
    run_time_faulty_kalman(2)
  if(fault==3):
    run_time_faulty_kalman(3)
  if(fault==4):
    add_line_faulty()
  if(fault==5):
    change_operand_fault()

   

 
 