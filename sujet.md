# Sujet de Projet Data Science : Analyse des Performances NBA depuis 1950

## Contexte
La NBA regroupe certaines des plus grandes légendes du sport. L'évolution du jeu, des règles et des athlètes a fortement influencé les statistiques. Ce projet explore les données NBA depuis 1950.

## 🏀 Comprendre les postes NBA

Chaque joueur dans le dataset est associé à un **poste**, qui détermine son rôle sur le terrain. Cela permet d’analyser les différences de performance selon les profils (scoreurs, rebondeurs, etc.).

Voici les postes principaux :

| Poste | Abréviation | Description |
|-------|-------------|-------------|
| **Meneur** | `PG` *(Point Guard)* | Organise le jeu, distribue les passes, dirige l’attaque. |
| **Arrière** | `SG` *(Shooting Guard)* | Bon tireur, souvent l’un des meilleurs marqueurs. |
| **Ailier** | `SF` *(Small Forward)* | Polyvalent, capable de défendre, pénétrer et tirer. |
| **Ailier fort** | `PF` *(Power Forward)* | Puissant et efficace proche du panier. |
| **Pivot** | `C` *(Center)* | Le plus grand joueur, spécialiste des rebonds et contres. |

> Certains joueurs sont multi-postes, ex. `G-F` (meneur/ailier) ou `F-C` (ailier fort/pivot).

Cette catégorisation est utilisée pour :
- Comparer les performances moyennes par poste
- Entraîner des modèles prédictifs en tenant compte du poste
- Filtrer les visualisations dans le dashboard

## Objectif
- Explorer l’évolution des statistiques individuelles (points, rebonds, etc.)
- Comparer les performances par poste et par époque
- Construire un modèle prédictif simple (ex. : prédiction du scoring)
- Créer un dashboard interactif pour visualiser les insights

## Dataset
Source : Kaggle  
- Seasons_Stats.csv
- Players.csv

## Raisons du choix
- Sujet grand public et passionnant
- Données riches et propres
- Parfait pour analyse temporelle et modélisation légère
