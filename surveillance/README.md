# Serverraumueberwachung

## Getting Started

- Install the requirements
  - fastapi
  - uvicorn
  - gpiozero
  - adafruit-circuitpython-dht
- Start the Application (Dev): `python -m uvicorn main:app --reload`
- open the [Dashboard](https://buntelrus.github.io/Serverraumueberwachung/settings) and configure your fastapi connection

## Helpful resources

- [GPIO-Pin-Doc](https://pinout.xyz/)

## Vererbung

The following diagram shows, how the programm processes the data to feed our dashboard.
```mermaid
classDiagram
    Subject <|-- ApiSubject
    ApiSubject <|-- Device
    Device <|-- MotionSensor
    Device <|-- TemperatureSensor
    Device <|-- LED
    Device <|-- PersonCounter
    note for ApiSubject "collects all events for REST api\nbroadcasts all events over websocket"
    note for Device "assigns id to each device\ncollects all devices for REST api"
    class Subject {
        +subscribe(Subscription)
        +unsubscribe(Subscription)
        +notify()
    }
    class ApiSubject {
        +event_list$
        -websocket_manager: WebsocketManager
        +ApiSubject(WebsocketManager)
        +notify()
    }
    class Device {
        +device_list$
        +id: int
        +pin: int
        +Device(int)
        +notify()
    }
    class MotionSensor {
    }
    class TemperatureSensor {
    }
    class LED{
        +on()
        +off()
    }
    class PersonCounter{
        -motion_sensor1: MotionSensor
        -motion_sensor2: MotionSensor
    }
```

