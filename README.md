# Ignacio Antías | Software Developer & Cybersecurity Researcher
**Engineering Student @ Universidad de Los Lagos**

Focus on **Ad-Tech Integrity**, **Automation**, and **Cybersecurity**. Dedicated to developing robust solutions that protect digital assets and optimize marketing infrastructure.

### Core Competencies:
* **Programming:** Python (Advanced), C, Java.
* **Cybersecurity:** Anomaly detection, secure API integration, and data integrity.
* **Automation:** Telegram Bot API, automated reporting systems, and real-time monitoring[cite: 1].
* **Tools:** OpenCV, Git, JSON/CSV Database Management[cite: 1].

### Ign Tech Solutions - Ongoing Projects:
* **Ad-Account Integrity Monitor:** Developing automated scripts to audit Meta Ads infrastructure and detect unauthorized access.
* **Biometric Access Systems:** Facial recognition implementation for secure attendance and user validation[cite: 1].
* **Notification Engines:** Real-time alert systems for budget monitoring and technical anomaly detection[cite: 1].

---
**Location:** Osorno, Chile[cite: 1].  
**Email:** iantiasb@gmail.com[cite: 1].

´´´mermaid
graph TD
    A[Inicio: Monitorización Programada] --> B{Solicitud API Meta Ads}
    B -->|Uso de Access Token seguro| C[Extracción de Métricas de Gasto y Acceso]
    
    C --> D{Motor de Detección de Anomalías}
    
    D -->|Gasto > Umbral Definido| E[ALERTA: Budget Leakage]
    D -->|Acceso No Autorizado| F[ALERTA: Security Breach]
    D -->|Cambio de Configuración| G[ALERTA: Config Anomaly]
    
    E & F & G --> H[Encriptación de Mensaje de Alerta]
    H --> I[Integración API Telegram]
    I --> J[Envío de Notificación en Tiempo Real]
    
    D -->|Sin Anomalías| K[Log de Integridad del Sistema]
    J --> K
    K --> L[Fin: Estado de Standby]
´´´
