#Author: Anish Reddy
#Date : 21-10-2020
#Description : Verify properties of a one qubit active rotation operation.


import math
import cmath
import numpy as np


i = 0+1j                                                #Initialize i as a complex number
def Program():                                          #Function to test the Identity
    print("\n")
    print("Enter the vector 'n' about which the state gets rotated") #Vector n is the axis about which the state is rotated in the Bloch Sphere
    nx = float(input("Enter nx "))                      #Component of n in x direction
    ny = float(input("Enter ny "))                      #Component of n in y direction
    nz = float(input("Enter nz "))                      #Component of n in z direction
    theta = float(input("Enter the angle of rotation(Theta) in radians "))  #Angle of rotation Theta that the state is rotated by

    print("\n")
    print("\n")
    nmod = math.sqrt(nx**2 + ny**2 +nz**2)      #Modulus of Vector n
    nx = nx/nmod                                #Normalize n to get components of the unit vector in the direction of n i.e ncap
    ny = ny/nmod
    nz = nz/nmod

    a = -theta/2                                #Value to be used in caluculation

    print("On Computing the Dot Product of the unit vector of 'n' with the Pauli Vector, We get the following Matrix: ")
    print("\n")
    dotp = np.array([[nz,nx - i*ny] , [nx + i*ny, -nz]]) #The Pauli Matrices are multiplied with their respective components of ncap to produce this 2x2 Matrix ncap.Signma
    print(dotp)
    print("\n")
    print("\n")
    print("The Matrix Rn(theta) is calculated using the above dot product, it is shown here: ") #Rn(Theta) is calculated by breaking the exponent to sin and cos functions
    print("\n")

    sinmat = i*dotp*math.sin(a)                         #sin component of Rn(theta)
    cosmat = (math.cos(a))*np.array([[1,0] , [0,1]])    #cos component of Rn(theta)

    sinmat1 = i*dotp*math.sin(-a)                       #sin component of Rn(-theta)
    cosmat1 = (math.cos(-a))*np.array([[1,0] , [0,1]])  #cos component of Rn(-theta)

    Rtheta = sinmat + cosmat                            #Produce Rn(theta)
    print(Rtheta)
    print("\n")
    print("\n")
    print("From this matrix we can subsequently calculate the following: ")
    print("\n")
    print("\n")

    Rtran = Rtheta.conj().T                             #Conjugate Transpose of R(theta)
    Rminus = sinmat1 + cosmat1                          #Rn(-Theta)
    Rinv = np.linalg.inv(Rtheta)                        #Inverse of Rn(theta)

    print("Hermitian Transpose of Rn(Theta): ")
    print(Rtran)
    print("\n")
    print("\n")
    print("Matrix of Rn(-Theta): ")
    print(Rminus)
    print("\n")
    print("\n")
    print("Inverse of Matrix of Rn(Theta): ")
    print(Rinv)
    print("\n")
    print("\n")


    print("We Observe that the above 3 matrices are the same and hence The Identity is Verified") #The 3 matrices are Equivalent, Hence Proven
    print("\n")
def main():
    Program()

    while(1):
        x = str(input("To run the program again with different parameters press '0', else press any other key to terminate."))
        if(x == "0"):
            Program()
        else:
            break
main()
