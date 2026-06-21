# 🌱 Smart Garden Monitoring System

## Overview

Smart Garden Monitoring System is an IoT-based project that uses an ESP32 microcontroller and Django web application to monitor environmental conditions in a garden and automate irrigation.

The system collects data from multiple sensors, including soil moisture, temperature, humidity, and light intensity. The collected data is sent to a Django backend through REST APIs, stored in a database, and displayed on a web dashboard.

When the soil moisture level drops below a predefined threshold, the system can automatically activate a water pump to irrigate the plants.

---

## Features

* Real-time soil moisture monitoring
* Temperature and humidity monitoring using DHT11
* Light intensity monitoring using LDR
* Automatic irrigation control
* Water pump management through relay module
* Django REST API integration
* Interactive web dashboard
* Historical sensor data storage
* Device status monitoring

---

## Hardware Components

* ESP32 Development Board
* Soil Moisture Sensor
* DHT11 Temperature & Humidity Sensor
* LDR Sensor
* 16x2 LCD with I2C
* Relay Module
* Water Pump
* Red LED
* Green LED
* Buzzer
* NPN Transistor
* Flyback Diode
* Breadboard and Jumper Wires

---

## Software Stack

### Backend

* Python
* Django
* Django REST Framework

### Database

* SQLite (Development)
* PostgreSQL (Production)

### IoT Device

* ESP32
* MicroPython

### Frontend

* HTML
* Bootstrap 5
* JavaScript
* Chart.js

---

## API Endpoints

### Sensor Data

```http
GET /api/sensors/
POST /api/sensors/
```

### Pump Status

```http
GET /api/pump/
POST /api/pump/
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/smart-garden.git
cd smart-garden
```

### Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Start Server

```bash
python manage.py runserver
```

---

## Future Improvements

* Mobile application
* MQTT integration
* Real-time notifications
* Weather forecast integration
* AI-based irrigation recommendations
* Multi-garden support

---

## Author

Developed by  Ahmed Badri.

______________________________________________

# 🌱 Nidaamka Kormeerka Beerta Casriga ah (Smart Garden Monitoring System)

## Hordhac

Smart Garden Monitoring System waa mashruuc IoT ah oo isku daraya ESP32 iyo Django si loo kormeero xaaladda beerta loona maareeyo waraabinta si otomaatig ah.

Nidaamku wuxuu ururiyaa xogta:

* Qoyaanka ciidda
* Heerkulka
* Qoyaanka hawada
* Iftiinka

Xogtan waxaa loo diraa Django REST API, waxaana lagu kaydiyaa database si loogu soo bandhigo dashboard web ah.

Marka qoyaanka ciiddu hoos uga dhaco heerka la dejiyay, nidaamku wuxuu si toos ah u shidi karaa bamka biyaha si uu u waraabiyo dhirta.

---

## Astaamaha Mashruuca

* Kormeerka qoyaanka ciidda
* Kormeerka heerkulka iyo qoyaanka hawada
* Kormeerka iftiinka
* Waraabin otomaatig ah
* Maareynta bamka biyaha
* REST API ku dhisan Django
* Dashboard web ah
* Kaydinta xogta sensors-ka
* Kormeerka xaaladda qalabka

---

## Qalabka La Isticmaalay

* ESP32 Development Board
* Soil Moisture Sensor
* DHT11 Sensor
* LDR Sensor
* LCD 16x2 I2C
* Relay Module
* Water Pump
* Red LED
* Green LED
* Buzzer
* Breadboard
* Jumper Wires

---

## Teknoolojiyada La Adeegsaday

### Backend

* Python
* Django
* Django REST Framework

### Database

* SQLite
* PostgreSQL

### IoT

* ESP32
* MicroPython

### Frontend

* HTML
* Bootstrap
* JavaScript
* Chart.js

---

## API-yada

### Sensor Data

```http
GET /api/sensors/
POST /api/sensors/
```

### Pump Control

```http
GET /api/pump/
POST /api/pump/
```

---

## Sida Loo Rakibo

### Soo dejiso Repository-ga

```bash
git clone https://github.com/yourusername/smart-garden.git
cd smart-garden
```

### Samee Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Ku rakib Dependencies

```bash
pip install -r requirements.txt
```

### Samee Migration

```bash
python manage.py makemigrations
python manage.py migrate
```

### Shid Server-ka

```bash
python manage.py runserver
```

---

## Horumarin Mustaqbalka

* Mobile App
* MQTT Integration
* Notifications
* Weather API Integration
* AI-based Irrigation
* Maareynta beero badan

---

## Qoraa

Waxaa sameeyay ahmed badri.


