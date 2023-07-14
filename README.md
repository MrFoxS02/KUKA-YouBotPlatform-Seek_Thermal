# KUKA-YouBotPlatform-Seek_Thermal

## Описание

KUKA-YouBotPlatform-Seek_Thermal — это драйвер пользовательского пространства для тепловизора SEEK THERMAL COMPACT, построенный на libusb и libopencv.

Поддерживаемые камеры:
* [Seek Thermal Compact](http://www.thermal.com/products/compact)


**ПРИМЕЧАНИЕ. Библиотека не поддерживает вывод абсолютного показания температуры и ограничивается выводом термограммы**


## Заимствования

Код основан на идее из следующего репозитория:
* https://github.com/coaco-robot/libseek-thermal

## Сборка

Зависимости:
* cmake
* libopencv-dev (>= 2.4)
* libusb-1.0-0-dev

ПРИМЕЧАНИЕ: вы можете просто «apt-get install» все вышеперечисленные библиотеки

```
cd libseek-thermal
mkdir build
cd build
cmake ..
make
```

Установите разделяемую библиотеку, заголовки и двоичные файлы:

```
sudo make install
sudo ldconfig 
```

## Запуск примеров

```
./examples/seek_viewer     # Получение поточного изображения с камеры
./examples/seek_snapshot   # Получение единичного изображения с камеры
```

### seek_viewer
seek_viewer — это программное решение для постоянного сохранения термограммы в процессе работы. Программа поддерживает поворот изображения, масштабирование и сопоставление цветов с использованием любой из цветовых карт OpenCV.

```
seek_viewer --camtype=seekpro --colormap=11 --rotate=0                          # view color mapped thermal video
```

### seek_snapshot
seek_snapshot делает единичное изображения. Это полезно для интеграции в сценарии оболочки. Программа поддерживает вращение и сопоставление цветов так же, как seek_viewer.

## Python_Seek_Thermal

Python_Seek_Thermal - это программное решение которое позволяет получить изображение с тепловизора установленного на роботе KUKA YouBot Platform при помощи стека (time, cv2, paramico)
ПРИМЕЧАНИЕ: в представленном решении изображение постоянно сохраняется на роботе т.к. linux server не позволяет отображать медиафайлы. Ввиду этого при помощи библиотеки paramico при помощи ssh происходит постоянный забор файла с робота на ПК пользователя.
