import numpy
import pylab
from math import pi, sqrt, sin, cos
from mpl_toolkits.mplot3d import Axes3D


def polar_to_cartesian(vCoordinate):
    sR = vCoordinate[0]
    sTheta = vCoordinate[1]
    sX = sR*cos(sTheta)
    sY = sR*sin(sTheta)
    return (sX, sY)


def cylindrical_to_cartesian(vCoordinate):
    sR = vCoordinate[0]
    sPhi = vCoordinate[1]
    sZ = vCoordinate[2]
    sX = sR*cos(sPhi)
    sY = sR*sin(sPhi)
    sZ = sZ
    return (sX, sY, sZ)


def spherical_to_cartesian(vCoordinate):
    sR = vCoordinate[0]
    sPhi = vCoordinate[1]
    sTheta = vCoordinate[2]
    sX = sR*sin(sTheta)*cos(sPhi)
    sY = sR*sin(sTheta)*sin(sPhi)
    sZ = sR*cos(sTheta)
    return (sX, sY, sZ)
