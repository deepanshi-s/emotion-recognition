#NOTE: Assume that the frame received by the function is already windowed
import numpy as np
import scipy.signal as sig
import scipy.io.wavfile as wav

def pitch(frame,Fs):
    '''
    A short description about the function
    '''


def zcr(frame,Fs):
    '''
    A short description about the function
    '''


def teo(frame,Fs):
    size=len(frame)
    te=np.zeros(size-2)
    te[0]=0
    for i in range(1,size-1,1):
        te[i]=frame[i]*frame[i]-frame[i-1]*frame[i+1]
    return(te)
    '''
    calculates the non linear energy of the signal.
    '''


def energy(frame,Fs):
    size=len(frame)
    E=0
    for i in range (0,size,1):
        E=E+frame[i]*frame[i]
    E1=np.log10(E)
    return(E1)
    '''
    calcultes the net energy of the signal.
    '''



