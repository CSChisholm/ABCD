#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 17:54:39 2021

@author: craig
"""

import numpy as np
import matplotlib.pyplot as plt

class Beam:
    '''
    Implements a Gaussian beam with ABCD optics
    '''
    def __init__(self,z0,w0,wl,focus):
        '''

        Parameters
        ----------
        z0 : float
            Starting position.
        w0 : float
            Beam waist at focus.
        wl : float
            wavelength.
        focus : float
            Position of focus.

        Returns
        -------
        None.

        '''
        self.z = z0 #Current position along propagation axis, um
        self.wl = wl #wavelength in um
        self.w0 = w0 #Beam waist at current position, um
        self.R0 = np.inf #Radius of curvature at current position, um
        self.q = self.complexq(self.R0,self.w0) #Complex q parameter at z = 0
        self.propagate(-focus) #Set focus
        self.z=z0
    
    def RayleighRange(self,ww):
        '''Calculates the Rayleigh range for a Gaussian beam with beam waist ww'''
        return np.pi*(ww**2)/self.wl
    
    def complexq(self,RR,ww):
        '''Calculates complex-q parameter'''
        return 1/(1/RR + 1j/self.RayleighRange(ww))

    def ABCDpropagation(self,dist):
        '''Returns the ABCD parameters for propagation by distance dist'''
        return [1,dist,0,1]
    
    def ABCDlens(self,focal):
        '''Returns the ABCD parameters for a thin lens with focal length focal'''
        return [1,0,-1/focal,1]
    
    def MakeMatrix(self,*params):
        '''Constructor for ABCD matrix'''
        A = params[0]
        B = params[1]
        C = params[2]
        D = params[3]
        return np.array([[A,B],[C,D]])
    
    def propagate(self,dist):
        '''Propagates the beam'''
        self.ABCD(self.MakeMatrix(*self.ABCDpropagation(dist)))
        self.z+=dist
        return
    
    def passthroughlens(self,focal):
        '''Passes the beam through a thin lens'''
        self.ABCD(self.MakeMatrix(*self.ABCDlens(focal)))
        return
    
    def passthroughthicklens(self,lens):
        self.ABCD(lens.MakeMatrix())
        self.z+=lens.thickness
    
    def ABCD(self,mat):
        '''Applies ABCD matrix'''
        vec = mat@np.array([[self.q],[1]])
        self.q = vec[0,0]/vec[1,0]
        return
    
    def setfocus(self,focus):
        '''Set the focus a distance focus ahead of the current position'''
        zcurrent = self.z
        self.propagate(-focus)
        self.z = zcurrent
        return
    
    def radius(self):
        '''Calculates the radius of the beam at the current point'''
        return np.sqrt((self.wl/np.pi)/(1/self.q).imag)
    
    def curvature(self):
        '''Calculates the radius of curvature of the wavefront at the current point'''
        return 1/((1/self.q).real)

class Lens:
    '''Implements a thin lens'''
    def __init__(self):
        self.location = 0 #Position of the lens in um
        self.focal = np.inf #Focal lenght of the lens in um
        self.diameter = 50e3 #lens diameter, um
    
    def plot(self,hh):
        '''Plots a line with height hh to represent a lens'''
        xx = [self.location*1e-3]*2
        yy = [-hh,hh]
        plt.plot(xx,yy,c='C1')
        return

class ThickLens:
    '''Implements a thick lens'''
    def __init__(self):
        self.location = 0 #Position of first surface, um
        self.R1 = np.inf #Radius of first surface, um
        self.R2 = np.inf #Radius of second surface, um
        self.thickness = 1 #Thickness of lens, um
        self.diameter = 50e3 #lens diameter, um
        self.n = 1 #Refractive index of material
    
    def MakeMatrix(self):
        f2 = self.R1*self.n/(self.n-1)
        f3 = self.R2/(1-self.n)
        M1 = np.array([[1,0],[-1/f2,1/self.n]])
        M2 = np.array([[1,self.thickness],[0,1]])
        M3 = np.array([[1,0],[-1/f3,self.n]])
        return M3@M2@M1
    
    def plot(self,hh):
        '''Draws the two surfaces of the thick lens'''
        c1 = 1/self.R1
        c2 = 1/self.R2
        xvals = np.linspace(-hh,hh,100)
        zvals = self.location + c1*np.power(xvals,2)/(1+np.sqrt(1-(c1**2)*np.power(xvals,2)))
        plt.plot(zvals*1e-3,xvals,c='C1')
        zvals = self.location + self.thickness + c2*np.power(xvals,2)/(1+np.sqrt(1-(c2**2)*np.power(xvals,2)))
        plt.plot(zvals*1e-3,xvals,c='C1')
        return

#Default parameters
z0 = 0
w0 = 50
wl = 1.064
focus = 50e3
propagationdistance = 200e3
lenses = []
lens0 = Lens()
lens0.location = 100e3
lens0.focal = 50e3
lenses.append(lens0)
lens1 = Lens()
lens1.location = 150e3
lens1.focal = 50e3
lenses.append(lens1)

def main(z0,w0,wl,focus,propagationdistance,lenses=None):
    '''Runs the propagation'''
    plt.close("all")
    if (lenses is None):
        lenses = []
    
    #initialise beam
    beam = Beam(z0,w0,wl,focus)
    
    #Enforce that the first lens is at a position greater than or equal to the start point and that lenses are ordered
    if any([not(isinstance(lens,Lens) or isinstance(lens,ThickLens)) for lens in lenses]):
        raise TypeError('All elements of lenses must be Lens or ThickLens class')
    if (len(lenses)):
        lenses = sorted(lenses,key=lambda x: x.location)
        if (lenses[0].location<beam.z):
            shiftdistance = beam.z-lenses[0]
            for lens in lenses:
                lens.location+=shiftdistance
    
    #Perform propagation
    zArray = np.linspace(beam.z,beam.z+propagationdistance,101)
    waist = np.zeros(len(zArray))
    skipIters = []
    for itr, zz in enumerate(zArray):
        if (itr in skipIters):
            #Inside a thick lens
            continue
        currentpoint = beam.z
        nextpoint = zz
        #Check for lenses within the propagation space
        nextLenses = [lens for lens in lenses if currentpoint<=lens.location<nextpoint]
        for lens in nextLenses:
            if (lens.location<beam.z):
                raise Exception('Lens collision error')
            beam.propagate(lens.location-currentpoint)
            if isinstance(lens,Lens):
                beam.passthroughlens(lens.focal)
                currentpoint = beam.z
            else:
                #This is a thick lens
                if (beam.z==zz):
                    waist[itr] = beam.radius()
                beam.passthroughthicklens(lens)
                skipIters = np.where((zArray>=zz) & (zArray<beam.z))[0]
                waist[skipIters] = np.nan
                currentpoint=beam.z
        if (nextpoint>=currentpoint):
            beam.propagate(nextpoint-currentpoint)
            waist[itr] = beam.radius()
    
    #Plot result
    plt.figure()
    plt.plot(zArray*1e-3,waist,c='C0')
    plt.plot(zArray*1e-3,-waist,c='C0')
    for lens in lenses:
        lens.plot(lens.diameter/2)
    plt.xlabel('$z$ (mm)')
    plt.ylabel('$w$ ($\mu$m)')
    return zArray, waist, beam

if (__name__=='__main__'):
    main(z0,w0,wl,focus,propagationdistance,lenses)
