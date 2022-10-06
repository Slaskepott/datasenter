## Klasse for representasjon av racks i en regneklynge.
#
from node import Node
class Rack:
    ## oppretter et rack der det senere kan plasseres noder
    #
    def __init__(self):
        self._noder = []

    ## Plasserer en ny node inn i racket
    #  @param node noden som skal plasseres inn
    def settInn(self, node):
        self._noder.append(node)

    ## Henter antall noder i racket
    # @return antall noder
    def getAntNoder(self):
        return len(self._noder)

    ## Beregner sammenlagt antall prosessorer i nodene i et rack
    # @return antall prosessorer
    def antProsessorer(self):
        antPros = 0
        assert self._noder
        for node in self._noder:
            antPros += int(node.antProsessorer())
        return antPros


    ## Beregner antall noder i racket med minne over gitt grense
    # @param paakrevdMinne antall GB minne som kreves
    # @return antall noder med tilstrekkelig minne
    def noderMedNokMinne(self, paakrevdMinne):
        antNoderMedNokMinne = 0
        assert self._noder
        for node in self._noder:
            if node.nokMinne(paakrevdMinne):
                antNoderMedNokMinne += 1
        return antNoderMedNokMinne

    def __str__(self):
        return f'Dette racket inneholder {self.getAntNoder()} noder.'
