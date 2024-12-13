# 🚲 Proyecto API y MongoDB - Bicicorunha

## Índice

1. [Descripción](#descripción)
2. [Instalación](#instalación)
3. [Script 1: Conexión á API e Almacenamento en MongoDB](#script-1-conexión-á-api-e-almacenamento-en-mongodb)
   - [Funcionalidade](#funcionalidade)
   - [Requisitos](#requisitos)
   - [Instalación](#instalación-1)
4. [Script 2: Lectura de MongoDB e Exportación a Pandas](#script-2-lectura-de-mongodb-e-exportación-a-pandas)
   - [Funcionalidade](#funcionalidade-1)
   - [Requisitos](#requisitos-1)
   - [Instalación](#instalación-2)

---

## 📝 Descripción

Este repositorio contén dous scripts que interactúan cunha API pública e MongoDB. O primeiro script conecta á API de CityBike e almacena os datos de estacións de bicicletas en MongoDB a intervalos regulares. O segundo script consulta a base de datos de MongoDB, recupera os datos almacenados, crea un DataFrame de pandas e exporta os datos en formatos CSV e Parquet.

Este proxecto permite a integración de datos en tempo real e a súa manipulación mediante pandas para análise ou exportación.

---

## 🔧 Instalación

### Clonar o Repositorio

Para comezar, clona este repositorio utilizando o seguinte comando:
```bash
git clone git@github.com:RaulEP-7/ProyectoSistemas-Raul.git
cd ProyectoSistemas-Raul
```
## 🚀 Script 1: Conexión á API e Almacenamento en MongoDB

### 🛠 Funcionalidade

- Conéctase á API de CityBike a intervalos regulares (cada 10 segundos).
- Obtén os datos de resposta da API.
- Almacena os datos na base de datos MongoDB.
- A execución do script continúa ata que se cancele manualmente (funciona en modo infinito).

### 🧩 Requisitos

- Python 3.x
- MongoDB
- Librerías necesarias:
  - `requests`
  - `pymongo`
  
### 🔧 Instalación

1. Instala as dependencias necesarias:
    ```bash
    pip install requests pymongo
    ```
2. Executa o script:
    ```bash
    python script_1.py
    ```

---

## 🐍 Script 2: Lectura de MongoDB e Exportación a Pandas

### 🛠 Funcionalidade

- Lé os datos almacenados na base de datos MongoDB.
- Filtra os documentos para exportar só os campos necesarios: `id`, `name`, `timestamp`, `free_bikes`, `empty_slots`, `uid`, `last_updated`, `slots`, `normal_bikes` e `ebikes`.
- Almacena os datos nun DataFrame de pandas.
- Exporta os datos a dous formatos:
  - **CSV**
  - **Parquet**

### 🧩 Requisitos

- Python 3.x
- MongoDB
- Librerías necesarias:
  - `pandas`
  - `pymongo`
  
### 🔧 Instalación

1. Instala as dependencias necesarias:
    ```bash
    pip install pandas pymongo
    ```
2. Executa o script:
    ```bash
    python script_2.py
    ```

---

