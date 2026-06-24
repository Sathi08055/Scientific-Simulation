import torch
import numpy as np
import matplotlib.pyplot as plt
from  icecream import ic


nMax=50
alpha=1j+2
device="cuda"
theta=45 # Half
coherentState= torch.math.exp((np.abs(alpha)**2)/2)*torch.tensor([pow(alpha,n)/torch.math.sqrt(torch.math.factorial(n)) for n in range(nMax+1)],device=device,dtype=torch.complex128)
#coherentState=coherentState.reshape(shape=(nMax+1,1))

def fockState(n,nMax=nMax,device=device):
    return torch.tensor([1 if i==n else 0 for i in range (nMax+1) ],device=device,dtype=torch.complex128)


# Inputs:
path1=coherentState
path2=fockState(0)
ic(path1.size())
p12=torch.kron(path1,path2)
ic(p12.dtype)

def aOperator(nMax=nMax):
    coEffs=torch.tensor([np.sqrt(n+1) for n in range(nMax)],device=device)
    return torch.diag(coEffs,diagonal=-1)
aOp=aOperator()

tensorProductsize=aOp.size()
a1=torch.kron(aOp,torch.eye(nMax+1,device=device))
a2=torch.kron(torch.eye(nMax+1,device=device),aOp)

U=torch.matrix_exp(theta*1j*(a1.T@a2 +a1@a2.T))
ic(U.dtype)
out=U@p12
out=out.reshape(shape=((nMax+1)**2,1))
p=torch.abs(coherentState)
theory=torch.kron(coherentState/np.sqrt(2),coherentState/np.sqrt(2)*1j)
ic(theory.shape)
ic(torch.abs(out)**2-torch.abs(theory)**2)
a=1 #ignore: tg