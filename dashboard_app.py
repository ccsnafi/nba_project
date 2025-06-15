import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression

# Chargement des données et du modèle
@st.cache_data
def load_data_and_model():
    df = pd.read_csv("data/Seasons_Stats.csv")
    players = pd.read_csv("data/Players.csv")

    df = df.drop(columns=['blanl', 'blank2'], errors='ignore')
    df = df.dropna(subset=['Year', 'Player'])
    df['Year'] = df['Year'].astype(int)
    df['PTS_per_game'] = df['PTS'] / df['G']
    df['Era'] = (df['Year'] // 10) * 10
    players = players.drop(columns=['Unnamed: 0'], errors='ignore')
    df = pd.merge(df, players, on="Player", how="left")
    df['Pos_encoded'] = df['Pos'].astype('category').cat.codes

    # Entraînement du modèle
    features = ['Age', 'height', 'weight', 'MP', 'FGA', 'FTA', '3PA', 'Pos_encoded']
    model_data = df[features + ['PTS_per_game']].dropna()
    X = model_data[features]
    y = model_data['PTS_per_game']
    model = LinearRegression().fit(X, y)

    return df, model

df, model = load_data_and_model()

st.title("🏀 Dashboard NBA - Analyse & Simulation de Performance")

# ----------- PARTIE 1 : VISUALISATIONS ----------------
st.header("📈 Visualisations NBA")

year = st.slider("Sélectionnez une année", int(df['Year'].min()), int(df['Year'].max()), 2000)
pos = st.selectbox("Poste", ["Tous"] + sorted(df['Pos'].dropna().unique().tolist()))
era = st.selectbox("Décennie", ["Toutes"] + sorted(df['Era'].dropna().unique().astype(int).tolist()))

filtered = df[df['Year'] == year]
if pos != "Tous":
    filtered = filtered[filtered['Pos'] == pos]
if era != "Toutes":
    filtered = df[df['Era'] == int(era)]

st.subheader("Top 10 des joueurs par Points par match")
top10 = filtered.sort_values(by="PTS_per_game", ascending=False).head(10)
st.dataframe(top10[['Player', 'Year', 'PTS_per_game', 'Pos', 'Tm']])

fig = px.bar(top10, x='Player', y='PTS_per_game', color='Tm', title="Top 10 Scoreurs")
st.plotly_chart(fig)

# ----------- PARTIE 2 : PRÉDICTION PERSONNALISÉE ----------------
st.header("🎯 Simulation : prédire les points/match d'un joueur")

st.markdown("**Remplis les caractéristiques ci-dessous :**")

age = st.slider("Âge", 18, 40, 25)
height = st.slider("Taille (cm)", 160, 230, 198)
weight = st.slider("Poids (kg)", 60, 150, 95)
mp = st.slider("Minutes jouées par match", 0, 48, 30)
fga = st.slider("Tirs tentés (FGA)", 0, 40, 15)
fta = st.slider("Lancers francs tentés (FTA)", 0, 20, 5)
three_pa = st.slider("3 points tentés (3PA)", 0, 15, 5)
pos_list = df['Pos'].astype('category').cat.categories.tolist()
pos_selected = st.selectbox("Poste", pos_list)
pos_encoded = df[df['Pos'] == pos_selected]['Pos_encoded'].iloc[0] if not df[df['Pos'] == pos_selected].empty else 0

# Prédiction
features = [[age, height, weight, mp, fga, fta, three_pa, pos_encoded]]
predicted_pts = model.predict(features)[0]

st.success(f"🏀 Ce joueur marquerait environ **{predicted_pts:.2f} points par match** selon le modèle.")

st.caption("Données issues de Kaggle | Modèle : Régression Linéaire")
