#creazione con metodo --init--


class Volo:
    _codice : str # <<imm>> noto alla nascita
    _durata_minuto : int #GZ  non noto alla nascita  // #GZ : Greater than Zero (Maggiore di zero)
    
    def __init__(self, codice: str, durata_minuto: int):
        self._codice = codice
        self._durata_minuto = durata_minuto

    def codice(self) -> str:
        return self._codice
    
    def durata_minuto(self) -> int: #GZ
        return self._durata_minuto
    
    
class Aereoporto:
    _codice : str #<<imm>> noto alla nascita
    _nome : str # non noto alla nascita

    def __init__(self, codice: str, nome: str):
        self._codice = codice
        self._nome = nome

    def codice(self) -> str:
        return self._codice
    
    def nome(self) -> str:
        return self._nome
    
    
class CompagniaAerea:
    _nome : str # non noto alla nascita
    _fondazione : int #G 1900 <<imm>> noto alla nascita

    def __init__(self, nome: str, fondazione: int):
        self._nome = nome
        self._fondazione = fondazione

    def nome(self) -> str:
        return self._nome
    
    def fondazione(self) -> int:  #G greater
        return self._fondazione
    
    
class Citta:
    _nome : str # non noto alla nascita
    _abitanti : int #GEZ non noto alla nascita

    def __init__(self, nome: str, abitanti: int):
        self._nome = nome
        self._abitanti = abitanti

    def nome(self) -> str:
        return self._nome
    
    def abitanti(self) -> int: #GEZ greater than or equal zero
        return self._abitanti
    
    
class Nazione:
    nome : str # non noto alla nascita

    def __init__(self, nome: str):
        self._nome = nome 

    def nome(self) -> str:
        return self._nome
    
#creazione di un oggetto volo    
volo1 = Volo("AZ123", 120)

#accesso agli attributi dell'oggetto volo1
codice_volo1 = volo1.codice()
durata_volo1 = volo1.durata_minuto()

print(f"Il codice del volo è: {codice_volo1}")
print(f"La durata del volo è: {durata_volo1} minuti")

areoporto1 = Aereoporto("FCO", "Aereoporto Leonardo Da Vinci Fiumicino")

codice_areoporto1 = areoporto1.codice()
nome_areoporto1 = areoporto1.nome()

print(f"Il codice dell'Aereoporto è: {codice_areoporto1}")
print(f"Il nome dell'Aereoporto è: {nome_areoporto1}")

compagnia_aerea = CompagniaAerea("Lufthansa", 1900) 

nome_compagnia_aerea = compagnia_aerea.nome()
fondazione_compagnia_aerea = compagnia_aerea.fondazione()

print(f"Il nome della compagnia aerea è: {nome_compagnia_aerea}")
print(f"La compagnia aerea è stata fondatata nel: {fondazione_compagnia_aerea}")

citta = Citta("Roma", 2.746_789)

nome_citta = citta.nome()
abitanti_citta = citta.abitanti()

print(f"Il nome della citta è: {nome_citta}")
print(f"Gli abitanti nel 2025 sono: {abitanti_citta}")

nazione = Nazione("Italia <3")

nome_nazione = nazione.nome()

print(f"La nazione della capitale è: {nome_nazione}")