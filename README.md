<h1> Klasifikacija pisaca na osnovu odlomka iz romana </h1>

<h3> Ukratko o projektu </h3>
<p>
Tema ovog projekta rada jeste klasifikacija pisaca na osnovu odlomaka iz
različitih romana. Cilj jeste da se koristeći model mašinskog učenja prepozna da li je
određeni pasus napisao pisac Ivo Andrić ili Meša Selimović. Model mašinskog
učenja je u ovom slučaju bila 1D konvolutivna neuronska mreža. U daljem tekstu,
objašnjen je način pripremanja podataka, obrade istih, kao i rezultati primene
algoritma na te podatke. </p>

<br> <br>
<h3>Skup podataka</h3>
<p>Skup podataka nad kojim sam radio ovo istraživanje sam morao da napravim sam,
skripta koja pravi csv fajl se takođe nalazi u mom github repozitorijumu. Dakle, uzeo
sam 2 knjige od Ive Andrića i 2 knjige od Meše Selimovića. Učitao PDF fajlove, njih
pretvorio u listu stringova dužine 500 karaktera (morao sam da imam fiksnu dužinu
pasusa jer CNN zahteva fiksni ulaz). Na kraju, skup podataka je imao 1650 pasusa u
prvoj koloni i prezime pisca u drugoj (podaci se nalaze u „pisci.csv“). Prilikom
obrade PDF fajlova, imao sam problem sa enkodiranjem specijalnih karaktera kao što
su karakteri: „š, č, ć , đ, ž“ koje sam regularnim izrazima popravio.</p>

<br> <br>
<h3>Pretprocesiranje podataka</h3>
<p>Pošto sam ja napravio skup podataka, znao sam da u njemu nema nedostajućih
vrednosti, kao ni duplikata. Kao što sam ranije napomenuo, osnovno pretprocesiranje
je urađeno u fazi pravljenja skupa podataka. Prvo šta sam morao da popravim bio je
ciljni atribut „pisac“. Taj atribut je kategoricki nominalan atribut, pa sam zbog toga
morao da za svaku kategoriju koja postoji napravim posebnu kolonu, gde će vrednost
u toj koloni da bude nula ili jedan u zavisnosti od toga da li konkretni entitet pripada
toj kategoriji. U ovom slučaju postojale su dve kategorije, „selimovic“ i „andric“.
Binarizaciju sam uradio pomoću funkcije get_dummies. Nad prvom kolonom
nažalost nisam mogao da radim nikakav Stemming (lematizacije) jer nisam pronašao
ni jedan stemmer prilagođen srpskom jeziku. Takođe nisam imao ni popularnu stop
listu reči, jer nigde nisam uspeo da pronađem stop listu za naš jezik. Jedina obrada
prve kolone bila je pomoću tokenizera, pretvorio sam reči u sekvence. Gde sam
uzimao samo 10 hiljada najfrekventnijih reči u obzir, a ostale se nisu razmatrale. Na
kraju, podatke smo podelili na trening i testne funkcijom train_test_split, gde je 25%
ukupnog skupa pripalo testnim podacima.</p>

<br> <br>
<h3>Obučavanje i evaluacija modela</h3>
Skup za obučavanje ćemo podeliti na dva nova skupa, jedan će biti skup na kome će se zapravo vršiti obučavanje (80% originalnog skupa za obučavanje), a validacioni skup ćemo koristiti da na kraju svake epohe evaluiramo koliko je dobar naš model.
Obučavaćemo model 20 epoha i čuvaćemo tačnost na podacima za obučavanje i validaciju tokom treninga.
Možemo primetiti da je 20 epoha previše i da puštanje obučavanja da toliko dugo traje ne doprinosi tačnosti modela. Ponovićemo optimizacioni proces ponovo, ali ovaj put ćemo koristiti tehniku ranog zaustavljanja (eng. early stopping).
<br>
Ideja je definisati skup ograničenja koja kad se ispune, obučavanje modela će biti zaustavljeno. Na primer, ukoliko se u k uzastopnih epoha ne poboljša vrednost "acc" ima smisla zaustaviti obučavanje.

<br>
Treba pomenuti da je gotovo sigurno mali skup podataka, i to što su tekstovi pisani na srpskom jeziku dosta uticalo na sam rezultat.
Naš model od 199 pasusa, dobro klasifikuje 153 pasusa.<br>
Rezultati su sledeći:<br>
Preciznost: 0.853<br>
Recall skor: 0.646<br>
F1: 0.736<br>

