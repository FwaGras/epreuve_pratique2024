class Noeud:
    def __init__(self, etiquette):
        '''Méthode constructeur pour la classe Noeud.
        Crée une feuille d'étiquette donnée.'''
        self.etiquette = etiquette
        self.gauche = None
        self.droit = None

    def inserer(self, cle):
        '''Insère la clé dans l'arbre binaire de recherche
        en préservant sa structure.'''
        if cle < self.etiquette:
            if self.gauche != None:
                self.gauche.inserer(cle)
            else:
                self.gauche = Noeud(cle) 
        else:
            if self.droit != None:
                self.droite.inserer(cle)
            else:
                self.droit = Noeud(cle) 
                
arbre = Noeud(7)
for cle in (3, 9, 1, 6):
        arbre.inserer(cle)

assert arbre.gauche.etiquette == 3, "oups"
assert arbre.gauche.gauche.etiquette == 1, "oups"
assert arbre.gauche.droit.etiquette == 6, "oups"