# Podstawowe typy danych w Pythonie
# 1. Liczby całkowite (eng. integers, w Pythonie `int`): 0, 1, -2, etc. Są wykorzystywane do specyficznych danych liczbowych w których nie występują ułamki, na przykład ponumerowane objekty. Iloraz liczb całkowitych może nie być całkowity dlatego często do tego typu liczb stosuje się dzielenie z resztą. Generalnie podstawowy język nie definiuje symbolu dla nieskończoności, ale za to można definiować bardzo duże liczby - tak duże jak pozwala dostępna pamięć dla interpretera pythona pmięci.
#
# 2. Typ boolean (`bool`): `True`, `False`. Ułatwiają wykorzystywanie w kodzie wartości prawda/fałsz i zwiększają jego czytelność. Są traktowane jako 0, 1 przez interpreter Pythona (`False == 0`, `True == 1`)
#
# 3. Liczby zmiennoprzecinkowe (`float`): 3.14, 2.73, 0.0, -1.23, etc. Są wykorzystywane do danych liczbowych oznaczających ilość czegoś, na przykład masa, cena. Nie istnieją rozwinięcia nieskończone ani definiowanie ułamków zwykłych. Nie da się w podstawowym języku ustalić, że liczby będą podawane z dokładnością do zadanego miejsca po przecinku - podczas wykonywania działań matematyczny, szczególnie dzielenia, wszystko zależy architektury komputera.
#
# 4. Napisy (string, w Pythonie `str`): "abc", 'typ danych', "a)jda8ld)%#'". Sekwencja znaków zawarta pomiędzy "" lub ''. Nie ma osobnego typu dla znaków- na przykład 'a' to string o długości 1. Raz stworzony napis nie może zostać w żaden sposób zmieniony - operacje na nim skutkują stworzeniem nowego napisu.
#
# 5. `None`, typ pusty - nie jest to 0 ani False, ani "", ani [].

# Podstawowe operatory w Pythonie
#
# Operatory to symbole i słowa kluczowe służące do wykonywania działań na wartościach. Poniższe sekcje grupują je według zastosowania i rodzajów wartości, na których działają. Każdy operator ma krótki opis, a po nim znajduje się przykład do uruchomienia.

# ## Operatory porównania
print("Operatory porównania")
#
# Operatory porównania zestawiają dwie wartości i zwracają wartość logiczną: `True` albo `False`. Porównywanie typów liczbowych jest intuicyjne. Stringi są porównywane na zasadzie, czy te same symbole są w takiej samej kolejności. Do porównywania obiektów ze sobą oraz z None wykorzystywane jest `is`.

# `==` sprawdza, czy dwie wartości są równe.
print(7 == 3)  # False

# `!=` sprawdza, czy dwie wartości są różne.
print(7 != 3)  # True

# `<` sprawdza, czy wartość po lewej stronie jest mniejsza od wartości po prawej stronie.
print(2 < 5)  # True

# `<=` sprawdza, czy wartość po lewej stronie jest mniejsza lub równa wartości po prawej stronie.
print(18 <= 18)  # True

# `>` sprawdza, czy wartość po lewej stronie jest większa od wartości po prawej stronie.
print(92 > 75)  # True

# `>=` sprawdza, czy wartość po lewej stronie jest większa lub równa wartości po prawej stronie.
print(18 >= 18)  # True

# `is` sprawdza, czy dwie wartości wskazują ten sam obiekt (albo None). Do porównywania konkretnych wartości używaj `==`, ale do True/False zalecany jest właśnie `is`.
print(None is None)  # True

# `is not` sprawdza, czy dwie wartości wskazują różne obiekty.
print(None is not None)  # False

# ## Operatory logiczne
print("Operatory logiczne")
#
# Operatory logiczne łączą wartości logiczne lub zmieniają ich znaczenie. Ich argumentami są zwykle wartości logiczne albo wyrażenia logiczne, na przykład porównania. Wynikiem jest `True` lub `False`.

# `and` zwraca `True` tylko wtedy, gdy oba argumenty są prawdziwe.
print(True and True)  # True

# `or` zwraca `True`, gdy co najmniej jeden argument jest prawdziwy.
print(False or True)  # True

# `not` neguje wartość logiczną: `not True` to `False`, a `not False` to `True`.
print(not False)  # True

# ## Arytmetyka zmiennoprzecinkowa
print("Arytmetyka zmiennoprzecinkowa")
#
# Liczby zmiennoprzecinkowe (`float`) mogą reprezentować część ułamkową. Operatory arytmetyczne wykonują działania na wartościach liczbowych, a wyniki działań z udziałem `float` są zwykle również typu `float`. Komputery przechowują te liczby z ograniczoną precyzją, dlatego niektóre wyniki dziesiętne są przybliżone.

