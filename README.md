# News API Mini Project

This is a repository of a News API for a mini project created by Dennis Filemon




# Documentation

This API can be tested on Heroku with the following URL:

```sh
https://testing-api-course.herokuapp.com/
```



### Geting all the news

Here is the URL of the API to get all the news saved in the database :

```sh
https://testing-api-course.herokuapp.com/items (GET Method)
```

Here is the example of the result :

```sh
[
    {
        "content": "Suara.com – Redmi 8A masuk ke pasar Indonesia sebagai penutup ponsel lansiran Xiaomi pada tahun 2019 lalu. Dilihat dari banderolnya yang hanya Rp 1,4 juta, ponsel ini jelas menyasar segmen low-end.\r\nMeski bermain di kelas bawah, ada beberapa fitur menarik yan… [+5346 chars]",
        "category": "technology",
        "title": "Tak Cuma Murah, Kaya Fungsi Dukung Pekerjaan - Celebes Top News",
        "country": "id",
        "id": 1
    },
    {
        "content": "TRIBUNNEWS.COM – Berikut daftar harga HP Samsung Februari 2020, ada Galaxy A, Galaxy S, Galaxy Note, Galaxy M, dan Galaxy Fold.\r\nUntuk Galaxy A51 yang belum lama dirilis ini dijual Rp 4,3 juta.\r\nSedangkan Galaxy S10 yang memiliki sistem operasi Android 9.0 di… [+539 chars]",
        "category": "technology",
        "title": "Daftar Harga Terbaru HP Samsung Februari 2020: Galaxy A51 Rp 4,3 Juta hingga Galaxy S10 Rp 12,9 Juta - Tribunnews",
        "country": "id",
        "id": 2
    },
    {
        "content": "NEW DELHI - MediaTek meluncurkan SoC game andalannya, Helio G90, pada pertengahan 2019. Chipset ini mendukung keberhasilan Redmi Note 8 Pro di pasar. Nah sekarang, MediaTek memiliki solusi yang bahkan lebih terjangkau untuk para gamer, namanya Helio G80. Kema… [+1294 chars]",
        "category": "technology",
        "title": "MediaTek Rilis Chipset Kelas Menengah Khusus untuk Game Helio... - SINDOnews.com",
        "country": "id",
        "id": 3
    },
    {
        "content": "SEOUL - Samsung bakal menggelar acara besarnya hanya dalam waktu satu pekan ke depan. Bocoran terkait handphone flagship-nya, Galaxy S20 Series, terus mengalir deras.Kali ini kebocoran baru menumpahkan lebih banyak rincian pada sisi kemampuan kamera. Sebab ke… [+1150 chars]",
        "category": "technology",
        "title": "Semua Kamera Samsung Galaxy S20 Dukung Pemotretan Simultan - SINDOnews.com",
        "country": "id",
        "id": 4
    },
    {
        "content": "Jakarta - WhatsApp Beta Dark Mode menjadi salah satu fitur yang bikin warga dunia penasaran. Dikutip dari situs wabetainfo, aplikasi milik facebook ini memang sempat menjanjikan dark mode.\r\nJanji tersebut akhirnya dipenuhi, meski tidak untuk aplikasi WhatsApp… [+1636 chars]",
        "category": "technology",
        "title": "WhatsApp Beta Dark Mode, Begini Cara Mengaktifkannya - detikInet",
        "country": "id",
        "id": 5
    }
]
```



### Registering an account

Here is the URL of the API to register an account (username and password data required) :

```sh
https://testing-api-course.herokuapp.com/register (POST Method)
```

Here is the example of the result :

```sh
{
    "message": "User created successfully."
}
```



### Login with a registered account

Here is the URL of the API to login with a registered account (username and password data required) :

```sh
https://testing-api-course.herokuapp.com/auth (POST Method)
```

Here is the example of the result :

```sh
{
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1ODA3NTM5NzIsImlhdCI6MTU4MDc1MzY3MiwibmJmIjoxNTgwNzUzNjcyLCJpZGVudGl0eSI6MX0.gCnpS9fCxu8jNa7jefE02lRHbRvfVufjdH5zGWKOIuQ"
}
```



### Getting specific news

Here is the URL of the API to get a certain news saved in the database (Login + category and country data required) :

```sh
https://testing-api-course.herokuapp.com/item/<category_name>?country=<country_code> (GET Method)
```

Here is the example of the result :

```sh
[
    {
        "content": "Jakarta, CNBC Indonesia - Bursa Amerika Serikat (AS) dibuka menguat pada perdagangan Senin (03/02/2020), dipimpin saham Nike yang melonjak 3,3% setelah direkomendasikan beli oleh JP Morgan dan UBS karena harganya terlalu murah akibat krisis Wuhan.\r\nIndeks Dow… [+2561 chars]",
        "category": "business",
        "title": "Investor Buru Saham-Saham Murah, Wall Street Dibuka Melonjak - CNBC Indonesia",
        "country": "id",
        "id": 5
    },
    {
        "content": "Jakarta, CNN Indonesia -- Badan Pemeriksa Keuangan (BPK) menyatakan telah menemukan indikasi kecurangan atau fraud di tubuh Asabri. Indikasi tersebut disimpulkan dari hasil audit sementara yang mereka lakukan terhadap Asabri.Tak hanya di tubuh Asabri, indikas… [+1613 chars]",
        "category": "business",
        "title": "BPK Temukan Indikasi Kecurangan di Tubuh Asabri dan Jiwasraya - CNN Indonesia",
        "country": "id",
        "id": 6
    }
]
```



### Saving news to the database

Here is the URL of the API to save a certain news to the database (Login + category and country data required) :

```sh
https://testing-api-course.herokuapp.com/item/<category_name>?country=<country_code> (POST Method)
```

Here is the example of the result :

```sh
{
    "message": "Item saved.",
    "data": {
        "id": 1,
        "title": "AirAsia CEO Fernandes and chairman step aside as Airbus bribery allegations probed - CNA",
        "category": "business",
        "country": "sg",
        "content": "KUALA LUMPUR: AirAsia Group CEO Tony Fernandes and Chairman Kamarudin Meranun will step aside for at least two months while the airline and authorities investigate allegations Airbus paid a bribe of US$50 million to win plane orders from the company.\r\nA commi… [+3072 chars]"
    }
}
```



### Deleting news to the database

Here is the URL of the API to Delete a certain news from the database (Login + news id required) :

```sh
https://testing-api-course.herokuapp.com/item/<news_id> (DELETE Method)
```

Here is the example of the result :

```sh
{
    "message": "Item deleted.",
    "data": {
        "id": 9,
        "title": "Bankrupt Forever 21 in deal to sell for $110.6m - The Straits Times",
        "category": "business",
        "country": "sg",
        "content": "NEW YORK (BLOOMBERG) - A group that includes two of Forever 21's biggest landlords has offered to buy the bankrupt retailer for US$81 million (S$110.6 million), a fraction of what the international fashion pioneer was once worth.\r\nThe consortium of Simon Prop… [+1717 chars]"
    }
}
```
