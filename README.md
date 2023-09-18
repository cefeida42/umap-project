# Klasifikacija galaksija, zvezda i kvazara u pripremi za LSST
*Prednosti i mane UMAP algoritma*

# UVOD

LSST je desetogodišnji fotometrijski pregled neba sa planiranim početkom operacija u prvoj polovini 2024. godine. Tokom svog staža, LSST će prikupiti ~300 PB sirovih podataka o ~4 x 10^10 astrofizčkih objekata i isporučiti legat u vidu kataloga veličine ~15 PB koji će sadržati uređene informacije o svim detektovanim objektima. Jedan od glavnih zadataka u procesu kreiranja kataloga je klasifikacija objekata, a s obzirom da se radi o ogromnoj količini podataka, automatizovana klasifikacja je imperativ.

U ovom projektu ćemo istražiti mogućnosti Uniform Manifold Approximation and Projection (UMAP) algoritma u svrhu ne samo klasifikacije astrofizičkih objekata, već i topološke analize prostora podataka sa kojim bi LSST raspolagao. UMAP je algoritam za smanjenje dimenzionalnosti i spada u grupu nelinearnih metoda. Dizajniran je tako da očuvava lokalnu strukturu mnogostrukosti poput t-SNE i sličnih algoritama, ali za razliku od njih, efikasan je u očuvanju strukture i na globalnim skalama. Cilj ovog projekta je da se proveri da li postoje prednosti u ovakvoj reprezentaciji multidimenzionalnih podataka i da li je moguće efikasno iskoristiti dobijene reprezentacije u nadgledanoj, nenadgledanoj i polu-nadgledanoj klasifikaciji. Ukoliko vreme dozvoli, istražićemo i uticaj outlier-a na dobijanje konačnih projekcija koristeći [Robust LLE metod](https://github.com/cefeida42/agndc-contrib/blob/main/RLLE.py) koji je baziran na radu [Chang & Yeung (2006)](https://www.sciencedirect.com/science/article/abs/pii/S0031320305003353).

# PODACI

Za ovaj eksperiment, poslužićemo se AGN Data Challenge setom podataka koji je sastavljen baš u svrhu testiranja različitih metoda na podacima kakve očekujemo od LSST-a. Ovaj uzorak se sastoji od 440,000 objekata od kojih je 55% galaksija, ~25% zvezda i ~20% aktivnih galaktičkih jezgara. Uzorak sadrži 374 parametra koji se mogu raščlaniti na nekoliko kategorija: fotometrijska merenja, boje, astrometrija, morfologija, parametri svetlosnih krivih, crveni pomak i ciljne promenljiive u vidu klasa.


# PREDLOG RADNIH CELINA

1. Priprema podataka (eksplorativna analiza, odabir parametara, skaliranje podataka, osvrt na problem disbalansa klasa)
2. Primena UMAP u nadgledanom režimu
3. Primena UMAP u nenadgledanom režimu
4. Primena UMAP u polu-nadgledanom režimu
5. Analiza dobijenih projekcija, mere kvaliteta modela i diskusija

6. OPCIONI DODATAK 1: Testiranje uticaja outliera na mere kvaliteta modela i projekcija
- poređenje Robust LLE metode za otklanjanje outliera sa nekim od konvencionalnih metoda već implementiranih u scikit-learn.

7. OPCIONI DODATAK 2: UMAP kao alat za odabir najkorisnijih parametara za treniranje
- ovde sam imala ideju da definišemo osnovni skup parametara koji podrazumeva samo fotometrijske podatke, a ostale parametre (pretežno one dobijene iz svetlosnih krivih) da testiramo ubacivanjem i izbacivanjem u UMAP. Mera korisnosti bi mogla biti relativna udaljenost klastera normalizovana u odnosu na bounding box koji sadrži celu projekciju. Na ovaj način bi možda uspeli da pronađemo recimo 10 najboljih parametara (od njih 300) koji bi nam davali najveća razdvajanja u projekcijama, a samim tim bi znali da su to parametri koji nose više relevantnih inforamcija za razdvajanje klasa. Prednost ovog pristupa u odnosu na prosto ubacivanje svih parametara odjednom je to što dodavanjem svakog novog parametra gubimo na veličini uzorka jer nisu svi izmereni za sve objekte. Prema nekim preliminarnim testovima ovakav eksperiment bi mogao da oduzme ~10 sati rada na ličnom računaru.


# LITERATURA
- [Chang & Yeung (2006) - Robust Locally Linear Embedding](https://www.sciencedirect.com/science/article/abs/pii/S0031320305003353)
- [Clarke et al. (2020) - Identifying galaxies, quasars, and stars with machine learning: A new catalogue of classifications for 111 million SDSS sources without spectra](https://ui.adsabs.harvard.edu/abs/2020A%26A...639A..84C/abstract)
- [McInnes et al. (2018) - UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction](https://arxiv.org/abs/1802.03426)




