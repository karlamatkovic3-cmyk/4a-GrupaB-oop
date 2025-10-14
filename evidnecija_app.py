import tkinter as tk
from tkinter import messagebox

class Ucenik:

    def __init__(self,ime, prezime,razred):

        self.ime=ime
        self.prezime=prezime
        self.razred=razred

    def __str__(self):
        return (f"ime:{self.ime},prezime:{self.prezime},razred:{self.razred}")

class EvidencijaApp:

    def __init__(self,root):
        self.root=root
        self.root.title("Evidencija učenika")
        self.root.geometry("800x800")
        self.ucenici =[]
        self.odabrani_ucenik_index=None

        
        
        self.root.columnconfigure(0, weight=1)
       

        
        self.root.rowconfigure(1, weight=1)



        unos_frame = tk.Frame(self.root, padx=10, pady=10,bg="purple")
        unos_frame.grid(row=0, column=0, sticky="EW") 


        prikaz_frame = tk.Frame(self.root, padx=10, pady=10,bg="grey")
        prikaz_frame.grid(row=1, column=0, sticky="NSEW") 


        prikaz_frame.columnconfigure(0, weight=1)
        prikaz_frame.rowconfigure(0, weight=1)



        tk.Label(unos_frame, text="Ime:",fg="grey").grid(row=0, column=0, padx=5, pady=5, sticky="W")
        self.ime_entry = tk.Entry(unos_frame)
        self.ime_entry.grid(row=0, column=1, padx=5, pady=5, sticky="EW")

        tk.Label(unos_frame, text="Prezime:",fg="grey").grid(row=1, column=0, padx=5, pady=5, sticky="W")
        self.prezime_entry = tk.Entry(unos_frame)
        self.prezime_entry.grid(row=1, column=1, padx=5, pady=5, sticky="EW")

        tk.Label(unos_frame, text="Razred:",fg="grey").grid(row=2, column=0, padx=5, pady=5, sticky="W")
        self.razred_entry = tk.Entry(unos_frame)
        self.razred_entry.grid(row=2, column=1, padx=5, pady=5, sticky="EW")

        self.dodaj_gumb = tk.Button(unos_frame, text="Dodaj učenika",command=self.dodaj_ucenika)
        self.dodaj_gumb.grid(row=3, column=0, padx=5, pady=10)
        self.spremi_gumb = tk.Button(unos_frame, text="Spremi izmjene",command=self.spremi_izmjene)
        self.spremi_gumb.grid(row=3, column=1, padx=5, pady=10, sticky="W")


        self.listbox = tk.Listbox(prikaz_frame)
        self.listbox.grid(row=0, column=0, sticky="NSEW")

        scrollbar = tk.Scrollbar(prikaz_frame, orient="vertical", command=self.listbox.yview)
        scrollbar.grid(row=0, column=1, sticky="NS")
        self.listbox.config(yscrollcommand=scrollbar.set)
        self.listbox.bind("<<ListboxSelect>>",self.odaberi_ucenika)

    def dodaj_ucenika(self):
        ime=self.ime_entry.get()
        prezime=self.prezime_entry.get()
        razred=self.razred_entry.get()
        if not ime or not prezime or not razred:
            messagebox.showwaring("Upozorenje", "Sva polja moraju biti popunjena.")
            return
        novi=Ucenik(ime,prezime,razred)
        self.ucenici.append(novi)
        self.osvjezi_prikaz()
        self.ocisti_polja()
    def osvjezi_prikaz(self):
        self.listbox.delete(0,tk.END)
        for u in self.ucenici:
            self.listbox.insert(tk.END,str(u))
    def odaberi_ucenika(self,event):
        odabrani=self.listbox.curselection()
        if not odabrani:
            return
        self.odabrani_ucenik_index=odabrani[0]
        u=self.ucenici[self.odabrani_ucenik_index]
        self.ime_entry.delete(0,tk.END)
        self.ime_entry.insert(0,u.ime)
        self.prezime_entry.delete(0,tk.END)
        self.prezime_entry.insert(0,u.prezime)
        self.razred_entry.delete(0,tk.END)
        self.razred_entry.insert(0,u.razred)

    def spremi_izmjene(self):
        if self.odabrani_ucenik_index is None:
            messagebox.showwarning("Upozorenje", "Nijedan učenik nije odabran.")
            return
        ime=self.ime_entry.get()
        prezime=self.prezime_entry.get()
        razred=self.razred_entry.get()
        if not ime or not prezime or not razred:
            messagebox.schowwaring("Upozorenje", "Sva polja moraju biti popunjena.")
            return
        u=self.ucenici[self.odabrani_ucenik_index]
        u.ime=ime
        u.prezime=prezime
        u.razred=razred
        self.osvjezi_prikaz()
        self.ocisti_polja()
        self.odabrani_ucenik_index=None

    def ocisti_polja(self):
        self.ime_entry.delete(0,tk.END)
        self.prezime_entry.delete(0,tk.END)
        self.razred_entry.delete(0,tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = EvidencijaApp(root)
    root.mainloop()




            


                                   
