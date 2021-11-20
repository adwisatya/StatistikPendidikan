# Statistik Pendidikan - Scrapper Data http://statistik.data.kemdikbud.go.id
Library ini digunakan untuk memudahkan developer atau user dalam mengakses data dari statistik.data.kemdikbud.go.id dalam bentuk json sehingga lebih mudah diolah

## Penggunaan

### Instalasi
Untuk mendownload dan menginstall library ini, gunakan perintah
```sh
pip install StatistikPendidikan
```

### Pemanggilan
Pemanggilan fungsi bisa dilakukan dengan import sederhana terhadap function yang tersedia
```Python
from StatistikPendidikan.processor import getGambaranUmumSekolah
```
Function getGambaranUmumSekolah memerlukan dua parameter yakni: tingkat pendidikan (sd,smp,sma, dan smk) dan tahun ajaran (2017,2018,2019,2020,dst)


License
----

MIT License
