'''hashabel (è una funzione  built_in (integrata di python che prende un oggetto come input e restituisce un valore intero fisso, chiamato valore hash))

eq;  (abbreviazione (equals in inglese), ovvero (==),è l'operazione più comune per verificare se il valore è lo stesso)

is; (è un operatore di identità, a differenza dell'operatore di uguaglianza == , 
     che verifica se il valore di due oggetti è lo stesso due variabili si riferiscono allo stesso oggetto in memoria)
     esempio: X is Y restituisce True solo se X e Y sono la stessa posizione di memoria.
     Restituisce False anche se X e Y hanno lo stesso valore ma sono oggetti distinti.)'''

from datetime import date

class Citta:
    def __init__(self, nome: str):
        self.nome = nome

    def __eq__(self, other):
        if isinstance(other, Citta):
            return self.nome == other.nome
        return NotImplemented

    def __hash__(self):
        return hash(self.nome)

    def __repr__(self):
        return f"Citta(nome='{self.nome}')"

class Regione:
    def __init__(self, nome: str, citta: Citta):
        self.nome = nome
        self.citta = citta

    def __eq__(self, other):
        if isinstance(other, Regione):
            return self.nome == other.nome and self.citta == other.citta
        return NotImplemented

    def __hash__(self):
        return hash((self.nome, self.citta))

    def __repr__(self):
        return f"Regione(nome='{self.nome}', citta={self.citta})"

class Nazione:
    def __init__(self, nome: str, regione: Regione):
        self.nome = nome
        self.regione = regione

    def __eq__(self, other):
        if isinstance(other, Nazione):
            return self.nome == other.nome and self.regione == other.regione
        return NotImplemented

    def __hash__(self):
        return hash((self.nome, self.regione))

    def __repr__(self):
        return f"Nazione(nome='{self.nome}', regione={self.regione})"

class Persona:
    def __init__(self, nome: str, cognome: str, cf_codice_fiscale: str, indirizzo: str, telefono: str, data_nascita: date):
        self.nome = nome
        self.cognome = cognome
        self.cf_codice_fiscale = cf_codice_fiscale
        self.indirizzo = indirizzo
        self.telefono = telefono
        self.data_nascita = data_nascita

    def __eq__(self, other):
        if isinstance(other, Persona):
            return self.cf_codice_fiscale == other.cf_codice_fiscale
        return NotImplemented

    def __hash__(self):
        return hash(self.cf_codice_fiscale)

    def __repr__(self):
        return f"Persona(nome='{self.nome}', cognome='{self.cognome}', cf_codice_fiscale='{self.cf_codice_fiscale}')"

class Proprietario(Persona):
    def __init__(self, nome: str, cognome: str, cf_codice_fiscale: str, indirizzo: str, telefono: str, data_nascita: date, veicoli_posseduti: list = None):
        super().__init__(nome, cognome, cf_codice_fiscale, indirizzo, telefono, data_nascita)
        self.veicoli_posseduti = veicoli_posseduti if veicoli_posseduti is not None else []

    def __repr__(self):
        return f"Proprietario(nome='{self.nome}', cognome='{self.cognome}', cf_codice_fiscale='{self.cf_codice_fiscale}', veicoli={self.veicoli_posseduti})"

class Dipendente(Persona):
    def __init__(self, nome: str, cognome: str, cf_codice_fiscale: str, indirizzo: str, telefono: str, data_nascita: date, agenzia_servizio: str, officina_interna: bool):
        super().__init__(nome, cognome, cf_codice_fiscale, indirizzo, telefono, data_nascita)
        self.agenzia_servizio = agenzia_servizio
        self.officina_interna = officina_interna

    def __repr__(self):
        return f"Dipendente(nome='{self.nome}', cognome='{self.cognome}', cf_codice_fiscale='{self.cf_codice_fiscale}', agenzia='{self.agenzia_servizio}', interno={self.officina_interna})"

class Direttore(Dipendente):
    def __init__(self, nome: str, cognome: str, cf_codice_fiscale: str, indirizzo: str, telefono: str, data_nascita: date, agenzia_servizio: str, officina_interna: bool, data_nomina: date):
        super().__init__(nome, cognome, cf_codice_fiscale, indirizzo, telefono, data_nascita, agenzia_servizio, officina_interna)
        self.data_nomina = data_nomina

    def __repr__(self):
        return f"Direttore(nome='{self.nome}', cognome='{self.cognome}', cf_codice_fiscale='{self.cf_codice_fiscale}', agenzia='{self.agenzia_servizio}', interno={self.officina_interna}, nomina={self.data_nomina})"

class TipoVeicolo:
    def __init__(self, nome: str):
        self.nome = nome

    def __eq__(self, other):
        if isinstance(other, TipoVeicolo):
            return self.nome == other.nome
        return NotImplemented

    def __hash__(self):
        return hash(self.nome)

    def __repr__(self):
        return f"TipoVeicolo(nome='{self.nome}')"

class Modello:
    def __init__(self, nome: str, tipo_veicolo: TipoVeicolo):
        self.nome = nome
        self.tipo_veicolo = tipo_veicolo

    def __eq__(self, other):
        if isinstance(other, Modello):
            return self.nome == other.nome and self.tipo_veicolo == other.tipo_veicolo
        return NotImplemented

    def __hash__(self):
        return hash((self.nome, self.tipo_veicolo))

    def __repr__(self):
        return f"Modello(nome='{self.nome}', tipo={self.tipo_veicolo})"

