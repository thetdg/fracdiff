"""
This programme provides easily accessible and vectorized 
unit step, ramp and parabolic functions
Created by Tanmoy Dasgupta
"""
from numpy import array

#unit step function
def u(x):
    x = array(x).astype('float64')
    step_out = (x >= 0).astype('float64')
    return step_out

#unit ramp function
def r(x):
    x = array(x).astype('float64')
    ramp_out = x * (x >= 0).astype('float64')
    return ramp_out

#unit parabolic function
def p(x):
    x = array(x).astype('float64')
    parabolic_out = x * x * (x >= 0).astype('float64')
    return parabolic_out

#Dirac delta function
def d(x, width=0.01):
    x = array(x).astype('float64')
    delta_out = (x > - width).astype('float64') + (x < width).astype('float64')
    return delta_out