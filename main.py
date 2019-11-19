import argparse


def analyser_commande():
    parser = argparse.ArgumentParser()
    parser.add_argument('idul', help="IDUL du joueur.")
    parser.add_argument("-l", "--lister", help="Lister les identifiants de vos 20 dernière parties")
    return parser.parse_args()

import api


def afficher_damier_ascii(dicio):
    damier = [['Légende:  1 = idul,  2=automate','|','.'* 9, '|']] #commande incomplète
    print(damier)