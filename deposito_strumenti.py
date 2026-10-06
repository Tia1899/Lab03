import datetime,csv
from operator import attrgetter
class strumento:
    def __init__(self,codice,nome,marca,anno,valore):

        self.codice = codice
        self.nome = nome
        self.marca = marca
        self.anno = anno
        self.valore = valore
    def __str__(self):
        return f'{self.codice} {self.nome} {self.marca} {self.anno} {self.valore}'

class prestito:
    def __init__(self,codice,data,codicestrumento,cognome):
        self.codice = codice
        self.data = data
        self.codicestrumento = codicestrumento
        self.cognome = cognome
    def __str__(self):
        return f'{self.codice} {self.data} {self.codicestrumento} {self.cognome}'


class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.nome = nome
        self.responsabile = responsabile
        self.prestiti = {}
        self.strumenti = {}


    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        # TODO
        with open(file_path) as file:
            reader = csv.reader(file)
            for line in reader:
                strumento=strumento(line[0],line[1],line[2],int(line[3]),float(line[4]))
                self.strumenti[line[0]]=strumento




    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO
        nuovo_codice='s{len(self.strumenti)}'
        nuovo_strumento=strumento(nuovo_codice,tipo,marca,anno_acquisto,valore)
        self.strumenti[nuovo_codice]=nuovo_strumento

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO
        lista_ordinare=[]
        for codice in self.strumenti:
            lista_ordinare.append(self.strumenti[codice])
        lista_ordinati=sorted(lista_ordinare, key=attrgetter('marca'))

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # TODO

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO
