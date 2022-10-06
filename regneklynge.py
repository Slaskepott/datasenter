## Klasse for representasjon av regneklynge i et datasenter.
#
from rack import Rack
class Regneklynge:
    ## Oppretter en regneklynge og setter maks antall
    # det er plass til i et rack
    # @param noderPerRack max antall noder per rack
    def __init__(self, noderPerRack):
        self._noderPerRack = int(noderPerRack)
        self._racks = []

    ## Plasserer en node inn i et rack med ledig plass, eller i et nytt
    # @param node referanse til noden som skal settes inn i datastrukturen
    def settInnNode(self, node):
        if self._racks:
            ledigRack = None
            for rack in self._racks: #Leter etter ledig rack
                antall = rack.getAntNoder()
                if self._noderPerRack > rack.getAntNoder(): #Sjekk om det er plass i racket.
                    ledigRack = rack
            if ledigRack != None:
                ledigRack.settInn(node)
        if not self._racks or ledigRack == None: #Hvis det enten ikke finnes racks, eller alle er fulle
            nyttRack = Rack()
            nyttRack.settInn(node)
            self._racks.append(nyttRack)

    ## Beregner totalt antall prosessorer i hele regneklyngen
    # @return totalt antall prosessorer
    def antProsessorer(self):
        antallProsessorer = 0
        if self._racks:
            for rack in self._racks:
                antallProsessorer += rack.antProsessorer()
        return antallProsessorer

    ## Beregner antall noder i regneklyngen med minne over angitt grense
    # @param paakrevdMinne hvor mye minne skal noder som telles med ha
    # @return antall noder med tilstrekkelig minne
    def noderMedNokMinne(self, paakrevdMinne):
        noderMedNokMinne = 0
        if self._racks:
            for rack in self._racks:
                noderMedNokMinne += rack.noderMedNokMinne(paakrevdMinne)
        return noderMedNokMinne


    ## Henter antall racks i regneklyngen
    # @return antall racks
    def antRacks(self):
        return len(self._racks)

    def __str__(self):
        return f'Denne regneklyngen inneholder {self.antRacks()} racks. Den har {self.noderMedNokMinne(32)} noder med 32GB eller mer og {self.antProsessorer()} prosessorer.'
