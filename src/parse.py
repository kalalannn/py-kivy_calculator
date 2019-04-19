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
import re

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

class State(Enum):
    A_START = 0
    A_NEG = 1
    A_LBRACK = 2
    A_RBRACK = 3
    A_DIG = 4
    A_DIG_TEMP = 5
    A_FUNC = 6
    A_OP = 7
    A_BAD = 8

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


##
#   @brief Add
#
#   This class represents binary operator "+".
class Plus(Bin_op):
    def __init__(self):
        super().__init__()
        self.priority=1

    def __str__(self):
        return "+"

    def eval(self,params):
        return params[0]+params[1]

##
#   @brief Subtract
#
#   This class represents binary operator "-".
class Minus(Bin_op):
    def __init__(self):
        super().__init__()
        self.priority=1

    def __str__(self):
        return "-"

    def eval(self,params):
        return params[0]-params[1]

##
#   @brief Multiply
#
#   This class represents binary operator "*".
class Multiply(Bin_op):
    def __init__(self):
        super().__init__()
        self.priority=2

    def __str__(self):
        return "*"

    def eval(self,params):
        return params[0]*params[1]

##
#   @brief Divide
#
#   This class represents binary operator "/".
class Divide(Bin_op):
    def __init__(self):
        super().__init__()
        self.priority=2

    def __str__(self):
        return "/"

    def eval(self,params):
        return params[0]/params[1]


##
#   @brief Square root
#
#   This class represents function square root.
class Square_root(Function):
    def __init__(self):
        super().__init__()
        self.param_no=1

    def __str__(self):
        return "sqrt"

    def eval(self,params):
        return math.sqrt(params[0])

##
#   @brief Power
#
#   This class represents binary operator "^".
class Power(Bin_op):
    def __init__(self):
        super().__init__()
        self.priority=3
        self.l_asoc=False

    def __str__(self):
        return "^"

    def eval(self,params):
        return math.pow(params[0],params[1])

##
#   @brief Logarithm
#
#   This class represents function logarithm with base 10.
class Logarithm(Function):
    def __init__(self):
        super().__init__()
        self.param_no=1
    def __str__(self):
        return "log"
    def eval(self,params):
        return math.log10(params[0])

##
#   @brief Factorial
#
#   This class represents function factorial.
class Factorial(Function):
    def __init__(self):
        super().__init__()
        self.param_no=1
    def __str__(self):
        return "fact"
    def eval(self,params):
        return math.gamma(params[0])*params[0]

