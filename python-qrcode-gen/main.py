from tkinter import *
import qrcode
from tkinter import messagebox
from functools import partial

def gera_qr_code(website_entry: Entry):
    url = website_entry.get()

    if len(url) == 0:
        messagebox.showinfo(
        title="Erro!",
        message="Favor insira uma URL válida")
        return

    opcao_escolhida = messagebox.askokcancel(
    title=url,
    message=f"O endereço URL é: \n "
            f"Endereço: {url} \n "
            f"Pronto para salvar?")

    if opcao_escolhida:
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color='black', back_color='white')
        img.save('qrExport.png')


class App:
    def __init__(self, window: Tk) -> None:
       self.window = window

    def setup(self):
        self.window.title("Gerador de Código QR")
        self.window.config(padx=10, pady=100)

        website_label = Label(text="URL:")
        website_label.grid(row=2, column=0)

        website_entry = Entry(width=35)
        website_entry.grid(row=2, column=1, columnspan=2)
        website_entry.focus()

        qr_code_fn = partial(gera_qr_code, website_entry)
        add_button = Button(text="Gerar QR Code", width=36, command=qr_code_fn)
        add_button.grid(row=4, column=1, columnspan=2)

    def start(self):
        self.window.mainloop()


app = App(Tk())
app.setup()
app.start()
