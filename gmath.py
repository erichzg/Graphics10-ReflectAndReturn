import math
from display import *

AMBIENT = 0
DIFFUSE = 1
SPECULAR = 2
LOCATION = 0
COLOR = 1
SPECULAR_EXP = 4

#lighting functions
def get_lighting(normal, view, ambient, light, areflect, dreflect, sreflect ):
    color = [0, 0, 0]
    amb = calculate_ambient(ambient, areflect)
    dif = calculate_diffuse(light, dreflect, normal)
    spec = calculate_specular(light, sreflect, view, normal)
    for index in range(len(color)):
        color[index] = amb[index] + dif[index] + spec[index]
    return limit_color(color)

def calculate_ambient(alight, areflect):
    ambient_color = [0, 0, 0]
    for index in range(len(ambient_color)):
        ambient_color[index] = alight[index] * areflect[index]
    return limit_color(ambient_color)
        

def calculate_diffuse(light, dreflect, normal):
    diffuse_color = [0, 0, 0]
    nHatDotLHat = dot_product(normalize(light[0]), normalize(normal))
    for index in range(len(diffuse_color)):
        diffuse_color[index] = light[1][index] * dreflect[index] * nHatDotLHat
    return limit_color(diffuse_color)

def calculate_specular(light, sreflect, view, normal):
    specular_color = [0, 0, 0]
    rHat = [0, 0, 0]
    normalizedLight = normalize(light[0])
    normalizedNormal = normalize(normal)
    nHatDotLHat = dot_product(normalizedLight, normalizedNormal)
    for index in range(len(rHat)):
        rHat[index] = 2 * nHatDotLHat * normalizedNormal[index] - normalizedLight[index]
    constantMult = (dot_product(rHat, normalize(view))) ** 15
    for index in range(len(specular_color)):
        specular_color[index] = light[1][index] * sreflect[index] * constantMult
    return limit_color(specular_color)
        

def limit_color(color):
    for index in range(len(color)):
        color[index] = int(color[index])
        if color[index] < 0:
            color[index] = 0
        elif color[index] > 255:
            color[index] = 255
    return color


#vector functions
def normalize(vector):
    magnitude = 0
    for val in vector:
        magnitude += val ** 2
    magnitude = magnitude ** 0.5
    for index in range(len(vector)):
        vector[index] /= magnitude
    return vector

def dot_product(a, b):
    retVal = 0
    for index in range(len(a)):
        retVal += a[index] * b[index]
    return retVal

def calculate_normal(polygons, i):

    A = [0, 0, 0]
    B = [0, 0, 0]
    N = [0, 0, 0]

    A[0] = polygons[i+1][0] - polygons[i][0]
    A[1] = polygons[i+1][1] - polygons[i][1]
    A[2] = polygons[i+1][2] - polygons[i][2]

    B[0] = polygons[i+2][0] - polygons[i][0]
    B[1] = polygons[i+2][1] - polygons[i][1]
    B[2] = polygons[i+2][2] - polygons[i][2]

    N[0] = A[1] * B[2] - A[2] * B[1]
    N[1] = A[2] * B[0] - A[0] * B[2]
    N[2] = A[0] * B[1] - A[1] * B[0]

    return N
