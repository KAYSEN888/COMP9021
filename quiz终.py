# A polynomial object can be created from a string that represents a polynomial
# as sums or differences of monomials.
# - Monomials are ordered from highest to lowest powers.
# - All factors are strictly positive, except possibly for the leading factor
# - For nonzero powers, factors of 1 are only implicit.
# A single space surrounds + and - signs between monomials.

# Written by *** and Eric Martin for COMP9021


import re # split() suffices though
from collections import defaultdict
from copy import deepcopy


class Polynomial:
    def __init__(self, polynomial='0'):
        self.grid = defaultdict(int)
        self.raw_polynomial = polynomial
        self.polynomial = polynomial.split() # ['2x^3','+','x','-','4']
        self.csfficients = []
        self.powers = []
        plus_minus = ['+','-']
        if polynomial =='0':
            self.grid[0] = 0
        elif polynomial!='0':
            
            symbol = polynomial.split(' ')
            f_p_c = self.construst_dic(symbol[0])
            self.grid[f_p_c[0]] = f_p_c[1]
            for i in range(2, len(symbol), 2):
                p_a_c = self.construst_dic(symbol[i])
                if symbol[i - 1] == '-':
                    self.grid[p_a_c[0]] = -1 * p_a_c[1]
                elif symbol[i - 1]!='-':
                    
                    self.grid[p_a_c[0]] = p_a_c[1]

    def repr(self):
        self.print = ''
        if_x = True
        for i in range(len(self.csfficients)):
            if self.csfficients[i] >= 0:
                mark = '+'
                if self.csfficients[i]>0 and self.csfficients[i] == 1 :
                    cs = ''
                elif self.csfficients[i]!=1:
                    
                    cs = str(self.csfficients[i])
            elif self.csfficients[i]<0:
                
                mark = '-'
                if self.csfficients == -1:
                    cs = ''
                else:	
                    cs = str(-1*self.csfficients[i])
                if self.powers[i] == 1:
                    po = ''
                elif self.powers[i] == 0:
                    if_x = False
                else:
                    po = '^' + str(self.powers[i])

                if self.print:
                    self.print += ' ' + mark + ' ' 
                else:
                    if mark == '-':
                        self.print += mark

                if if_x == True:
                    self.print = self.print + cs + 'x' + po
                else:
                    self.print = self.print + cs
        return self.print


    def construst_dic(self, fir_par_digital):
        x_index = fir_par_digital.find('x')
        self.print = ''
        if_x = True
        for i in range(len(self.csfficients)):
            if self.csfficients[i] <0:
                continue
            elif self.csfficients[i] >= 0:
                mark = '+'
                if self.csfficients[i]>0 and self.csfficients[i] == 1 :
                    cs = ''
                elif self.csfficients[i]!=1:
                    cs = str(self.csfficients[i])
        if fir_par_digital[0] != '-':
            if x_index == -1:
                power = 0
                cs = int(fir_par_digital)
                return power, cs
            if x_index == len(fir_par_digital) - 1:
                power = 1
                if x_index != 0:
                    cs = int(fir_par_digital[:x_index])
                elif x_index == 0:
                    
                    cs = 1
            elif x_index != len(fir_par_digital) - 1:
                power = int(fir_par_digital[x_index + 2:])
                if x_index != 0:
                    cs = int(fir_par_digital[:x_index])
                elif x_index == 0:
                    cs = 1
            return power, cs
        elif fir_par_digital[0] == '-':
            
            if x_index == -1:
                power = 0
                cs = int(fir_par_digital)
                return power, cs
            if x_index == len(fir_par_digital) - 1:
                power = 1
                if x_index > 1:
                    cs = int(fir_par_digital[:x_index])
                elif x_index<=1:
                    cs = -1
            elif x_index != len(fir_par_digital) - 1:
                power = int(fir_par_digital[x_index + 2:])
                if x_index > 1:
                    cs = int(fir_par_digital[:x_index])
                elif x_index<=1:
                    cs = -1
            return power, cs
        

    def __add__(self, other):
        first_one = deepcopy(self)
        for fir_one in other.grid.keys():
            if fir_one not in first_one.grid.keys():
                first_one.grid[fir_one] = other.grid[fir_one]
            elif fir_one in first_one.grid.keys():
                first_one.grid[fir_one] = first_one.grid[fir_one] + other.grid[fir_one]
        return first_one
    def __iadd__(self, other):
        first_one = deepcopy(self)
        for fir_one in other.grid.keys():
            if fir_one  not in first_one.grid.keys():
                first_one.grid[fir_one] = other.grid[fir_one]
            elif fir_one in first_one.grid.keys():
                first_one.grid[fir_one] = first_one.grid[fir_one] + other.grid[fir_one]
        return first_one
    
    
    def __mul__(self, other):
        first_one = Polynomial()
        first_one.grid.pop(0)
        for s_key in self.grid.keys():
            for fir_one in other.grid.keys():
                if s_key + fir_one  in first_one.grid.keys():
                    first_one.grid[s_key + fir_one] = first_one.grid[s_key + fir_one]
                    first_one.grid[s_key + fir_one]= first_one.grid[s_key + fir_one]+self.grid[s_key] * other.grid[fir_one]
                elif s_key + fir_one  not in first_one.grid.keys():
                    first_one.grid[s_key + fir_one] = self.grid[s_key] * other.grid[fir_one]

                    
        return first_one
    def mul(self,other):
        final_con = {}
        self.new_csfficients = []
        self.new_powers = []
        degree = self.powers[0]+other.powers[0]
        for i in range(degree):
            final_con[i] = 0
        for i in range(len(other.csfficients)):
            for j in range(len(self.csfficients)):
                final_con[other.powers[i]+self.powers[j]] += other.csfficients[i] * self.csfficients[j]
        for key in final_con.keys():
            if final_con[key]:
                self.new_powers.append(key)
                self.new_csfficients.append(final_con[key])
        self.csfficients = self.new_csfficients
        self.powers = self.new_powers
    def __imul__(self, other):
        first_one = Polynomial()
        first_one.grid.pop(0)
        for s_key in self.grid.keys():
            for fir_one in other.grid.keys():
                if s_key + fir_one  in first_one.grid.keys():
                    first_one.grid[s_key + fir_one] = first_one.grid[s_key + fir_one]
                    first_one.grid[s_key + fir_one]= first_one.grid[s_key + fir_one]+self.grid[s_key] * other.grid[fir_one]
                elif s_key + fir_one not in first_one.grid.keys():
                    first_one.grid[s_key + fir_one] = self.grid[s_key] * other.grid[fir_one]
        return first_one
    def __str__(self):
        
        if 0 in self.grid.keys() :
            if  self.grid[0] == 0:
                self.grid.pop(0)
        comp_dic = deepcopy(self.grid)
        for key in comp_dic.keys():
            if comp_dic[key] == 0:
                self.grid.pop(key)
        if len(self.grid) == 0:
            return '0'
        elif len(self.grid) != 0:
            sorted_dic = sorted(self.grid.items(), reverse=True)
            if sorted_dic[0][0] == 0:
                if sorted_dic[0][1] == 1:
                    first_elements = str(sorted_dic[0][1])
                elif sorted_dic[0][1] == -1:
                    first_elements = '-1'
                elif sorted_dic[0][1]!=1 and sorted_dic[0][1]!= -1:
                    first_elements = str(sorted_dic[0][1])
            elif sorted_dic[0][0] == 1:
                if sorted_dic[0][1] == 1:
                    first_elements = 'x'
                elif sorted_dic[0][1] == -1:
                    first_elements = '-x'
                elif sorted_dic[0][1]!=1 and sorted_dic[0][1]!= -1:
                    first_elements = str(sorted_dic[0][1]) + 'x'
            elif sorted_dic[0][0]!=0 and sorted_dic[0][0]!=1:
                if sorted_dic[0][1] == 1:
                    first_elements = 'x^'
                    first_elements+= str(sorted_dic[0][0])
                elif sorted_dic[0][1] == -1:
                    first_elements = '-x^'
                    first_elements += str(sorted_dic[0][0])
                elif sorted_dic[0][1]!=1 and sorted_dic[0][1]!= -1:
                    first_elements = str(sorted_dic[0][1])
                    first_elements += 'x^'
                    first_elements += str(sorted_dic[0][0])

            final_con = ''
            for i in range(1, len(sorted_dic)):
                if sorted_dic[i][1]==-1 or sorted_dic[i][1] < 0 :
                    if sorted_dic[i][0]>0 and sorted_dic[i][0] == 1:
                        if sorted_dic[i][1] >-1 or sorted_dic[i][1]<-1 :
                            final_con =final_con+ ' - '
                            final_con =final_con+str(-1 * sorted_dic[i][1])
                            final_con =final_con+ 'x'
                        elif sorted_dic[i][1]==-1:
                            
                            final_con =final_con+ ' - '
                            final_con =final_con+ 'x'
                    elif sorted_dic[i][0] == 0:
                        if sorted_dic[i][1] != -1:
                            final_con =final_con+ ' - '
                            final_con =final_con+ str(-1 * sorted_dic[i][1])
                        elif sorted_dic[i][1] == -1:
                            final_con =final_con+ ' - '
                            final_con =final_con+ '1'
                    elif sorted_dic[i][0]!= 0 and sorted_dic[i][0]!= 1:
                        
                        if sorted_dic[i][1] >-1 or sorted_dic[i][1] <-1:
                            final_con =final_con+ ' - '
                            final_con =final_con+ str(-1 * sorted_dic[i][1])
                            final_con =final_con+ 'x^'
                            final_con =final_con+ str(sorted_dic[i][0])
                        elif sorted_dic[i][1]==-1:
                            
                            final_con =final_con+ ' - ' + 'x^' + str(sorted_dic[i][0])
                elif sorted_dic[i][1]>0 or sorted_dic[i][1]==0 :
                    if sorted_dic[i][0]>0  and sorted_dic[i][0] == 1:
                        if sorted_dic[i][1] >1 or sorted_dic[i][1] <1:
                            final_con =final_con+ ' + '
                            final_con =final_con+ str(sorted_dic[i][1])
                            final_con =final_con+ 'x'
                        elif sorted_dic[i][1]==1:
                            final_con =final_con+ ' + '
                            final_con =final_con+ 'x'
                    elif sorted_dic[i][0] == 0:
                        if sorted_dic[i][1] != 1:
                            final_con =final_con+ ' + '
                            final_con =final_con+ str(sorted_dic[i][1])
                        elif sorted_dic[i][1] == 1:
                            final_con =final_con+ ' + ' + '1'
                    elif sorted_dic[i][0]!= 0 and sorted_dic[i][0]!= 1:
                        
                        if sorted_dic[i][1] >1 or sorted_dic[i][1] < 1:
                            final_con =final_con+ ' + '
                            final_con =final_con+ str(sorted_dic[i][1])
                            final_con =final_con+ 'x^'
                            final_con =final_con+ str(sorted_dic[i][0])
                        elif sorted_dic[i][1]==1:
                             
                            final_con =final_con+ ' + '
                            final_con =final_con+ 'x^'
                            final_con =final_con+ str(sorted_dic[i][0])

            final_con = first_elements + final_con
            return final_con
