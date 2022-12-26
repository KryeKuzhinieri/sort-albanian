# Renditja e fjalëve sipas alfabetit të gjuhës shqipe - Sorting Words Alphabetically in Albanian

Shpeshherë hasim në probleme që kërkojnë radhitjen e germave sipas alfabetit të gjuhës sonë. 
Problemi thellohet edhe më shumë kur gjuha lokale e kompjuterit nuk arrin ta identifikojë alfabetin saktë.
Rrjedhimisht, ky program shërben për renditjen e shkronjave sipas radhitjes së alfabetit të gjuhës shqipe.

### Procesi
Procesi fillon duke i këmbyer germat e përbëra me ato të Alfabetit Fonetik Ndërkombëtar si në vijim:
```python
shkronjat_e_përbëra = {
    "dh": "ð",
    "gj": "ɟ",
    "ll": "ɫ",
    "nj": "ɲ",
    "rr": "r̪",
    "sh": "ʃ",
    "th": "θ",
    "xh": "d͡ʒ",
    "zh": "ʒ",
}
```

Pastaj shkronjat renditen duke përdorur funksionin `sorted` të pythonit.

```python
sorted_words = sorted(
    words,
    key=lambda word: [string_alphabet.index(c) for c in word]
)
```

Së fundmi, shkronjat e përbëra rikthehen në germat e përbëra të gjuhës shqipe.

Pra, i gjithë procesi mund të përmblidhet në hapat e mëposhtëm:

    1. Këmbimi i germave të përbëra me ato të AFN-së.
    2. Renditja duke përdorur `sorted`.
    3. Rikëmbimi i germave të AFN-së me ato të përbëra.


### Testimi
Algoritmi është testuar me disa lista emrash, fjalësh dhe mbiemrash. Si shembull, lista e emrave shqiptarë

```python
TEST_WORDS_1 = [
    "Drenë",
    "Guxim",
    "Erjetë",
    "Ilir",
    "Dedë",
    "Agim",
    "Jetmirë",
    "Symirë",
    "Thëllënëz",
    "Bardhyl",
    "Shpend",
    "Besë",
    "Dhuratë",
    "Çiljetë",
    "Adriatik",
]
```

Renditet kështu sipas funksionit standard të pythonit:
```python
['Adriatik', 'Agim', 'Bardhyl', 'Besë', 'Dedë', 'Dhuratë', 'Drenë', 'Erjetë', 'Guxim', 'Ilir', 'Jetmirë', 'Shpend', 'Symirë', 'Thëllënëz', 'Çiljetë'].
```

Kurse si vijon sipas algoritmit tonë:
```python
['Adriatik', 'Agim', 'Bardhyl', 'Besë', 'Çiljetë', 'Dedë', 'Drenë', 'Dhuratë', 'Erjetë', 'Guxim', 'Ilir', 'Jetmirë', 'Symirë', 'Shpend', 'Thëllënëz']. 
```

Le ta konsiderojmë edhe listën e mëposhtme:

```python
TEST_WORDS_3 = [
    "Thupër",
    "Tytë",

    "Shok",
    "Supë",

    "Dhëmb",
    "Ditë",

    "Gjatë",
    "Gomë",
]
```

Pasi që shkronja `O` vjen pas shkronjës `J`, funksioni i pythonit do ti renditë fjalët "Gjatë" dhe "Gomë" gabimisht. Kjo mund të vërtetohen duke e provuar funksionin `sorted`.
Logjika e njejtë vlen edhe për fjalët e tjera të listës së lartpërmendur.
```python
['Dhëmb', 'Ditë', 'Gjatë', 'Gomë', 'Shok', 'Supë', 'Thupër', 'Tytë'].
```

Ndërsa algoritmi i propozuar paraqet zgjidhjen e saktë:
```python
['Ditë', 'Dhëmb', 'Gomë', 'Gjatë', 'Supë', 'Shok', 'Tytë', 'Thupër']. 
```

### Përmirësimi
Jam i sigurt se ekziston zgjidhje më efikase sa i përket kodit të pythonit andaj
të gjithë ata që kanë sugjerime mund të më kontaktojnë përmes Githubit.

Detyra për veten (apo edhe dikë që është i interesuar): 
    
    1. Testet njësi (Unit testing).
    2. Shndërrimi i kodit në librari të pythonit. 
    3. Uebfaqe për radhitjen e fjalëve pa programim.

Mirë mbetshi!
