import re
import time
import datetime
import ctypes
import random
import os
import sys

import numpy as np
import matplotlib.pyplot as plt

def kalman():
  nsample=100
  t = np.linspace(0, 10, 100)
  dt = 1.0/10
  x0=0
  vtrue= 10
  Xtrue=x0+t*vtrue
  phi = np.array([[1, dt], [0, 1]])
  Q = np.array([[0, 0], [0, 0]])
  P=np.array([[1,0],[0,1]])
  M=np.array([[1,0]]) 
  R=np.array([1])
  Xk_prev=np.array([0,0.5]) 
  Xk=[]
  z1=[]
  Xk_buffer=[]
  noise=np.random.normal(0, 10,100)
  for k in range(nsample) : # noise measurement
    z=10*t[k]+ x0 +noise[k] 
    z1.append(z)
    p_pred=np.dot(np.dot(phi, P), phi.T) + Q #Predicted (a priori) state estimate
    S=np.dot(np.dot(M, p_pred), M.T) + R #Innovation (or pre-fit residual) covariance
    K = np.dot(np.dot(p_pred,  M.T), np.linalg.inv(S))#Optimal Kalman gain
    P=p_pred -(np.dot(np.dot(K, M), p_pred)) #Updated (a posteriori) estimate
    Xk=np.dot(phi, Xk_prev) + np.dot(K,z-np.dot(np.dot(M, phi), Xk_prev)) ##Updated (a posteriori) state estimate
    Xk_buffer.append(Xk)
    Xk_prev=Xk



  plt.plot(range(len(z1)), z1, label = 'noise measurment')  #plot output
  plt.plot(range(len(Xtrue)), Xtrue, label = 'true measurment')
  Xk_buffer=np.array(Xk_buffer)
  plt.plot(range(len(Xk_buffer)),Xk_buffer[:, 0], label = 'kalman predict')#mehvare x=time mehvare y= makan 
  plt.savefig("correct.jpg")

if __name__ == '__main__':
  kalman()
