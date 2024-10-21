import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt
import csv

class CreditContract:
    def __init__(self, contract_id, amount, manager):
        self.contract_id = contract_id
        self.amount = amount
        self.manager = manager

    def __str__(self):
        return f"ID: {self.contract_id}, Amount: {self.amount}, Manager: {self.manager}"

class ContractManager:
    def __init__(self):
        self.contracts = []

    def load_contracts(self, filename):
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) != 3:
                        raise ValueError("Incorrect data format")
                    contract_id, amount, manager = row
                    amount = float(amount)
                    self.contracts.append(CreditContract(contract_id, amount, manager))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load data: {e}")

    def segment_by_amount(self):
        small, medium, large = 0, 0, 0
        for contract in self.contracts:
            if contract.amount < 1000:
                small += 1
            elif contract.amount < 10000:
                medium += 1
            else:
                large += 1
        return {'Small': small, 'Medium': medium, 'Large': large}

    def segment_by_manager(self):
        manager_dict = {}
        for contract in self.contracts:
            if contract.manager in manager_dict:
                manager_dict[contract.manager] += 1
            else:
                manager_dict[contract.manager] = 1
        return manager_dict

    def segment_by_amount_plot(self):
        self.plot_pie_chart(self.segment_by_amount(), "Contracts by Amount")

    def segment_by_manager_plot(self):
        self.plot_pie_chart(self.segment_by_manager(), "Contracts by Manager")

    def plot_pie_chart(self, data, title):
        labels = data.keys()
        sizes = data.values()
        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title(title)
        plt.show()

class App:
    def __init__(self, root):
        self.manager = ContractManager()
        self.root = root
        self.root.title("Credit Contracts Manager")

        self.load_button = tk.Button(root, text="Load Contracts", command=self.load_contracts)
        self.load_button.pack()

        self.segment_amount_button = tk.Button(root, text="Segment by Amount", command=self.segment_by_amount)
        self.segment_amount_button.pack()

        self.segment_manager_button = tk.Button(root, text="Segment by Manager", command=self.segment_by_manager)
        self.segment_manager_button.pack()
    def segment_by_amount(self):
        self.manager.segment_by_amount_plot()

    def segment_by_manager(self):
        self.manager.segment_by_manager_plot()


    def load_contracts(self):
        filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if filename:
            self.manager.load_contracts(filename)
            messagebox.showinfo("Info", "Contracts loaded successfully")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()