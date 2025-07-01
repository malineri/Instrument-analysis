import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Create function reading from file
def Data_values(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    #extract important lines in document:    
    data_lines = lines[:]
    z_imag = []
    z_real = []
    
    for line in data_lines:
        # Split the line into components (tab-separated)
        parts = line.split()
        z_imag.append(float(parts[1])) #imaginary values
        z_real.append(float(parts[0])) #real values
        
   
    return z_imag, z_real



#Theoretical values:
X1, R1 = Data_values("C1.txt")
X2, R2 = Data_values("C2.txt")
X3, R3 = Data_values("C3.txt")
X4, R4 = Data_values("C4.txt")
X5, R5 = Data_values("C5.txt")



def SBF7_values(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    #extract important lines in document:    
    data_lines = lines[13:]
    freq = []
    z_imag = []
    z_real = []
    
    for line in data_lines:
        # Split the line into components (tab-separated)
        parts = line.split(",")
        freq.append(float(parts[0]))
        z_real.append(float(parts[1])) #real values
        z_imag.append(float(parts[2])) #imaginary values
    
        
        
   
    return z_imag, z_real


X1_SBF7, R1_SBF7 = SBF7_values("C1.mfu")
X2_SBF7, R2_SBF7 = SBF7_values("C2.mfu")
X3_SBF7, R3_SBF7 = SBF7_values("C3.mfu")
X4_SBF7, R4_SBF7 = SBF7_values("C4.mfu")
X5_SBF7, R5_SBF7 = SBF7_values("C5.mfu")



def Zurich_values(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    #extract important lines in document:    
    data_lines = lines[1:]
    freq = []
    z_imag = []
    z_real = []
    
    for line in data_lines:
        # Split the line into components (tab-separated)
        parts = line.split()
        freq.append(float(parts[0]))
        z_imag.append(-1*(float(parts[5]))) #imaginary values
        z_real.append((float(parts[4]))) #real values
    
        
        
   
    return z_imag, z_real


X1_Z, R1_Z = Zurich_values("C1_Z.txt")
X2_Z, R2_Z = Zurich_values("C2_Z.txt")
X3_Z, R3_Z = Zurich_values("C3_Z.txt")
X4_Z, R4_Z = Zurich_values("C4_Z.txt")
X5_Z, R5_Z = Zurich_values("C5_Z.txt")





plt.title("Circuit 1 - Bl4ack Capacitor")
plt.plot(R1, X1, label='Theoretical')
plt.plot(R1_SBF7, X1_SBF7, label='SBF7')
plt.plot(R1_Z, X1_Z, label='Zurich')
plt.ylabel(r'Reactance [$\Omega$]')
plt.xlabel(r'Resistance [$\Omega$]')
plt.legend()
plt.savefig("C1_comparison.png")
plt.show()
   


plt.title("Circuit 2 - Brown Capacitor")
plt.plot(R2, X2, label='Theoretical')
plt.plot(R2_SBF7, X2_SBF7, label='SBF7')
plt.plot(R2_Z, X2_Z, label='Zurich')
plt.ylabel(r'Reactance [$\Omega$]')
plt.xlabel(r'Resistance [$\Omega$]')
plt.legend()
plt.savefig("C2_comparison.png")
plt.show()


plt.title("Circuit 3 - Green Capacitor")
plt.plot(R3, X3, label='Theoretical')
plt.plot(R3_SBF7, X3_SBF7, label='SBF7')
plt.plot(R3_Z, X3_Z, label='Zurich')
plt.xlabel(r'Reactance [$\Omega$]')
plt.ylabel(r'Resistance [$\Omega$]')
plt.legend()
plt.savefig("C3_comparison.png")
plt.show()

plt.title("Circuit 4 - Yellow Capacitor")
plt.plot(R4, X4, label='Theoretical')
plt.plot(R4_SBF7, X4_SBF7, label='SBF7')
plt.plot(R4_Z, X4_Z, label='Zurich')
plt.ylabel(r'Reactance [$\Omega$]')
plt.xlabel(r'Resistance [$\Omega$]')
plt.legend()
plt.savefig("C4_comparison.png")
plt.show()

plt.title("Circuit 5 - Red Capacitor")
plt.plot(R5, X5, label='Theoretical')
plt.plot(R5_SBF7, X5_SBF7, label='SBF7')
plt.plot(R5_Z, X5_Z, label='Zurich')
plt.ylabel(r'Reactance [$\Omega$]')
plt.xlabel(r'Resistance [$\Omega$]')
plt.legend()
plt.savefig("C5_comparison.png")
plt.show()
    



