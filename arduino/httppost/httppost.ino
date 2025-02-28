#include <WiFi.h>
#include <HTTPClient.h>


const char* ssid = "ardilluda";
const char* password = "01971101";

const char* serverUrl = "http://192.168.0.6:8000/api/sensor/";




float temperatura = 0;
float humedad = 0;

void setup() {
    Serial.begin(115200);

    // Conexión a WiFi
    Serial.print("Conectando a WiFi...");
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
    Serial.println("\nConectado a WiFi");
}

void loop() {


    
    if (WiFi.status() == WL_CONNECTED) {
        HTTPClient http;
        http.begin(serverUrl);
        http.addHeader("Content-Type", "application/json");
        
        temperatura = 0;
        humedad = 0;

        // Crear el JSON
        String jsonString = "{";
        jsonString += "\"temperatura\":" + String(temperatura, 2) + ",";
        jsonString += "\"humedad\":" + String(humedad);
        jsonString += "}";

        // Enviar datos
        int httpResponseCode = http.POST(jsonString);
        if (httpResponseCode > 0) {
            Serial.print("Respuesta del servidor: ");
            Serial.println(http.getString());
        } else {
            Serial.print("Error en la solicitud: ");
            Serial.println(httpResponseCode);
        }

        http.end();
    } else {
        Serial.println("No conectado a WiFi");
    }

    delay(5000);  // Esperar 5 segundos antes del próximo envío
}
