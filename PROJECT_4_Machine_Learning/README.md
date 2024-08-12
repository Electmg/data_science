# PROJECT-4. Задача классификации

## Оглавление
* [1. Описание проекта](https://github.com/Electmg/data_science/blob/main/PROJECT_4_Machine_Learning/README.md#Описание-проекта)
* [2. Какой кейс мы решаем](https://github.com/Electmg/data_science/blob/main/PROJECT_4_Machine_Learning/README.md#какой-кейс-мы-решаем)
* [3. Краткая информация о данных](https://github.com/Electmg/data_science/blob/main/PROJECT_4_Machine_Learning/README.md#Краткая-информация-о-данных)
* [4. Этапы работы над проектом](https://github.com/Electmg/data_science/blob/main/PROJECT_4_Machine_Learning/README.md#Этапы-работы-над-проектом)
* [5. Результат](https://github.com/Electmg/data_science/blob/main/PROJECT_4_Machine_Learning/README.md#Результат)
* [6. Выводы](https://github.com/Electmg/data_science/blob/main/PROJECT_4_Machine_Learning/README.md#Выводы)

## 1. Описание проекта
 Банки хранят огромные объёмы информации о своих клиентах. Эти данные можно использовать для того, чтобы оставаться на связи с клиентами и индивидуально ориентировать их на подходящие именно им продукты или банковские предложения.

Обычно с выбранными клиентами связываются напрямую через разные каналы связи: лично (например, при визите в банк), по телефону, по электронной почте, в мессенджерах и так далее. Этот вид маркетинга называется прямым маркетингом. На самом деле, прямой маркетинг используется для взаимодействия с клиентами в большинстве банков и страховых компаний. Но, разумеется, проведение маркетинговых кампаний и взаимодействие с клиентами — это трудозатратно и дорого.
Банкам хотелось бы уметь выбирать среди своих клиентов именно тех, которые с наибольшей вероятностью воспользуются тем или иным предложением, и связываться именно с ними.


:arrow_up:[к оглавлению](https://github.com/Electmg/data_science/blob/main/PROJECT_4_Machine_Learning/README.md#Оглавление)

## 2. Какой кейс мы решаем
Мне предоставили данные о последней маркетинговой кампании, которую проводил банк: задачей было привлечь клиентов для открытия депозита.Необходимо проанализировать эти данные, выявить закономерность и найти решающие факторы, повлиявшие на то, что клиент вложил деньги именно в этот банк. При успешном выполнении задачи, увеличаться доходы банка и понимание целевой аудитории, которую необходимо привлекать путём рекламы и различных предложений.

Бизнес-задача: определить характеристики, по которым можно выявить клиентов, более склонных к открытию депозита в банке, и за счёт этого повысить результативность маркетинговой кампании.

Техническая задача для специалиста в Data Science: построить модель машинного обучения, которая на основе предложенных характеристик клиента будет предсказывать, воспользуется он предложением об открытии депозита или нет.

**Основные цели:**
- Исследовать данные, а не просто вычисляйте метрики и создавайте визуализации.
- Попробовать выявить характерные черты для потенциальных клиентов, чтобы чётко очертить ЦА и увеличить прибыль банка.
- Необходимо проявить фантазию и использовать разные инструменты для повышения качества прогноза.

Проект будет состоять из пяти частей:
1. **Первичная обработка данных**. В рамках этой части предстоит обработать пропуски и выбросы в данных. Это необходимо для дальнейшей работы с ними
2. **Разведывательный анализ данных (EDA)**. Необходимо будет исследовать данные, нащупать первые закономерности и выдвинуть гипотезы.
3. **Отбор и преобразование признаков**. На этом этапе необходимо перекодировать и преобразовать данные таким образом, чтобы их можно было использовать при решении задачи классификации. Если на первом этапе необходимо лишь избавить данные от ненужных артефактов, то на этом шаге необходимо совершить действия, более важные для подготовки данных к задаче классификации, уже понимая их структуру.
4. **Решение задачи классификации: логистическая регрессия и решающие деревья**. На данном этапе необходимо построить прогностическую модель и оценить её качество, а также научиться подбирать оптимальные параметры модели для того, чтобы получить наилучший результат для конкретного алгоритма.
5. **Решение задачи классификации: ансамбли моделей и построение прогноза**. На заключительном этапе необходимо доработать своё предсказание с использованием более сложных алгоритмов и оценить, с помощью какой модели возможно сделать более качественные прогнозы.

**Условия выполнения:**
Каждая из представленных частей проекта будет состоять из блока практических заданий, которые необходимо выполнить в своих Jupyter-ноутбуках, и контрольных вопросов на платформе, отвечая на которые есть возможность проверять верность своего решения.

**Метрика качества**
Для оценки качества модели — точности прогнозов, сделанных моделью, —  будет использоваться метрика (некий числовой показатель), в соответствии с поставленной задачей;

ДЛЯ УСПЕШНОГО ВЫПОЛНЕНИЯ ПРОЕКТА необходимо:
- Скачайть датасет и ноутбук-шаблон. Проверить, что файлы скачались в корректном формате: датасет должен быть в формате CSV, а ноутбук  в формате .IPYNB.
- Внимательно изучить детали задачи и данные. Данные реальные, без предварительной обработки. Уделите особое внимание предобработке данных, учитывайте все нюансы.
- Ответить на все контрольные вопросы. Внимательно читайте вопросы и не забывайте про жёсткие требования к их последовательности: любое нарушение порядка действий может повлечь невозможность получить верные ответы.
- Загрузить ноутбук со своим решением на GitHub, аккуратно его оформив. Несмотря на то, что ваши ответы не будут проверяться ментором, решение реального кейса может стать хорошим вкладом в ваше портфолио.

**Что практикуем**
- Учимся работать с IDE;
- Учимся работать с GitHub;
- Учимся работать с Jupyter Notebook;
- Учимся создавать, преобразовывать и производить отбор новых признаков;
- Учимся делать выводы исходя из полученных данных, построенных графиков;
- Учимся строить прогностические модели(логистическая регрессия и решающие деревья) и оцените их качество; 
- Учимся подбирать оптимальные параметры модели для того, чтобы получить наилучший результат для конкретного алгоритма..

:arrow_up:[к оглавлению](https://github.com/Electmg/data_science/blob/main/PROJECT_4_Machine_Learning/README.md#Оглавление)

## 3. Краткая информация о данных
Код представлен в файле Project_4_ML_Bolotov_MG.ipynb
Код написан на Python версии 3.9.10

:arrow_up:[к оглавлению](https://github.com/Electmg/data_science/blob/main/PROJECT_4_Machine_Learning/README.md#Оглавление)

## 4. Этапы работы над проектом
Работа проведена в 4 этапа:
1) Код написан на Python и с использованием Jupyter Notebook
2) Код выложен на на платформу GitHub
3) Код оформел требуемым образом
4) Выполненны ответы на все поставленные вопросы

:arrow_up:[к оглавлению](https://github.com/Electmg/data_science/blob/main/PROJECT_4_Machine_Learning/README.md#Оглавление)

## 5. Результат

- Выполнены ответы на все контрольные вопросы;
- Загружен ноутбук со своим решением на GitHub, оформив его в соответствии с требованиями;
- Выполнены все необходимые выводы по каждому поставленному вопросу;
- Произведена оценка каждой модели, в соответствии с небходимой для поставленой задачей метрики 
- Результат работы выполнен в формате .ipynb и находится по ссылке (https://github.com/Electmg/data_science/blob/main/PROJECT_4_Machine_Learning/Project_4_ML_Bolotov_MG.ipynb).

:arrow_up:[к оглавлению](https://github.com/Electmg/data_science/blob/main/PROJECT_4_Machine_Learning/README.md#Оглавление)


## 6. Выводы
Все поставленные задачи выполнены!

:arrow_up:[к оглавлению](https://github.com/Electmg/data_science/blob/main/PROJECT_4_Machine_Learning/README.md#Оглавление)