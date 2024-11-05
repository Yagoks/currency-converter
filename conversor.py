import tkinter as tk
from tkinter import messagebox

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de Moedas - D&D")
        
        # Criação dos campos de entrada para cada moeda
        self.entries = {
            'CP': self.create_entry('Copper (CP)', 0),
            'SP': self.create_entry('Silver (SP)', 1),
            'EC': self.create_entry('Electrum (EC)', 2),
            'GP': self.create_entry('Gold (GP)', 3),
            'PP': self.create_entry('Platinum (PP)', 4),
        }
        
        # Botão para converter
        convert_button = tk.Button(self.root, text="Converter", command=self.convert)
        convert_button.grid(row=5, column=0, columnspan=2, pady=10)

    def create_entry(self, label_text, row):
        label = tk.Label(self.root, text=label_text)
        label.grid(row=row, column=0, padx=10, pady=5)
        entry = tk.Entry(self.root)
        entry.grid(row=row, column=1, padx=10, pady=5)
        return entry

    def convert(self):
        try:
            # Obtém os valores inseridos, tratando entradas vazias como 0
            cp = int(self.entries['CP'].get() or 0)
            sp = int(self.entries['SP'].get() or 0)
            ec = int(self.entries['EC'].get() or 0)
            gp = int(self.entries['GP'].get() or 0)
            pp = int(self.entries['PP'].get() or 0)

            # Converte tudo para CP
            total_cp = (cp 
                        + sp * 10 
                        + ec * 100 
                        + gp * 1000 
                        + pp * 10000)

            # Converte de volta para PP, GP, EC, SP e CP
            pp = total_cp // 10000
            total_cp %= 10000

            gp = total_cp // 1000
            total_cp %= 1000

            ec = total_cp // 100
            total_cp %= 100

            sp = total_cp // 10
            cp = total_cp % 10

            # Atualiza os campos com os novos valores
            self.entries['CP'].delete(0, tk.END)
            self.entries['CP'].insert(0, str(cp))

            self.entries['SP'].delete(0, tk.END)
            self.entries['SP'].insert(0, str(sp))

            self.entries['EC'].delete(0, tk.END)
            self.entries['EC'].insert(0, str(ec))

            self.entries['GP'].delete(0, tk.END)
            self.entries['GP'].insert(0, str(gp))

            self.entries['PP'].delete(0, tk.END)
            self.entries['PP'].insert(0, str(pp))

        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira apenas números inteiros.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()
