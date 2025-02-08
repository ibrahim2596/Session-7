import matplotlib.pyplot as plt  
# Week Days  
days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']  
# temperatures in Celsius  
temperatures = [20, 22, 25, 23, 21, 24, 26]  
# Create the plot  
plt.plot(days, temperatures, marker='o', linestyle='-', color='b')  
# Add labels and title  
plt.xlabel('Week Day')  
plt.ylabel('Temperature (°C)')  
plt.title('Temperature Variation Over a Week') 
# Add grid for better readability  
plt.grid(True)  
# Show the plot  
plt.show()  