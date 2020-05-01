import myModule
import myModule as m 
from myModule import greeting # import part of module
import platform # build-in modules

myModule.greeting()
m.greeting()
greeting()

print(platform.system())
# print(dir(platform)) # list of all function names or variables in module

