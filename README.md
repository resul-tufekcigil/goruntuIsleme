# Görüntü İşleme Ödevi
## _Resul Tüfekçigil 2016010205017 (%30 1.Öğretim)_

Ödev sırasında kullanılan kütüphaneler:
- cv2 (openCv)
- sys
- getopt
- matplotlib
- numpy

## Kullanım
Kullanım Bilgisi getirmek için:
```sh
goruntuIsleme.py -h
```
Resimi uygulamaya tanımlamak için -i komutu ile dosya yolunu vermeniz gerekmektedir
```sh
goruntuIsleme.py -i <image path>
```
Görüntü işleme yapmak için -o ile seçenek vermeniz gerekmektedir
- gama
- logaritmik
- negatif
- metin
- bit_slicing
- kenar
- addNoise
```sh
goruntuIsleme.py -i <image path> -o gama
goruntuIsleme.py -i <image path> -o logaritmik
goruntuIsleme.py -i <image path> -o negatif
goruntuIsleme.py -i <image path> -o metin
goruntuIsleme.py -i <image path> -o bit_slicing
goruntuIsleme.py -i <image path> -o kenar
goruntuIsleme.py -i <image path> -o addNoise
```
## Spider IDE ile çalıştırmak için 
Spider IDE içerisinde bulunan terminal içerisinde args değişkeni verebilmektesiniz.Bunun için aşağıdaki args kısmını özelleştiriniz.
```sh
runfile('<*.py yolu>',args='args', wdir='*.py konumu')
```
IDE içerisindeki consol üzerinde runfile fonksiyonu kullanarak '*.py' dosyasını çalıştırabilirsiniz.
