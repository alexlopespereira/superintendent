from superintendent import Superintendent
from ipyannotations.text import ClassLabeller
import os
import ipywidgets as widgets
import pandas as pd
# from IPython import display
dfm = pd.read_json("../data/licitacoes_trilha18_chunks_elastic_rotulado_auditor.json")
user = os.getenv('POSTGRES_USER', "superintendent")
pw = os.getenv('POSTGRES_PASSWORD', "superintendent2022lewagonAlice")
db_name = os.getenv('POSTGRES_DB', "labelling")
db_host = os.getenv('POSTGRES_HOST', "db")

db_string = f"postgresql+psycopg2://{user}:{pw}@{db_host}:5432/{db_name}"
worker_dropdown = widgets.Dropdown(
    options=['Alex', 'Bruno', 'Erick', 'Gustavo'],
    description='Rotolador:',
    disabled=False,
)
input_widget = ClassLabeller(options=['alerta procedente', 'alerta inprocedente'])
input_data = dfm['chunk']
data_labeller = Superintendent(
    features=input_data,
    labelling_widget=input_widget,
    database_url=db_string,
    worker_id=worker_dropdown.get_interact_value()
)

data_labeller._begin_annotation()
print(data_labeller)