class Veicolo:
    def __init__(self, targa: str, modello: Modello, range_km: float, anno_immatricolazione: int, proprietario: Proprietario = None):
        self.targa = targa
        self.modello = modello
        self.range_km = range_km
        self.anno_immatricolazione = anno_immatricolazione
        self.proprietario = proprietario

    def __eq__(self, other):
        if isinstance(other, Veicolo):
            return self.targa == other.targa
        return NotImplemented

    def __hash__(self):
        return hash(self.targa)

    def __repr__(self):
        return f"Veicolo(targa='{self.targa}', modello={self.modello}, anno={self.anno_immatricolazione}, proprietario={self.proprietario})"

class Lavoro:
    def __init__(self, codice: str, descrizione: str, costo_previsto: float, data_inizio: date, dipendente: Dipendente = None, officina: 'Officina' = None):
        self.codice = codice
        self.descrizione = descrizione
        self.costo_previsto = costo_previsto
        self.data_inizio = data_inizio
        self.dipendente = dipendente
        self.officina = officina

    def __eq__(self, other):
        if isinstance(other, Lavoro):
            return self.codice == other.codice
        return NotImplemented

    def __hash__(self):
        return hash(self.codice)

    def __repr__(self):
        return f"Lavoro(codice='{self.codice}', descrizione='{self.descrizione}', costo={self.costo_previsto}, inizio={self.data_inizio}, dipendente={self.dipendente}, officina={self.officina})"

class Officina:
    def __init__(self, nome: str, indirizzo: str, agenzia_servizio: str, dipendenti: list = None, lavori_effettuati: list = None):
        self.nome = nome
        self.indirizzo = indirizzo
        self.agenzia_servizio = agenzia_servizio
        self.dipendenti = dipendenti if dipendenti is not None else []
        self.lavori_effettuati = lavori_effettuati if lavori_effettuati is not None else []

    def __eq__(self, other):
        if isinstance(other, Officina):
            return self.nome == other.nome and self.indirizzo == other.indirizzo
        return NotImplemented

    def __hash__(self):
        return hash((self.nome, self.indirizzo))

    def __repr__(self):
        return f"Officina(nome='{self.nome}', indirizzo='{self.indirizzo}', agenzia='{self.agenzia_servizio}')"

class Riparazione:
    def __init__(self, codice: str, veicolo: Veicolo, data_ora_accettazione: date, lavori_richiesti: list = None, riparazione_terminata: 'RiparazioneTerminata' = None):
        self.codice = codice
        self.veicolo = veicolo
        self.data_ora_accettazione = data_ora_accettazione
        self.lavori_richiesti = lavori_richiesti if lavori_richiesti is not None else []
        self.riparazione_terminata = riparazione_terminata

    def __eq__(self, other):
        if isinstance(other, Riparazione):
            return self.codice == other.codice
        return NotImplemented

    def __hash__(self):
        return hash(self.codice)

    def __repr__(self):
        return f"Riparazione(codice='{self.codice}', veicolo={self.veicolo}, accettazione={self.data_ora_accettazione}, terminata={self.riparazione_terminata})"

class RiparazioneTerminata:
    def __init__(self, riparazione: Riparazione, data_ora_terminazione: date):
        self.riparazione = riparazione
        self.data_ora_terminazione = data_ora_terminazione

    def __eq__(self, other):
        if isinstance(other, RiparazioneTerminata):
            return self.riparazione == other.riparazione
        return NotImplemented

    def __hash__(self):
        return hash(self.riparazione)

    def __repr__(self):
        return f"RiparazioneTerminata(riparazione={self.riparazione}, termine={self.data_ora_terminazione})"

# Esempio di utilizzo e confronto con 'is'
if __name__ == "__main__":
    roma1 = Citta("Roma")
    roma2 = Citta("Roma")
    milano = Citta("Milano")

    print(f"roma1 == roma2: {roma1 == roma2}") # True (stesso nome)
    print(f"roma1 is roma2: {roma1 is roma2}") # Probabilmente False (oggetti diversi in memoria)

    persona1_cf = "RSSGNN01A01H501X"
    persona1 = Persona("Giovanni", "Rossi", persona1_cf, "Via...", "...", date(2001, 1, 1))
    persona2 = Persona("Mario", "Bianchi", "ABCDEF...", "Via...", "...", date(1990, 5, 10))
    persona3 = Persona("Luigi", "Verdi", persona1_cf, "Altra Via...", "...", date(2001, 1, 1))

    print(f"persona1 == persona3: {persona1 == persona3}") # True (stesso codice fiscale)
    print(f"persona1 is persona3: {persona1 is persona3}") # False (oggetti diversi)

    tipo1 = TipoVeicolo("Auto")
    tipo2 = TipoVeicolo("Auto")
    print(f"tipo1 == tipo2: {tipo1 == tipo2}") # True (stesso nome)
    print(f"tipo1 is tipo2: {tipo1 is tipo2}") # Probabilmente False

    # Esempio con 'is None' (anche se non direttamente dalle classi UML)
    veicolo1 = Veicolo("AA123BB", Modello("Punto", tipo1), 100000, 2010)
    print(f"veicolo1.proprietario is None: {veicolo1.proprietario is None}") # True inizialmente

    proprietario1 = Proprietario("Carlo", "Neri", "GHIJKL...", "Via...", "...", date(1975, 11, 20))
    veicolo1.proprietario = proprietario1
    print(f"veicolo1.proprietario is None: {veicolo1.proprietario is None}") # False dopo l'assegnazione