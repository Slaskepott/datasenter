from datasenter import Datasenter
#__init__(self),lesInnRegneklynge(self, filnavn),skrivUtAlleRegneklynger(self),skrivUtRegneklynge(self, navn)
from regneklynge import Regneklynge
#__init__(self, noderPerRack),settInnNode(self, node),_settInnRack(self,rack),antProsessorer(self),noderMedNokMinne(self, paakrevdMinne),antRacks(self)
from rack import Rack
#__init__(self), settInn(self, node), getAntNoder(self),antProsessorer(self),noderMedNokMinne(self, paakrevdMinne)
from node import Node
#__init__(self, minne, antPros), antProsessorer(self), nokMinne(self, paakrevdMinne)

def node_tester():
    minNode = Node(56,2) #minne, antall prosessorer
    assert minNode.antProsessorer() == 2
    assert not minNode.nokMinne(57)
    assert minNode.nokMinne(55)

def rack_tester():
    mittRack = Rack()
    for i in range(5):
        nyNode = Node(56,2)
        mittRack.settInn(nyNode)
    for i in range(5):
        nyNode = Node(112,4)
        mittRack.settInn(nyNode)
    assert mittRack._noder
    assert mittRack.getAntNoder() == 10
    assert mittRack.antProsessorer() == 30 # 5*4 + 5*2 = 30
    assert mittRack.noderMedNokMinne(57) == 5
    assert mittRack.noderMedNokMinne(55) == 10
    assert mittRack.noderMedNokMinne(113) == 0

def regneklynge_tester():
    minRegneklynge = Regneklynge(5)
    for i in range(100):
        minRegneklynge.settInnNode(Node(56,2))
    assert len(minRegneklynge._racks) == 20
    assert minRegneklynge.antProsessorer() == 200
    assert minRegneklynge.noderMedNokMinne(57) == 0
    assert minRegneklynge.noderMedNokMinne(56) == 100
    assert minRegneklynge.antRacks() == 20

def datasenter_tester():
    mittDatasenter = Datasenter()
    mittDatasenter.lesInnRegneklynge('saga.txt')
    mittDatasenter.lesInnRegneklynge('abel.txt')
    mittDatasenter.skrivUtRegneklynge('abel')
    mittDatasenter.skrivUtAlleRegneklynger()

node_tester()
rack_tester()
regneklynge_tester()
datasenter_tester()
