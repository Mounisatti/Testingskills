import Library.CommonModule

objA = Library.CommonModule.A()
objA.CommonA()

#This is from module import class
from Library.CommonModule import D

objD=D()
objD.CommonD()

#This for another import code

from Pages.Princes.Joy import C
obj = C()
obj.Mytesting()

