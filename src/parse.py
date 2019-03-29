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
#   @file parse.py
#   @author Martin Krbila
#   @date 22.3.2019
#
#   @brief Parser prototype
#
#   Contains proposed structure for parser of mathematical expression.

from enum import Enum
import math

##
#   @brief Enumeration of various token types
#
#   This class contains basic types of tokens found in mathematical expressions
class Token_type(Enum):
    ERR=-1 # Error
    NUM=0  # Number
    LB=1   # Left bracket
    RB=2   # Right bracket
    OP=3   # Binary operator
    FUNC=4 # Function
    COM=5  # Comma

##
#   @brief Token
#
#   This class represents token in mathematical expression.
#   Specific tokens inherit this class.
class Token:

    ##
    #   @brief Constructor
    #
    #   Constructs object Token.
    def __init__(self):

        ## Number of parameters to evaluate
        self.param_no=0

        ## Priority of the operation
        self.priority=0

        ## Is associative from left to right?
        self.l_asoc=True

        ## Defines type of token
        self.t_type=Token_type.ERR

    ##
    #   @brief Get type of token
    #
    #   @return Token type
    def get_type(self):
        return self.t_type

    ##
    #   @brief Get priority of token
    #
    #   @return Token priority
    def get_priority(self):
        return self.priority

    ##
    #   @brief Get associativity of token
    #
    #   @return Left to right associativity
    def get_asociativity(self):
        return self.l_asoc

    ##
    #   @brief Get number of required parameters
    #
    #   @return Parameter count
    def get_param_cnt(self):
        return self.param_no

    ##
    #   @brief Convert to string
    #
    #   @return String representation of the token
    def __str__(self):
        return "?"

    ##
    #   @brief Evaluate token
    #
    #   @param params List of parameters
    #   @return Floating point value of token
    def eval(self,params):
        return 0.0

##
#   @brief Left bracket
#
#   This class represents Left bracket of mathematical expression.
class LBracket(Token):
    def __init__(self):
        super().__init__()
        self.t_type=Token_type.LB

    def __str__(self):
        return "("

    def eval(self,params):
        return 0

##
#   @brief Comma
#
#   This class represents separator of function arguments: ','  .
class Comma(Token):
    def __init__(self):
        super().__init__()
        self.t_type=Token_type.COM

    def __str__(self):
        return ","

    def eval(self,params):
        return 0


##
#   @brief Right bracket
#
#   This class represents Right bracket of mathematical expression.
class RBracket(Token):
    def __init__(self):
        super().__init__()
        self.t_type=Token_type.RB

    def __str__(self):
        return ")"

    def eval(self,params):
        return 0

##
#   @brief Unary minus
#
#   This class represents unary minus.
class Negate(Token):
    def __init__(self):
        super().__init__()
        self.param_no=1
        self.priority=99
        self.t_type=Token_type.FUNC

    def __str__(self):
        return "neg"

    def eval(self,params):
        return -(params[0])

##
#   @brief Number
#
#   This class represents floating point number.
class Number(Token):
    def __init__(self,value):
        super().__init__()
        self.value=value
        self.t_type=Token_type.NUM

    def __str__(self):
        return str(self.value)

    def eval(self,params):
        return self.value

##
#   @brief Binary operator
#
#   This class represents binary operator.
class Bin_op(Token):
    def __init__(self):
        super().__init__()
        self.param_no=2
        self.priority=1
        self.t_type=Token_type.OP

    def __str__(self):
        return "?"

##
#   @brief Function
#
#   This class represents function.
class Function(Token):
    def __init__(self):
        super().__init__()
        self.param_no=1
        self.priority=99
        self.t_type=Token_type.FUNC



class Plus(Bin_op):
    def __init__(self):
        super().__init__()
        self.priority=1

    def __str__(self):
        return "+"

    def eval(self,params):
        return params[0]+params[1]

class Minus(Bin_op):
    def __init__(self):
        super().__init__()
        self.priority=1

    def __str__(self):
        return "-"

    def eval(self,params):
        return params[0]-params[1]

class Multiply(Bin_op):
    def __init__(self):
        super().__init__()
        self.priority=2

    def __str__(self):
        return "*"

    def eval(self,params):
        return params[0]*params[1]

class Divide(Bin_op):
    def __init__(self):
        super().__init__()
        self.priority=2

    def __str__(self):
        return "/"

    def eval(self,params):
        return params[0]/params[1]


class Square_root(Function):
    def __init__(self):
        super().__init__()
        self.param_no=1

    def __str__(self):
        return "sqrt"

    def eval(self,params):
        return math.sqrt(params[0])


##
#   @brief Parser
#
#   Parser of mathematical expressions in form of strings
class Parser():

    ##
    #   @brief Constructor
    #
    #   Initializes parser with basic operations
    def __init__(self):
        self.init_basic_ops()

    ##
    #   @brief Clear operators
    #
    #   Removes all operators registered in parser
    def clear_ops(self):
        self.func_table={}
        self.operator_table={}

    ##
    #   @brief Initialize operators
    #
    #   Registers basic operators
    def init_basic_ops(self):
        self.func_table={
            "sqrt":Square_root()
        }

        self.operator_table={
            "+":Plus(),
            "-":Minus(),
            "*":Multiply(),
            "/":Divide(),
        }

    ##
    #   @brief Add new operator
    #
    #   Insert new operator.
    #   @param name Text representation of operator used in lexical analysis
    #   @param op_object Object of class Bin_op representing behavior of this operator
    def add_operator(self,name,op_object):
        self.operator_table[name]=op_object

    ##
    #   @brief Add new function
    #
    #   Insert new function.
    #   @param name Text representation of function used in lexical analysis
    #   @param op_object Object of class Function representing behavior of this operator
    def add_function(self,name,op_object):
        self.func_table[name]=op_object

    ##
    #   @brief Lexical analysis
    #
    #   Perform lexical analysis on string and return list of tokens.
    #   @param expr String that contains mathematical expression.
    #   @return List of Token objects
    def lexer(self,expr):
        t_ary=[Number(1),Plus(),Number(2)]
        return t_ary

    ##
    #   @brief Syntax analysis
    #
    #   Perform syntax analysis using list of tokens.
    #   @param token_ary List of Token objects
    #   @return List of tokens in post-fix notation
    def shunting_yard(self,token_ary):
        ret=[Number(1),Number(2),Plus()]
        return ret

    ##
    #   @brief Semantic analysis
    #
    #   Perform final evaluation of the expression in post-fix notation.
    #   @param post_ary List of tokens in post-fix notation
    #   @return Numerical value of the expression
    def postfix_eval(self,post_ary):
        return 42.0

    ##
    #   @brief Parse expression
    #
    #   Parses mathematical expression in form of string and returns its numerical value.
    #   @param expr String that contains the expression
    #   @return Floating point value of the expression
    def parse(self,expr):
        tokens=self.lexer(expr)
        postfix=self.shunting_yard(tokens)
        return self.postfix_eval(postfix)

###############################
#
#   Entry point - tests
#
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests_operations.txt")
    doctest.testfile("tests_lexer.txt")
    doctest.testfile("tests_parser.txt")
    doctest.testfile("tests_semantics.txt")
    doctest.testfile("tests_complete_analysis.txt")