##
#   @brief Variable root
#
#   This class represents root function of variable base.
class Nroot(Function):
    def __init__(self):
        super().__init__()
        self.param_no=2
    def __str__(self):
        return "nroot"
    def eval(self,params):
        return pow(params[1],(1.0/params[0]))

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
        prev_state = State.A_START
        self.ind = 0
        token_arr = []
        expr = re.sub(r'\s', '', expr)
        expr += ':'

        def analyze():
            acc = 0
            state = State.A_START
            while (self.ind < len(expr)):
                if state == State.A_START:
                    if expr[self.ind] == '-':
                        state = State.A_NEG
                    elif expr[self.ind] == '(':
                        state = State.A_LBRACK
                    elif expr[self.ind] == ')':
                        state = State.A_RBRACK
                    elif expr[self.ind].isdigit() or expr[self.ind]==".":
                        acc = expr[self.ind]
                        state = State.A_DIG
                    elif expr[self.ind] in self.operator_table.keys():
                        state = State.A_OP
                        acc = expr[self.ind]
                    elif expr[self.ind].isalpha(): 
                        acc = expr[self.ind]
                        state = State.A_FUNC
                    else:
                        acc = expr[self.ind]
                        state = State.A_BAD
                elif state == State.A_NEG:
                    #self.ind -= 1
                    return Negate()
                elif state == State.A_LBRACK:
                    #self.ind -= 1
                    return LBracket()
                elif state == State.A_RBRACK:
                    #self.ind -= 1
                    return RBracket()
                elif state == State.A_DIG:
                    if (expr[self.ind].isdigit() or expr[self.ind]=="."):
                        acc += expr[self.ind]
                    else:
                        #self.ind -= 1
                        try:
                            acc=float(acc)
                        except:
                            raise SyntaxError("'"+acc+"' is not a number")
                        return Number(acc)
                elif state == State.A_BAD:
                    raise SyntaxError("unexpected symbol '"+acc+"'")
                elif state == State.A_OP:
                    return self.operator_table[acc]
                elif state == State.A_FUNC:
                    if (expr[self.ind].isalpha() or expr[self.ind]=="_" or expr[self.ind].isdigit()):
                        acc += expr[self.ind]
                    else:
                        if acc in self.func_table.keys():
                            #self.ind -= 1
                            return self.func_table[acc]
                        else:
                            raise SyntaxError("function '" + acc + "' is not defined")
                self.ind += 1

        while (self.ind < len(expr) - 1):
            token_arr.append(analyze()) 

        return token_arr

    ##
    #   @brief Syntax analysis
    #
    #   Perform syntax analysis using list of tokens.
    #   @param token_ary List of Token objects
    #   @return List of tokens in post-fix notation
    #   @throws SyntaxError
    def shunting_yard(self,token_ary):

        # Output queue
        ret=[]

        # Operator stack
        stack=[]

        # Loop over all tokens
        for t in token_ary:
            
            # Numbers:
            if t.get_type()==Token_type.NUM:
                # Insert numbers to the output queue
                ret.append(t)
                
            # Left brackets:
            elif t.get_type()==Token_type.LB:
                # Insert left brackets to the operator stack
                stack.append(t)

            # Right brackets:    
            elif t.get_type()==Token_type.RB:
                # Remove operators from stack and insert them to the output queue,
                # until left bracket is found.
                while stack and stack[-1].get_type()!=Token_type.LB:
                    ret.append(stack.pop())
                if not stack:
                    raise SyntaxError("missing left bracket")
                # Remove left bracket
                stack.pop()
                # Check if brackets follow after function call
                if stack and stack[-1].get_type()==Token_type.FUNC:
                    ret.append(stack.pop())

            # Comma:
            elif t.get_type()==Token_type.COM:
                # Remove operators from the stack and pass them to the output queue,
                # until left bracket is found.
                while stack and stack[-1].get_type()!=Token_type.LB:
                    ret.append(stack.pop())
                if not stack:
                    raise SyntaxError("missing left bracket")
                pass

            # Binary operator:
            elif t.get_type()==Token_type.OP:
                # Remove operators with higher priority from stack and pass them to the output queue
                while stack and stack[-1].get_type()!=Token_type.LB:
                    # Operators with left asociativity are removed even if the priority is the same.
                    if t.get_asociativity() and t.get_priority()<=stack[-1].get_priority():
                        ret.append(stack.pop())
                    elif (not t.get_asociativity()) and t.get_priority()<stack[-1].get_priority(): 
                        ret.append(stack.pop())
                    else:
                        # Break the loop if there are no more operators with higher priority
                        break
                # Insert current operator to the stack
                stack.append(t)

            # Function:
            elif t.get_type()==Token_type.FUNC:
                # Insert functions to the output queue
                stack.append(t)
                
            # Error:
            else:
                # Unkwnon token type, raise exception
                raise SyntaxError("Uknown token type: "+str(t))

        # Empty leftover tokens from stack
        while stack:
            if stack[-1].get_type()==Token_type.LB:
                # Left bracket in the stack indicates missing right bracket
                raise SyntaxError("missing right bracket")
            
            # Move all operators to the output queue
            ret.append(stack.pop())
            
        # Return token array in postfix notation.
        return ret

    ##
    #   @brief Semantic analysis
    #
    #   Perform final evaluation of the expression in post-fix notation.
    #   @param post_ary List of tokens in post-fix notation
    #   @return Numerical value of the expression
    def postfix_eval(self,post_ary):
        stack=[]
        if(post_ary==[]):
            return None
        for i in post_ary:
            if(i==None):
                i=Number(None)
            if(i.get_type()==Token_type.NUM):
                stack.append(i)
            if(i.get_type()==Token_type.OP or i.get_type()==Token_type.FUNC):
                pc=i.get_param_cnt()
                params=[]
                if(pc>len(stack)):
                    what= "operator" if i.get_type()==Token_type.OP else "function"
                    what2="arguments" if i.get_type()==Token_type.OP else "parameters"
                    raise SyntaxError(what+" '"+i.__str__()+"' takes "+str(pc)+" "+what2+", but only "+str(len(stack))+" were given")
                for y in range(pc):
                    params.append(stack.pop().eval([]))
                params.reverse()
                stack.append(Number(i.eval(params)))
        if(len(stack)>1):
            raise SyntaxError("leftover parameters")
        return stack.pop().eval([])

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
    # doctest.testfile("tests_operations.txt")
    doctest.testfile("tests_lexer.txt")
    doctest.testfile("tests_parser.txt")
    doctest.testfile("tests_parser2.txt")
    doctest.testfile("tests_semantics.txt")
    doctest.testfile("tests_semantics2.txt")
    # doctest.testfile("tests_complete_analysis.txt")
