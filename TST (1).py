import tkinter as tk
from tkinter import messagebox
    class ChildNutritionCalculatorGUI:
def __init__(self, root):
self.root = root
self.root.title("Child Nutrition Calculator")
self.child_details = {}
# Nutritional values for each food (per 100g)
self.food_nutrients = {
'Milk': {'calories': 100, 'protein': 3.4, 'fat': 3.6, 'carbs': 4.8}, # g per 100g
'Egg': {'calories': 155, 'protein': 13, 'fat': 11, 'carbs': 1.1}, # g per 100g
'Rice': {'calories': 130, 'protein': 2.7, 'fat': 0.3, 'carbs': 28}, # g per 100g
'Lentils': {'calories': 113, 'protein': 9, 'fat': 0.4, 'carbs': 20}, # g per 100g
'Vegetable': {'calories': 85, 'protein': 3.5, 'fat': 0.5, 'carbs': 15}, # g per 100g
'Meat': {'calories': 143, 'protein': 20, 'fat': 5, 'carbs': 0} # g per 100g
}
# Daily calorie requirements for different age groups
self.calorie_requirements = {
(0, 2): 800,
(2, 4): 1400,
(4, 8): 1800
}
self.create_widgets()
def create_widgets(self):
# Instructions
tk.Label(self.root, text="Enter Child's Information", font=('Arial', 12, 'bold')).grid(row=0, column=0,
columnspan=2,
pady=(10, 5))
# Child details inputs with padding
tk.Label(self.root, text="Child's Name:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
self.name_entry = tk.Entry(self.root)
self.name_entry.grid(row=1, column=1, padx=10, pady=5)
tk.Label(self.root, text="Age (years):").grid(row=2, column=0, padx=10, pady=5, sticky="e")
self.age_entry = tk.Entry(self.root)
self.age_entry.grid(row=2, column=1, padx=10, pady=5)
tk.Label(self.root, text="Gender:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
self.gender_entry = tk.Entry(self.root)
self.gender_entry.grid(row=3, column=1, padx=10, pady=5)
tk.Label(self.root, text="Height (cm):").grid(row=4, column=0, padx=10, pady=5, sticky="e")
self.height_entry = tk.Entry(self.root)
self.height_entry.grid(row=4, column=1, padx=10, pady=5)
tk.Label(self.root, text="Weight (kg):").grid(row=5, column=0, padx=10, pady=5, sticky="e")
self.weight_entry = tk.Entry(self.root)
self.weight_entry.grid(row=5, column=1, padx=10, pady=5)
# Food intake inputs
tk.Label(self.root, text="\nFood Intake (grams)", font=('Arial', 12, 'bold')).grid(row=6, column=0,
columnspan=2, pady=(10, 5))
self.food_intake_entries = {}
row_index = 7
for food in self.food_nutrients:
tk.Label(self.root, text=f"{food}:").grid(row=row_index, column=0, padx=10, pady=5, sticky="e")
entry = tk.Entry(self.root)
entry.grid(row=row_index, column=1, padx=10, pady=5)
self.food_intake_entries[food] = entry
row_index += 1
# Buttons
tk.Button(self.root, text="Calculate", command=self.calculate, bg="lightgreen",
font=('Arial', 10, 'bold')).grid(row=row_index, column=0, pady=10)
tk.Button(self.root, text="Quit", command=self.root.quit, bg="red", font=('Arial', 10, 'bold')).grid(
row=row_index, column=1, pady=10)
# Results label
self.results_label = tk.Label(self.root, text="", font=('Arial', 10), fg="blue")
self.results_label.grid(row=row_index + 1, column=0, columnspan=2, pady=10)
def validate_inputs(self):
try:
age = int(self.age_entry.get())
height = float(self.height_entry.get())
weight = float(self.weight_entry.get())
if age <= 0 or height <= 0 or weight <= 0:
raise ValueError("Age, height, and weight must be positive.")
return True
except ValueError as ve:
messagebox.showerror("Input Error", str(ve))
return False
def calculate_bmi(self):
height_m = float(self.height_entry.get()) / 100
weight_kg = float(self.weight_entry.get())
bmi = weight_kg / (height_m ** 2)
return bmi
def get_min_calorie_requirement(self):
age = int(self.age_entry.get())
for age_range, calories in self.calorie_requirements.items():
if age_range[0] <= age < age_range[1]:
return calories
return 0 # If age is out of defined ranges
def calculate_daily_nutrients(self):
total_calories = 0
total_protein = 0
total_fat = 0
total_carbs = 0
for food, entry in self.food_intake_entries.items():
quantity = float(entry.get()) if entry.get() else 0
nutrients = self.food_nutrients[food]
total_calories += (nutrients['calories'] / 100) * quantity
total_protein += (nutrients['protein'] / 100) * quantity
total_fat += (nutrients['fat'] / 100) * quantity
total_carbs += (nutrients['carbs'] / 100) * quantity
return total_calories, total_protein, total_fat, total_carbs
def display_results(self, bmi, min_calories, daily_calories, protein, fat, carbs):
result = f"Calculated BMI: {bmi:.2f}\n"
result += f"Minimum Daily Calorie Requirement: {min_calories} calories\n"
result += f"Daily Calorie Consumption: {daily_calories:.2f} calories\n"
result += f"Total Protein Intake: {protein:.2f} g\n"
result += f"Total Fat Intake: {fat:.2f} g\n"
result += f"Total Carbohydrate Intake: {carbs:.2f} g\n"
if daily_calories < min_calories:
result += "\nThe child is undernourished."
else:
result += "\nThe child's calorie intake is adequate."
self.results_label.config(text=result)
def calculate(self):
if not self.validate_inputs():
return
try:
bmi = self.calculate_bmi()
min_calories = self.get_min_calorie_requirement()
daily_calories, protein, fat, carbs = self.calculate_daily_nutrients()
self.display_results(bmi, min_calories, daily_calories, protein, fat, carbs)
except Exception as e:
messagebox.showerror("Error", f"An error occurred: {str(e)}")
if __name__ == "__main__": # Corrected __name__ check
root = tk.Tk()
app = ChildNutritionCalculatorGUI(root)
root.mainloop()
