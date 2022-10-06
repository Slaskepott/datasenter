## Klasse for representasjon av et datasenter
#
from regneklynge import Regneklynge
from node import Node
class Datasenter:

    ## Oppretter et datasenter
    #
    def __init__(self):
        self._regneklyngeBoka = {}

    ## Leser inn data om en regneklynge fra fil og legger
    # den til i ordboken
    # @param filnavn filene der dataene for regneklyngen ligger
    def lesInnRegneklynge(self, filnavn):
        with open(filnavn,'r') as fil:
            navn = filnavn.replace(".txt","")
            dataliste = []
            for line in fil:
                data = line.strip().split()
                dataliste.append(data)

            nyRegneklynge = Regneklynge(dataliste[0][0])
            i = 1
            while i < len(dataliste):
                linje = dataliste[i]
                #print(f'Leser inn følgende noder til regneklyngen "{navn}":')
                #print(f'Gruppe {i}: {linje[0]} stykker med {linje[1]}GB minne og {linje[2]} prosessorer')
                for node_index in range(int(linje[0])):#antall noder, evaluerer til 264 på saga, 650 på abel
                    nyNode = Node(linje[1],linje[2])
                    nyRegneklynge.settInnNode(nyNode)
                i += 1

            self._regneklyngeBoka[navn] = nyRegneklynge

            #Datalisten inneholder informasjon om en regneklynge
            #Datalisten er en liste med lister. Første liste inneholder max noder per rack
            #Alle lister etter dette er på formatet [AntallNoder,MinnePerNode,ProsessorerPerNode]


    ## Skriver ut informasjon om alle regneklyngene
    #
    def skrivUtAlleRegneklynger(self):
        for key in self._regneklyngeBoka:
            self.skrivUtRegneklynge(key)

    ## Skriver ut informasjon om en spesifikk regeklynge
    # @param navn navnet på regnekyngen
    def skrivUtRegneklynge(self, navn):
        regneklynge = self._regneklyngeBoka[navn]
        print('\n')
        print(f'Regneklyngen {navn} har:')
        print(f'Har {regneklynge.noderMedNokMinne(32)} noder med minst 32GB minne.')
        print(f'Har {regneklynge.noderMedNokMinne(64)} noder med minst 64GB minne.')
        print(f'Har {regneklynge.noderMedNokMinne(128)} noder med minst 128GB minne.')
        print(f'Har {regneklynge.antProsessorer()} prosessorer.')
        print(f'Har {regneklynge.antRacks()} rack.')

    def __str__(self):
        tempList = []
        for key in self._regneklyngeBoka:
            tempList.append(key)
        return f'Dette datasenteret inneholder {tempList}'
