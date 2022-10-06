class Node:
    ## Oppretter en node med gitt minne-storrelse og antall prosessorer
    #  @param minne GB minne i den nye noden
    #  @param antPros antall prosessorer i den nye noden
    def __init__(self, minne, antPros):
        self._minne = minne
        self._antPros = antPros

    ## Henter antall prosessorer i noden
    #  @return antall prosessorer i noden
    def antProsessorer(self):
        return self._antPros

    ## Sjekker om noden har tilstrekkelig minne for et program
    #  @param paakrevdMinne GB minne som kreves for programmet
    #  @return True hvis noden har minst så mye minne
    def nokMinne(self, paakrevdMinne):
        assert paakrevdMinne >= 0
        if int(self._minne) >= paakrevdMinne:
            return True
        return False

    def __str__(self):
        return f'Denne noden har {self._minne}GB minne og {self._antPros} prosessorer.'
