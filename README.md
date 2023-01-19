# Generator parafraz

## Cel projektu

Celem projektu było stworzenie generatora parafraz wykorzystującego bazy API do mapowania słów na ich odpowiedniki lub też dodawanie przymiotników do słów już istniejących. Wykorzystuję w tym celu poniższe API:
- [ ]   https://www.datamuse.com/api/
- [ ]   https://poetrydb.org/index.html
- [ ]	https://docs.genius.com/

## Układ projektu
Cały projekt składa się z 5 głównych modułów:
1.	ui_paraphrase_generator.py – plik wygenerowany w programie zewnętrznym Qt Designer, w którym został zaprojektowany graficzny interfejs użytkownika (gui). Zawiera jedną klasę, Ui_MainWindow.
2.	gui.py – moduł, który uruchamia program. Zawiera jedną klasę, ParaphraseGeneratorWindow, która dziedziczy po klasie z wyżej wspomnianego modułu. Przypisuje ona każdemu obiektowi w interfejsie graficznym odpowiednie działanie, korzystając reszty modułów, łącząc je w jedną całość.
3.	operations.py – moduł ten zawiera funkcje do operacji na danych wejściowych, tzn.: na tekstach piosenek i wierszy. Funkcje pozwalają parafrazować wybrane słowa na ich odpowiedniki znalezione w bazie danych lub dodawać do nich przymiotniki opisujące je.
4.	poem.py – moduł zawiera dwie klasy: Author i Poem. Pierwsza z nich służy do przechowywania autorów i pobierać listę wszystkich wierszy napisanych przez nich, znalezionych w bazie danych. Druga natomiast pozwala przechowywać same wiersze i pobierać ich teksty z bazy. Moduł posiada też funkcję do pobrania wszystkich autorów znalezionych w bazie.
5.	song.py – moduł zawiera klasę, która pozwala przechowywać piosenki oraz funkcję służącą do wyszukiwania danego utworu w bazie danych geniusa.
Poza opisanymi wyżej modułami do projektu należą również:
- [ ]	errors.py – zawiera w sobie własne możliwe wyjątki (exceptions),
- [ ]	testy do modułów opisanych w podpunktach: 3, 4, 5.

## Opis projektu
Generator parafraz oferuje możliwość wyszukania tekstu piosenki w bazie tekstów Genius. Aby otrzymać teksty wystarczy podać tytuł piosenki, a dla większej dokładności również wykonawcę. Po wyszukaniu tekst piosenki automatycznie zostaje dodany jako tekst wejściowy. 
Można również przełączyć się na okno do wyszukiwania wierszy i wybrać kolejno autora i jego dzieło, które po kliknięciu analogicznie zostanie dodane jako tekst wejściowy.

Program pozwala użytkownikowi na sparafrazowanie podanego tekstu na jeden z pięciu sposobów:
- [ ]	zamiana podanych słów na:
-- [ ]	rymy
-- [ ]	synonimy
-- [ ]	homofony
-- [ ]	homonimy
- [ ]	dodanie do podanych słów dodatkowych czasowników

Istnieje możliwość podania maksymalnie 10 słów do sparafrazowania. Zastosowałem ten górny margines, aby program działał stosunkowo szybko. Dla każdego z podanych słów kluczy jest pobierane, a następnie przypisywane mu, jedno wyrażenie. Słowa podane są następnie zamieniane lub dodawane są do nich pobrane wyrażenia. Po zakończonym procesie tekst wypisywany jest na wyjściu. Wszystkie funkcje, klasy i ich metody, są bardziej szczegółowy opis w postaci docstringów.

## Zmiany podczas pracy

Początkowo plan projektu był nieco inny, a dokładniej parafrazowane miało być każde słowo tekstu, które miało przypisane wyrażenie w bazie danych. Po implementacji tego rozwiązania okazało się, że zastosowanie to działa dla krótkich tekstów (np.: 1 zdanie), natomiast dla tekstów, które według polecenia miały być danymi wejściowymi (tj. teksty piosenek i wiersze) proces parafrazowania trwał czasem ponad minutę. Wynikało to konieczności łączenia się z API przy każdym słowie, co znacząco wpływało na wydajność czasową programu. 
Zastosowanie systemu słów kluczy, które mają zostać sparafrazowane, poza znacznym przyspieszeniem działania, daje większą kontrolę nad samym procesem, a jego efekt jest spójniejszy i logiczniejszy językowo.

## Rzeczy do poprawy w przyszłości

Podczas robienia projektu myślałem nad implementacją kilku dodatkowych funkcji, czego nie zrobiłem z kilku różnych opisanych niżej powodów:
1.	Do opcji parafrazowania: dodanie opcji do jednoczesnego zamieniania wybranego słowa na jego parafrazę i dodawania przymiotnika, wszystko podczas jednego przejścia przez tekst w pętli. Ostatecznie uznałem, że można uzyskać ten sam efekt kopiując uzyskany efekt jednej operacji, a następnie przeprowadzić na nim drugą, więc ten dodatek nie jest konieczny.
2.	Do systemu wyszukiwania piosenek: dodanie opcji pokazania najbardziej pasujących wyników do wpisanych fraz, które następnie można wybrać jako tekst wejściowy. Byłaby to przydatna funkcja w przypadkach, gdy uzyskany tekst nie jest tym, którego oczekiwał użytkownik. Jednak nie mogłem znaleźć odpowiednich funkcji dla API geniusa, które pozwoliłyby mi na implementacje tego pomysłu.