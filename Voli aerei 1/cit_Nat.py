class Nazione:
    _nome : str # non noto alla nascita

    def __init__(self, nome: str):
        self.set_nome(nome) 

    def nome(self) -> str:
        return self._nome
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome



class Citta:
    _nome : str # non noto alla nascita
    _abitanti : int #GEZ non noto alla nascita
    _nazione : Nazione #noto alla nascita


    def __init__(self, nome: str, abitanti: int, nazione:Nazione) -> None:
        self.set_nome(nome)
        self.set_abitanti(abitanti)
        self.set_nazione(Nazione) 

    def nome(self) -> str:
        return self._nome
    
    def abitanti(self) -> int: #GEZ greater than or equal zero
        return self._abitanti
    
    def nazione(self) -> Nazione:
        return self._nazione
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def set_abitanti(self, abitanti: int) -> None:
        self._abitanti = abitanti
    
    def set_nazione(self, nazione: Nazione) -> None:
        self._nazione = Nazione


    
italia = Nazione("italia")
citta = Citta("Roma", 2746789, italia)

nome_citta = citta.nome()
abitanti_citta = citta.abitanti()

print(f"Il nome della citta è: {nome_citta}")
print(f"Gli abitanti nel 2025 sono: {abitanti_citta}")

nazione = Nazione("Italia <3")

nome_nazione = nazione.nome()

print(f"La nazione della capitale è: {nome_nazione}")
    
    # Una aggregazione identifica una relazione "has-a" (ha-un)
    # la navigabilità: l'associazione può essere "navigata" solo in quel verso

                        #....................#                 #....................#
                        #                    #                 #                    #
       #vinc.molt.0..*  #       Citta        # <---cit_naz---- #       Nazione      #   vinc.molt. 1..1
                        #                    #                 #                    #
                        #....................#                 #....................#