# Coleta BIO

Aplicativo desenvolvido para um projeto de biologia da faculdade, voltado ao registro de coletas volumétricas de espécies de plantas nativas da Caatinga (Aroeira, Angico, Jurema Preta, Marmeleiro, entre outras).

O app permite preencher formulários de coleta, salvar os dados na nuvem (Firebase Realtime Database), consultar relatórios históricos e visualizar gráficos comparativos entre as espécies.

## Funcionalidades

- **Coleta**: formulário por espécie para registrar o volume coletado (ml).
- **Relatórios**: listagem expansível das coletas anteriores agrupadas por data.
- **Indicadores**: gráfico de barras com a média volumétrica por espécie em uma data selecionada.
- **Espécies**: ficha descritiva com foto e informações de cada planta observada.
- **Modo offline**: os dados são persistidos localmente em `assets/data/temporary_data.json` e sincronizados com o Firebase quando há conexão.

## Stack

- [Flet](https://flet.dev/) 0.84 (UI multiplataforma em Python)
- `flet-charts` para o gráfico de barras
- Firebase Realtime Database (via REST)
- `python-dotenv` para configuração

## Setup

Requer Python 3.11+.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Crie um arquivo `.env` na raiz do projeto com a URL do seu Firebase:

```
DATABASE_URL=https://<seu-projeto>.firebaseio.com
```

## Executando

```bash
python main.py
```

Ou via CLI do Flet (com hot reload):

```bash
flet run
```

## Estrutura

```
app_coletabio/
├── main.py                      # entrypoint
├── assets/
│   ├── config.py                # carrega DATABASE_URL do .env
│   ├── data/                    # JSONs locais (especies, info, buffer de coleta)
│   ├── models/                  # acesso a dados e regras (firebase, plants, reports, indicators)
│   ├── views/                   # telas (home, collect, reports, indicators, plants)
│   ├── widgets/                 # componentes compartilhados (navbar, appbar)
│   └── *.png                    # imagens das espécies e logo
└── requirements.txt
```

## Telas

**Home**
<img width="373" height="663" alt="image" src="https://github.com/user-attachments/assets/a8c75ab3-ce78-4bfe-ba84-fc42d587e5ee" />

**Espécies**
<img width="375" alt="Tela de espécies" src="https://github.com/user-attachments/assets/98bb3735-ff80-418d-9a12-89b1954b271b" />

**Coleta**
<img width="374" height="665" alt="image" src="https://github.com/user-attachments/assets/b41c97e2-5ccf-4378-af2e-93417b0f9024" />

**Indicadores**
<img width="377" height="670" alt="image" src="https://github.com/user-attachments/assets/995743ff-6ec0-4cc3-92bf-73afee45c8a0" />

**Relatórios**
<img width="370" height="662" alt="image" src="https://github.com/user-attachments/assets/60b76fd6-1069-4963-9a49-4f8917a33115" />

