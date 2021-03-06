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
    '''
    Calculates the non linear energy of the signal.
    '''
    size=len(frame)
    te=np.zeros(size-2)
    te[0]=0
    for i in range(1,size-1,1):
        te[i]=frame[i]*frame[i]-frame[i-1]*frame[i+1]
    return(te)


def energy(frame,Fs):
    '''
    Calcultes the net energy of the signal.
    '''
    return(np.log10(np.sum(frame*frame)))



