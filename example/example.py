"""
    Projekt IVS 2019

    Tým: /(o_o)/
    
    Autoři:
        - Martin Krbila 
	    - Jirka Hába
	    - Artsiom Luhin
	    - Nikolaj Vorobiev
"""

##
#   @file example.py
#   @author Martin Krbila
#   @date 13.3.2019
#
#   @brief Code and documentation example
#
#   This is a long description of this file.


##
#   @brief Simple class
#
#   This is detailed description of this class.
#   @todo Create some new method.
#   @bug Attribute x should be equal to 16
class Test():

    ##
    #   @brief Constructor
    #
    #   Constructs object Test.
    #   @param dx Value of attribute x
    def __init__(self,dx=4):

        
         
        ## Attribute x
        #
        #   Longer description
        self.x=dx**1 
        
       
        ## Another attribute
        #
        #   Longer description
        self.y="pokus"

        
        ## Next attribute
        #
        #   Longer description        
        self.z=3.14


    ##
    #   @brief Really interesting method
    #
    #   This method is very complex and cannot be simply explained.
    #   @param abc Number added to the result
    #   @return Sum of attributes x,z and parameter abc
    def add_xz(self,abc):

        return self.x+self.z+abc

if __name__=="__main__":
    import doctest
    doctest.testfile("test.txt")

