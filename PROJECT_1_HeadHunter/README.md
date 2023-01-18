# Анализ резюме из HeadHunter

## Оглавление
* [1. Описание проекта](https://github.com/Electmg/data_science/blob/main/PROJECT_1. Анализ резюме из HeadHunter/README.md#Описание-проекта)
* [2. Какой кейс мы решаем](https://github.com/Electmg/data_science/blob/main/PROJECT_1. Анализ резюме из HeadHunter/README.md#какой-кейс-мы-решаем)
* [3. Краткая информация о данных](https://github.com/Electmg/data_science/blob/main/PROJECT_1. Анализ резюме из HeadHunter/README.md#Краткая-информация-о-данных)
* [4. Этапы работы над проектом](https://github.com/Electmg/data_science/blob/main/PROJECT_1. Анализ резюме из HeadHunter/README.md#Этапы-работы-над-проектом)
* [5. Результат](https://github.com/Electmg/data_science/blob/main/PROJECT_1. Анализ резюме из HeadHunter/README.md#Результат)
* [6. Выводы](https://github.com/Electmg/data_science/blob/main/PROJECT_1. Анализ резюме из HeadHunter/README.md#Выводы)

## 1. Описание проекта
Компания HeadHunter хочет построить модель, которая бы автоматически определяла примерный уровень заработной платы, подходящей пользователю, исходя из информации, которую он указал о себе. Но прежде чем построить модель, данные необходимо преобразовать, исследовать и очистить.

Файлы с исходными данными расположенны по ссылкам: (https://drive.google.com/file/d/1Y50301yHBALfB2s5-8zw95QST0IlKE98/view?sp=share_link)
(https://drive.google.com/file/d/1D2Ut--ydC_q_I0LQl2DwkoAPmRhtLtv_/view?usp=share_link)

:arrow_up:[к оглавлению](https://github.com/Electmg/data_science/blob/main/PROJECT_1. Анализ резюме из HeadHunter/README.md#Оглавление)

## 2. Какой кейс мы решаем
Проект состоит из четырёх частей:
1. базовый анализ структуры данных;
2. преобразование данных;
3. разведывательный анализ;
4. очистка данных.

**Условия выполнения:**
Каждая часть будет состоит из блока практических заданий, которые необходимо выполнить в jupyter-ноутбук, и контрольных вопросов на платформе, отвечая на которые есть возможность проверить верность своего решения. Задания выполняются последовательно.
Помимо проверки заданий на платформе, необходимо отправить свой код ментору для code-ревью. Дополнительно предоставлен ноутбук-шаблон и требования, согласно которым необходимо оформить своё решение.

**Метрика качества**
ДЛЯ УСПЕШНОГО ВЫПОЛНЕНИЯ ПРОЕКТА необходимо:
- Внимательно изучить детали задачи;
- Скачать уже знакомый датасет и ноутбук-шаблон;
- Обязательно ознакомиться с дополнительным теоретическим материалом, который даётся перед заданием;
- Воспользоваться нашими советами и подсказками при выполнении проекта;
- Ответить на все контрольные вопросы: за них вы можете максимально набрать 30 баллов на платформе;
- Загрузить ноутбук со своим решением на GitHub, оформив его в соответствии с требованиями;
- Сдать проект на проверку и получить 10 баллов (из них 8 баллов — за основное задание и 2 балла — за дополнительное) за выводы по разведывательному анализу;
- Получить обратную связь от команды курса.

Требования к оформлению ноутбука-решения:
- Решение оформляется только в Jupyter Notebook;
- Решение оформляется в соответствии с ноутбуком-шаблоном;
- Каждое задание выполняется в отдельной ячейке, выделенной под задание (в шаблоне они помечены как ваш код здесь). Не следует создавать множество ячеек для решения задачи — это создаёт неудобства при проверке;
- Код для каждого задания оформляется в одной-двух jupyter-ячейках (не стоит создавать множество ячеек для решения задачи, это усложняет проверку);
- Решение должно использовать только пройденный материал: переменные, основные структуры данных (списки, словари, множества), циклы, функции, библиотеки numpy, pandas, matplotlib, seaborn, plotly. Если вы думаете, что для решения необходимо воспользоваться сторонними библиотеками или инструментами (например Excel), другими языками программирования или неизученными конструкциями, вы ошибаетесь :) Все задания решаются с помощью уже знакомых методов;
- Код должен быть читаемым и понятным: имена переменных и функций отражают их сущность, важно избегать многострочных конструкций и условий;
- Пользуйтесь руководством PEP 8;
- Графики оформляются в соответствии с теми правилами, которые мы приводили в модуле по визуализации данных;
- Обязательное требование: графики должны содержать название, отражающее их суть, и подписи осей;
- Выводы к графикам оформляются в формате Markdown под самим графиком в отдельной ячейке (в шаблоне они помечены как ваши выводы здесь).
Выводы должны быть представлены в виде небольших связанных предложений на русском языке.

**Что практикуем**
- Учимся писать хороший код на Python;
- Учимся работать с IDE;
- Учимся работать с GitHub;
- Учимся работать с Jupyter Notebook;
- Учимся работать с библиотеками numpy, pandas;
- Учимся строить графики с использованием библиотек matplotlib, seaborn, plotly;
- Учимся делать выводы исходя из построенных графиков.

:arrow_up:[к оглавлению](https://github.com/Electmg/data_science/blob/main/Project_1/README.md#Оглавление)

## 3. Краткая информация о данных
Код представлен в файле Project-1. Ноутбук-шаблон Болотов М.Г.ipynb
Код написан на Python версии 3.9.10

:arrow_up:[к оглавлению](https://github.com/Electmg/data_science/blob/main/PROJECT_1. Анализ резюме из HeadHunter/README.md#Оглавление)

## 4. Этапы работы над проектом
Работа проведена в 4 этапа:
1) Код написан на Python в соответствии со стандартами PEP8 и с использованием Jupyter Notebook
2) Код выложен на на платформу GitHub
3) Код оформел требуемым образом
4) Код отправлен ментору для проверки

:arrow_up:[к оглавлению](https://github.com/Electmg/data_science/blob/main/PROJECT_1. Анализ резюме из HeadHunter/README.md#Оглавление)

## 5. Результат

- Изучен дополнительный теоретический материал, который был дан перед заданием;
- Выполнены ответы на все контрольные вопросы;
- Загружен ноутбук со своим решением на GitHub, оформив его в соответствии с требованиями;
- Выполнены выводы по разведывательному анализу;
- Результат работы выполнен в формате .ipynb и находится по ссылке (https://github.com/Electmg/data_science/blob/main/PROJECT_1. Анализ резюме из HeadHunter/Project-1. Ноутбук-шаблон Болотов М.Г.ipynb)
- Результат работы в формате HTML можно скачать по ссылке: (https://github.com/Electmg/data_science/blob/main/PROJECT_1. Анализ резюме из HeadHunter/HTML/Project-1. Ноутбук-шаблон Болотов М.Г.html)
- Графики выполненные с использованием библиотеки plotly находятся в папке HTML по ссылке: (https://github.com/Electmg/data_science/blob/main/PROJECT_1. Анализ резюме из HeadHunter/HTML)
- Проект сдан на проверку для получения обратной связи от команды курса.

:arrow_up:[к оглавлению](https://github.com/Electmg/data_science/blob/main/PROJECT_1. Анализ резюме из HeadHunter/README.md#Оглавление)


## 6. Выводы
Выводы будут сделаны после проверки ментором!

:arrow_up:[к оглавлению](https://github.com/Electmg/data_science/blob/main/PROJECT_1. Анализ резюме из HeadHunter/README.md#Оглавление)