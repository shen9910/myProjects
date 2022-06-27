In this repo, I present mini-project I completed during my application to Kaspi Lab.
The csv data is available from https://www.kaggle.com/mattiuzc/stock-exchange-data

First, I created a database and tables: data, info and processed.
Then, I wrote a function in python that inserts data from csv files to the database

And finally I wrote some queries, created SQL Views, and completed interactive visualization
according to the tasks given:

3.1) Разработать представление (вью) V_NOTPROCESSED, отображающее записи из data, которые не были обработаны (данные в processed) в разрезе по регионам (info). Важно: Исключить записи, содержащие одинаковые значения ключей (поле key)
3.2) Разработать вью V_PROCESSED, отображающее все записи из processed в разрезе по регионам, году и месяцу. Также вью должна отображать информацию:
3.2.1) самую максимальную цену в момент даты открытия и самую минимальную цены во время для торговли. При выводе значения также вывести название валюты
3.2.2) полное наименование биржи


Отобразить данные из V_PROCESSED в отчетах:
4.1) для любого региона (на ваш выбор) показать в виде 2 графиков:
  максимальную цену в момент даты открытия в месячном разрезе
  минимальную цену во время для торговли в месячном разрезе. Имя региона читается из кода при формировании отчета (hardcoded)
4.2*) опционально, но дает дополнительные баллы:
Задача 4.1, но реализовать выбор региона на отчете через графические элементы “список”, “выпадающее меню” или радиокнопки (если число регионов меньше 10). 
