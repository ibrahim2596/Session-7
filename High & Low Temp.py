import pandas as pd
import matplotlib.pyplot as plt
temp = pd.read_excel("Temp.xlsx")
Days = temp["Day"].copy()
Low_Temp = temp["Low Temperature (°C)"].copy()
High_Temp = temp["High Temperature (°C)"].copy()
plt.plot(Days,Low_Temp, label = "Low Temperature (°C)", marker='o', linestyle='-', color='k')  
plt.plot(Days,High_Temp, label = "High Temperature (°C)", marker ='o', linestyle='--', color='b')  
# Add labels and title 
plt.xlabel('Week Day')  
plt.ylabel('Temperature (°C)')  
plt.title('Temperature Variation Over a Week') 
plt.grid(True)
plt.legend()
plt.show()