import matplotlib.pyplot as plt
import numpy as np

# Factorising a fraction
def simplify_script(fraction_in):

    # Unpack the list which is a fraction
    f1, f2 = fraction_in

    # Loop through and find simplify
    for x in range(abs(f1 * f2)*-1,abs(f1 * f2)):
        if x != 0:
            if f1 % x == 0 and f2 % x == 0:
                ff1 = int(f1 / x)
                ff2 = int(f2 / x)
    
    return (ff1, ff2)

# Quadratic class
class QuadFact:

    # Initalise the quadratic equation
    def __init__(self, a_in, b_in, c_in):
        self.a_in = a_in
        self.b_in = b_in
        self.c_in = c_in
        self.no_factor = False
    

    # Printing the quadratic
    def __str__(self):
        return f"y = {self.a_in}x^2 + {self.b_in}x + {self.c_in}"


    # Find the factors and the properties of the quadratic
    def find_factor(self):
        # Step 1 of solving a factor, find a * c
        self.ac_step = self.a_in * self.c_in

        # Loop through and find the factor that adds to be b and multiplies to equal a * c
        self.found_roots = False

        # Range is from negative a * c to positive to create a factor table
        for x in range((abs(self.ac_step))*-1,abs(self.ac_step)):

            # If statement to catch division by zero
            if x != 0:

                # Criteria to meet for the values to be found through factorising
                if x + self.ac_step/x == self.b_in and self.found_roots == False:

                    # This is the numbers that match the criteria
                    self.fact_opts = [int(x), int(self.ac_step/x)]

                    # Take the numbers that match the crieria and adds them into a mock fraction to form the bonimials
                    self.binomial1 = [self.fact_opts[0], self.a_in]
                    self.binomial2 = [self.fact_opts[1], self.a_in]

                    # Simplify the fractions and unpack them into two binomials
                    self.bin1 = simplify_script([self.binomial1[1], self.binomial1[0]])
                    self.bin2 = simplify_script([self.binomial2[1], self.binomial2[0]])

                    # Search criteria met for the binomials
                    self.found_roots = True

                    # Return the binomials
                    return self.bin1, self.bin2

            else:
                
                # Can't be found through factorising
                self.no_factor = True
                return "Cannot be solved with factoring."


    # Display the quadratic information
    def quad_info(self):
        # Factorise as needed
        self.find_factor()

        # Checks to make sure it can be factored and has been factored, then display the information
        if self.no_factor == False:
            print(f"Two numbers that add to be {self.b_in} and multiply to be {self.ac_step}:\n{self.fact_opts[0]} and {self.fact_opts[1]}")
            print(f"Binomials: ({self.bin1[0]}x + {self.bin1[1]})({self.bin2[0]}x + {self.bin2[1]}) = 0")


    # Graph the function
    def graph_quad(self):
        # Factorise the equation
        self.find_factor()
        
        # Setup the graph space
        fig = plt.figure(num=0)
        plt.suptitle(f"Equation: y = {self.a_in}x^2 + {self.b_in}x + {self.c_in}")

        # Pick title based on if it can be factored
        if self.no_factor == False:
            plt.figtext(0.5,0.05, f"Binomials: ({self.bin1[0]}x + {self.bin1[1]})({self.bin2[0]}x + {self.bin2[1]}) = 0", ha="center", fontsize=10)
        
        else:
            plt.figtext(0.5,0.05, "Cannot be solved with factoring.", ha="center", fontsize=10)

        # Generate the data points for the graph and apply the function to this
        self.x = np.linspace(-4,4,100)
        self.y = self.a_in*self.x**2 + self.b_in * self.x + self.c_in

        # Setup the graph space
        ax = fig.add_subplot(1, 1, 1)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')

        # Plot the function
        plt.plot(self.x, self.y)

        # Show the plot
        plt.show()


factor1 = QuadFact(3, 7, -6)
print(factor1)
factor1.quad_info()
print(factor1.find_factor())
factor1.graph_quad()

factor2 = QuadFact(-1, -2, 3)
print(factor2)
factor2.quad_info()
print(factor2.find_factor())
factor2.graph_quad()

factor3 = QuadFact(8, -5, -2)
print(factor3)
factor3.quad_info()
print(factor3.find_factor())
factor3.graph_quad()