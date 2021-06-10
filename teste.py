import BondGraphTools as bgt
model = bgt.new(name="RC")


#Now create a new generalised linear resistor (‘R’ component), a generalised linear capacitor (“C” component) with resistance and capacitance both set to 1,
#and an equal effort (“0” junction) conservation law through which these components share energy.:
C = bgt.new("C", value=1)
R = bgt.new("R", value=1)
zero_law = bgt.new("0")

#Add the newly created components to the model:
bgt.add(model, R, C, zero_law)

#Once the components are added to the model, connect the components and the law together.
#(Note the first argument is the tail of the energy bond, the second is the head):
bgt.connect(R, zero_law)
bgt.connect(zero_law, C)

#Draw the model to make sure everything is wired up:
bgt.draw(model)

#To demonstrate that the isolated system is behaving correctly, we simulate from the initial
#where the C component has $x_0=1$ and run the simulation over the time interval $(0,5)$.
#This results in a vector $t$ of time of time points and a corresponding vector $x$ of data points
#which can then be plotted against eachother with matplotlib
timespan = [0, 5]
x0 = [1]
t, x = simulate(model, timespan=timespan, x0=x0)
from matplotlib.pyplot import plot
fig = plot(t,x)