# `+` dodaje dwie liczby. Jeśli jeden z argumentów jest typu `float`, wynikiem również jest liczba typu `float`.
print(2.5 + 1.2)  # 3.7

# `-` odejmuje prawą liczbę od lewej.
print(5.5 - 2.0)  # 3.5

# `*` mnoży dwie liczby.
print(1.5 * 4.0)  # 6.0

# `/` dzieli lewą liczbę przez prawą i zwraca wynik zmiennoprzecinkowy.
print(7.0 / 2.0)  # 3.5

print(1.0 / 3.0)  # 0.3333333333333333

# `**` podnosi lewą liczbę do potęgi o wykładniku równym prawej liczbie.
print(2.0 ** 3.0)  # 8.0

# Ten operator można także wykorzystać do pierwiastkowania, choć nie jest to zalecane
print(2.0 ** 0.5)  # 1.4142135623730951

# `//` wykonuje dzielenie całkowite: dzieli i zaokrągla wynik w dół do najbliższej liczby całkowitej. (rzadko używane z float)
print(7.5 // 2.0)  # 3.0

# `%` zwraca resztę z dzielenia. (rzadko używane z float)
print(7.5 % 2.0)  # 1.5

# ## Arytmetyka całkowita
print("Arytmetyka całkowita")
#
# Liczby całkowite (`int`) nie mają części ułamkowej. Operatory arytmetyczne mają takie same symbole jak dla liczb zmiennoprzecinkowych, ale dzielenie całkowite `//` zwraca liczbę całkowitą, a `/` nadal zwraca wynik zmiennoprzecinkowy.

# `+` dodaje dwie liczby całkowite.
print(7 + 3)  # 10

# `-` odejmuje jedną liczbę całkowitą od drugiej.
print(7 - 3)  # 4

# `*` mnoży dwie liczby całkowite.
print(7 * 3)  # 21

# `/` dzieli dwie liczby całkowite i zwraca wynik zmiennoprzecinkowy.
print(7 / 2)  # 3.5

# `//` wykonuje dzielenie całkowite, zaokrąglając wynik w dół. Gdy oba argumenty są liczbami całkowitymi, wynikiem jest liczba całkowita.
print(7 // 2)  # 3

# `%` zwraca resztę z dzielenia całkowitego.
print(7 % 2)  # 1

# `**` podnosi liczbę do potęgi o całkowitym wykładniku.
print(2 ** 5)  # 32

# ## Operatory na łańcuchach znaków
print("Operatory na łańcuchach znaków")
#
# Operatory na łańcuchach znaków działają na tekście (`str`). Operator `+` łączy teksty, `*` powtarza tekst, a operatory przynależności sprawdzają, czy dany fragment występuje w innym tekście.

# `+` łączy dwa łańcuchy znaków w jeden.
print("Jan" + " " + "Kowalski")  # Jan Kowalski

# `*` powtarza łańcuch znaków określoną liczbę razy.
print("hej" * 3)  # hejhejhej

# `in` sprawdza, czy jeden łańcuch znaków występuje w innym.
print("przydatne" in "Python ma przydatne operatory")  # True

# `not in` sprawdza, czy jeden łańcuch znaków nie występuje w innym.
print("Java" not in "Python ma przydatne operatory")  # True

# Ostatnie dwa operatory są wykorzystywane także z innymi typami, reprezentującymi sekwencje i zbiory.
print(1 in [1, 2, 3])  # True

# ## Pozostałe operatory
print("Pozostałe operatory")
#
# Operatory bitowe działające na bitach liczb całkowitych.

# `&` porównuje odpowiadające sobie bity i zwraca `1` tylko wtedy, gdy oba bity mają wartość `1`.
print(6 & 3)  # 2

# `|` porównuje odpowiadające sobie bity i zwraca `1`, gdy co najmniej jeden bit ma wartość `1`.
print(6 | 3)  # 7

# `^` porównuje odpowiadające sobie bity i zwraca `1`, gdy bity mają różne wartości.
print(6 ^ 3)  # 5

# `~` odwraca każdy bit liczby całkowitej (w Pythonie `~n` jest równe `-n - 1`).
print(~6)  # -7

# `<<` przesuwa bity liczby całkowitej w lewo, dopisując z prawej strony zera.
print(3 << 2)  # 12

# `>>` przesuwa bity liczby całkowitej w prawo, odrzucając bity przesunięte poza jej koniec.
print(12 >> 2)  # 3

# TODO: Zadanie: dodaj więcej funkcji print, które testują działanie operatorów i zachowanie danych różnych typów, nie opisane w tym pliku.
