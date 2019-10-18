# test_task
Построить инвертированный индекс по стихотворению "Чепушники" Сергея Михалкова:

На одной лесной опушке
Жили-были круглый год:
Две старушки,
Две кукушки
И глухой безухий кот.
Две старушки вышивали,
Две кукушки куковали,
Кот сибирский, без ушей,
Полевых ловил мышей.

На выходе индекс должен представлять из себя массив вида:
[
  {
    <слово>:
      [
        { <номер_строки>, <номер_позиции> },
 ...
      ]
  },
  ...
]
Как передавать входные данные, не важно.
Вывод либо в консоль, либо в файл.

Бонусом - можно попробовать реализовать поиск слов по построенному индексу.
