# creazione senza assegnazione valori specifici.

class Volo:
    _codice : str # <<imm>> noto alla nascita
    _durata_minuto : int #GZ noto alla nascita  // #GZ : Greater than Zero (Maggiore di zero)
    
    def codice(self) -> str:
        return self._codice
    
    def durata_minuto(self) -> int: #GZ
        return self._durata_minuto
    
    
class Aereoporto:
    _codice : str #<<imm>> noto alla nascita
    _nome : str # non noto alla nascita

    def codice(self) -> str:
        return self._codice
    
    def nome(self) -> str:
        return self._nome
    
    
class CompagniaAerea:
    _nome : str # non noto alla nascita
    _fondazione : int #G 1900 <<imm>> noto alla nascita

    def nome(self) -> str:
        return self._nome
    
    def fondazione(self) -> int:  #G greater
        return self._fondazione
    
    
class Citta:
    _nome : str # non noto alla nascita
    _abitanti : int #GEZ non noto alla nascita

    def nome(self) -> str:
        return self._nome
    
    def abitanti(self) -> int: #GEZ greater than or equal zero
        return self._abitanti
    
    
class Nazione:
    nome : str # non noto alla nascita

    def nome(self) -> str:
        return self._nome