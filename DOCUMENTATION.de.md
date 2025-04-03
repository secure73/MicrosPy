# Micro Python Framework Dokumentation

## Übersicht
Dies ist ein Mikro-Framework, das **ausschließlich für Bildungszwecke** entwickelt wurde, um Anfängern das Verständnis der Grundlagen von Python und der RESTful-API-Entwicklung zu erleichtern. Es implementiert eine einfache MVC-Architektur (Model-View-Controller) und bietet grundlegende RESTful-API-Funktionalitäten.

> ⚠️ **Wichtiger Hinweis**: Dieses Framework ist **nicht für den Produktionseinsatz geeignet**. Es wurde ausschließlich als Lernwerkzeug entwickelt, um zu verstehen:
> - Wie Frameworks wie Django und FastAPI funktionieren
> - Python OOP-Prinzipien und Entwurfsmuster
> - Schichtenarchitektur und Trennung von Belangen
> - Grundlegende REST-API-Prinzipien und HTTP-Anfrageverarbeitung
> - Datenbankoperationen und ORM-Konzepte
> - Grundlegende MVC-Architekturimplementierung

> ⚠️ **Sicherheitswarnung**: Dieses Framework hat **begrenzte Sicherheitsimplementierungen** und sollte niemals in Produktionsumgebungen verwendet werden. Es fehlen:
> - Angemessene Authentifizierung und Autorisierung
> - Eingabesanierung
> - CSRF-Schutz
> - Ratenbegrenzung
> - Produktionsgerechte Fehlerbehandlung
> - Sicherheitsheader
> - Und viele andere grundlegende Sicherheitsfunktionen

Dieses Framework dient als ausgezeichneter erster Schritt zum Erlernen von REST-API-Prinzipien und zum Verständnis der Organisation von Web-Frameworks, sollte aber als Lernwerkzeug und nicht als produktionsreife Lösung behandelt werden.

## Voraussetzungen
- Python 3.13.2 oder höher
- Virtuelle Umgebung (empfohlen)

## Installation

1. Repository klonen:
```bash
git clone https://github.com/secure73/micro_py_framework.git
cd micro_py_framework
```

2. Virtuelle Umgebung erstellen und aktivieren:
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

3. Abhängigkeiten installieren:
```bash
pip install -r requirements.txt
```

## Projektstruktur
```
micro_py_framework/
├── app.py                 # Hauptanwendungseinstiegspunkt
├── controller/            # Controller-Verzeichnis
│   └── UserController.py  # Benutzerbezogene Operationen
├── model/                # Modelle-Verzeichnis
│   └── UserModel.py      # Benutzerdaten-Operationen
├── table/                # Datenbank-Tabellen
│   ├── DBConnection.py   # Datenbankverbindungsverwaltung
│   ├── DBMigrate.py      # Datenbankmigration und Schema
│   └── UserTable.py      # Benutzer-Tabellenschema
├── interface/            # Schnittstellen-Verzeichnis
│   └── IController.py    # Controller-Schnittstelle
└── helper/              # Hilfsprogramme
    ├── HttpHandler.py    # HTTP-Anfragenhandler
    ├── Response.py       # Antwortformatierung
    ├── JWTManager.py     # JWT-Authentifizierung
    └── FormatCheck.py    # Eingabevalidierung
```

## Anwendung starten
```bash
python app.py
```
Der Server startet standardmäßig auf Port 8001.

## API-Endpunkte

### User Controller Endpunkte

1. **Benutzer erstellen**
   - Methode: POST
   - URL: `/user`
   - Anfrage-Body:
     ```json
     {
         "email": "user@example.com",
         "password": "password123",
         "name": "John Doe"
     }
     ```
   - Antwort: Erfolgsmeldung oder Fehlerdetails

2. **Benutzer abrufen**
   - Methode: GET
   - URL: `/user` (alle Benutzer auflisten)
   - URL: `/user/{id}` (spezifischen Benutzer abrufen)
   - Antwort: Benutzerdaten oder Fehlermeldung

3. **Benutzer aktualisieren**
   - Methode: PUT
   - URL: `/user`
   - Anfrage-Body:
     ```json
     {
         "id": 1,
         "name": "Aktualisierter Name",
         "password": "neuespasswort"  // optional
     }
     ```
   - Antwort: Aktualisierte Benutzerdaten oder Fehlermeldung

4. **Benutzer löschen**
   - Methode: DELETE
   - URL: `/user`
   - Anfrage-Body:
     ```json
     {
         "id": 1
     }
     ```
   - Antwort: Erfolgsmeldung oder Fehlerdetails

## Datenvalidierung

### Benutzerdaten-Validierungsregeln
- E-Mail: Muss dem Standard-E-Mail-Format entsprechen
- Passwort: Mindestens 6 Zeichen
- Name: Mindestens 2 Zeichen

## Datenbank

### SQLite Datenbank
- Die Anwendung verwendet standardmäßig SQLite als Datenbank
- Datenbankdatei: `db.db`
- Tabellen werden beim ersten Start automatisch erstellt

### Datenbankmigration (DBMigrate.py)
Die Datei `DBMigrate.py` ist für die Datenbankinitialisierung und Tabellenerstellung zuständig. Sie behandelt:

1. **Datenbankverbindung**
   - Erstellt eine Verbindung zur SQLite-Datenbank (`db.db`)
   - Verwaltet Datenbank-Cursor für SQL-Befehle

2. **Tabellenerstellung**
   - Erstellt automatisch erforderliche Tabellen, falls sie nicht existieren
   - Verwaltet derzeit zwei Tabellen:
     - `users` Tabelle:
       ```sql
       CREATE TABLE users(
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           email TEXT NOT NULL UNIQUE,
           password TEXT NOT NULL,
           name TEXT NOT NULL
       )
       ```
     - `products` Tabelle:
       ```sql
       CREATE TABLE products(
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           name TEXT NOT NULL UNIQUE,
           category TEXT NOT NULL,
           price FLOAT NOT NULL
       )
       ```

3. **Verwendung**
   - Die Migration läuft automatisch beim Anwendungsstart
   - Stellt sicher, dass das Datenbankschema aktuell ist
   - Verhindert Fehler durch fehlende Tabellen

4. **Funktionen**
   - Verwendet `CREATE TABLE IF NOT EXISTS` zur Vermeidung doppelter Tabellenerstellung
   - Verwaltet Primärschlüssel mit Auto-Increment
   - Erzwingt eindeutige Einschränkungen für E-Mail und Produktnamen
   - Verwaltet erforderliche Felder mit NOT NULL Einschränkungen

### Datenbankverbindungsverwaltung (DBConnection.py)
Die Datei `DBConnection.py` verwaltet Datenbankverbindungen mit SQLAlchemy ORM. Sie bietet:

1. **SQLAlchemy-Integration**
   - Verwendet SQLAlchemy für Object-Relational Mapping (ORM)
   - Bietet eine deklarative Basis für Modelldefinitionen
   - Verwaltet Datenbanksitzungen effizient

2. **Verbindungskonfiguration**
   ```python
   engine = create_engine("sqlite:///db.db", echo=False)
   ```
   - Standardkonfiguration verwendet SQLite-Datenbank
   - Unterstützt MySQL/MariaDB durch Verbindungsstring-Modifikation
   - `echo=False` deaktiviert SQL-Abfragenprotokollierung für bessere Leistung

3. **Sitzungsverwaltung**
   ```python
   Session = sessionmaker(bind=engine)
   ```
   - Erstellt eine Sitzungsfabrik für Datenbankoperationen
   - Verwaltet Datenbankverbindungen und Transaktionen
   - Bietet threadsicheren Datenbankzugriff

4. **Hilfsmethoden**
   - `create_all()`: Erstellt alle in Modellen definierten Datenbanktabellen
   - `get_session()`: Gibt eine neue Datenbanksitzung für Operationen zurück

5. **Datenbankunterstützung**
   - **SQLite** (Standard):
     ```python
     engine = create_engine("sqlite:///db.db")
     ```
   - **MySQL/MariaDB**:
     ```python
     engine = create_engine("mysql+pymysql://username:password@localhost:3306/database_name")
     ```

6. **Fehlerbehandlung**
   - Fängt Datenbankverbindungsfehler ab und meldet sie
   - Bietet klare Fehlermeldungen für die Fehlersuche

7. **Verwendung in Modellen**
   ```python
   from table.DBConnection import DBConnection
   
   class YourModel:
       def __init__(self):
           self.Session = DBConnection.Session
   ```

8. **Best Practices**
   - Verwendet Verbindungspooling für bessere Leistung
   - Implementiert ordnungsgemäße Sitzungsverwaltung
   - Unterstützt mehrere Datenbank-Backends
   - Folgt SQLAlchemy Best Practices

### MySQL-Unterstützung
- Das Framework unterstützt auch MySQL-Datenbanken
- Um MySQL zu verwenden, ändern Sie den Verbindungsstring in `table/DBConnection.py`:
  ```python
  engine = create_engine("mysql+pymysql://username:password@localhost:3306/database_name")
  ```

## Fehlerbehandlung
Das Framework enthält grundlegende Fehlerbehandlung für:
- Ungültige Eingabedaten
- Datenbankoperationen
- HTTP-Anfragenvalidierung
- Nicht gefundene Ressourcen

## Sicherheitshinweise
1. Dies ist ein Lehr-Framework und nicht für Produktionsumgebungen empfohlen
2. Passwort-Hashing wird mit bcrypt implementiert
3. Grundlegende Eingabevalidierung wird durch FormatCheck.py bereitgestellt
4. JWT-Authentifizierungsunterstützung ist über JWTManager.py verfügbar
5. Kein integriertes Authentifizierungs-/Autorisierungssystem

## Eingabevalidierung
Das Framework enthält ein FormatCheck-Utility für die Validierung von Eingabedaten:

1. **E-Mail-Validierung**
   ```python
   FormatCheck.email("user@example.com")
   ```
   - Verwendet Regex-Muster: `^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-z]+$`
   - Validiert:
     - Benutzername-Teil: Buchstaben, Zahlen, Punkte, Unterstriche, Pluszeichen, Bindestriche
     - Domain-Teil: Buchstaben, Zahlen, Bindestriche
     - TLD: Nur Buchstaben
   - Rückgabewert: True wenn gültig, False sonst

2. **Längenvalidierung**
   ```python
   FormatCheck.minimumLength("password", 6)
   ```
   - Prüft, ob String die Mindestlängenanforderung erfüllt
   - Parameter:
     - input_string: zu validierender String
     - min_length: erforderliche Mindestlänge
   - Rückgabewert: True wenn Länge >= min_length, False sonst

3. **Verwendungsbeispiele**
   ```python
   # E-Mail-Validierung
   if not FormatCheck.email(user_email):
       return Response.bad_request("Ungültiges E-Mail-Format")

   # Passwort-Längenprüfung
   if not FormatCheck.minimumLength(password, 6):
       return Response.bad_request("Passwort muss mindestens 6 Zeichen lang sein")

   # Namen-Längenprüfung
   if not FormatCheck.minimumLength(name, 2):
       return Response.bad_request("Name muss mindestens 2 Zeichen lang sein")
   ```

4. **Validierungsregeln**
   - E-Mail: Muss dem Standard-E-Mail-Format mit gültigen Zeichen entsprechen
   - Passwort: Mindestens 6 Zeichen
   - Name: Mindestens 2 Zeichen

## Beispielverwendung

### Neuen Benutzer erstellen
```bash
curl -X POST http://localhost:8001/user \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "password123", "name": "John Doe"}'
```

### Alle Benutzer abrufen
```bash
curl http://localhost:8001/user
```

### Spezifischen Benutzer abrufen
```bash
curl http://localhost:8001/user/1
```

### Benutzer aktualisieren
```bash
curl -X PUT http://localhost:8001/user \
  -H "Content-Type: application/json" \
  -d '{"id": 1, "name": "Aktualisierter Name"}'
```

### Benutzer löschen
```bash
curl -X DELETE http://localhost:8001/user \
  -H "Content-Type: application/json" \
  -d '{"id": 1}'
```

## Entwicklungsrichtlinien

### Neue Controller erstellen
1. Neue Datei im `controller`-Verzeichnis erstellen
2. `IController`-Schnittstelle implementieren
3. Controller-Methoden hinzufügen (get, post, put, destroy)

### Neue Modelle erstellen
1. Neue Datei im `model`-Verzeichnis erstellen
2. `IModel`-Schnittstelle implementieren
3. Entsprechende Tabelle im `table`-Verzeichnis erstellen
4. Datenbankoperationen implementieren

## Einschränkungen
1. Kein integriertes Authentifizierungssystem
2. Begrenzte Fehlerbehandlung
3. Grundlegende Eingabevalidierung
4. Keine Anfragenratenbegrenzung
5. Kein integriertes Logging-System
6. Kein integriertes Caching-Mechanismus

## Best Practices
1. Immer virtuelle Umgebung verwenden
2. Controller schlank halten, Geschäftslogik in Modelle verschieben
3. Eingabedaten vor der Verarbeitung validieren
4. Datenbankfehler angemessen behandeln
5. Geeignete HTTP-Statuscodes in Antworten verwenden

## Fehlerbehebung
1. Wenn Datenbankverbindung fehlschlägt:
   - Prüfen Sie, ob die Datenbankdatei existiert
   - Überprüfen Sie die Datenbankanmeldedaten (bei MySQL)
   - Überprüfen Sie die Datenbankberechtigungen

2. Wenn Server nicht startet:
   - Prüfen Sie, ob Port 8001 verfügbar ist
   - Überprüfen Sie, ob alle Abhängigkeiten installiert sind
   - Überprüfen Sie die Python-Versionskompatibilität

3. Wenn Anfragen fehlschlagen:
   - Überprüfen Sie das Anfrageformat
   - Überprüfen Sie die Eingabevalidierungsregeln
   - Stellen Sie sicher, dass die richtige HTTP-Methode verwendet wird

## HTTP-Anfragen-Lebenszyklus

### Allgemeiner Anfragenfluss
```mermaid
graph TD
    A[Client-Anfrage] --> B[HttpHandler]
    B --> C{Anfragenvalidierung}
    C -->|Gültig| D[Route zum Controller]
    C -->|Ungültig| E[400 Fehler zurückgeben]
    D --> F[Controller-Methode ausführen]
    F --> G[Modell-Operationen verarbeiten]
    G --> H[Datenbankoperationen]
    H --> I[Antwort formatieren]
    I --> J[Antwort an Client senden]
```

### Benutzererstellung-Fluss
```mermaid
sequenceDiagram
    participant Client
    participant HttpHandler
    participant UserController
    participant UserModel
    participant Database

    Client->>HttpHandler: POST /user
    Note over HttpHandler: Anfrage validieren
    HttpHandler->>UserController: Route zum Controller
    UserController->>UserModel: create()
    UserModel->>UserModel: E-Mail validieren
    UserModel->>UserModel: Passwort hashen
    UserModel->>Database: INSERT Abfrage
    Database-->>UserModel: Erfolg
    UserModel-->>UserController: Erfolg
    UserController-->>HttpHandler: 200 OK
    HttpHandler-->>Client: Antwort
```

### Fehlerbehandlungsfluss
```mermaid
graph TD
    A[Fehler tritt auf] --> B{Fehlertyp}
    B -->|Validierung| C[Validierungsfehler formatieren]
    B -->|Datenbank| D[Datenbankfehler formatieren]
    B -->|Nicht gefunden| E[404 Fehler formatieren]
    C --> F[Fehler-Statuscode setzen]
    D --> F
    E --> F
    F --> G[Fehlerantwort senden]
```

### Komponenteninteraktion
```mermaid
graph LR
    A[HttpHandler] -->|Routet| B[Controller]
    B -->|Verwendet| C[Modelle]
    C -->|Interagiert| D[Datenbank]
    B -->|Implementiert| E[IController Schnittstelle]
    C -->|Implementiert| F[IModel Schnittstelle]
    D -->|Verwaltet von| G[DBConnection]
    D -->|Schema von| H[DBMigrate]
```

## Antwortverarbeitung

### Response-Klasse (helper/Response.py)
Die `Response`-Klasse bietet eine standardisierte Möglichkeit zur Formatierung von API-Antworten. Sie gewährleistet eine konsistente Antwortstruktur über alle Endpunkte hinweg.

#### Antwortstruktur
```json
{
    "status_code": 200,      // HTTP-Statuscode
    "status": "success",     // "success" oder "error"
    "message": {}            // Antwortdaten oder Fehlermeldung
}
```

#### Verfügbare Methoden

1. **Basis-Antwortmethode**
   ```python
   @staticmethod
   def response(status_code, data)
   ```
   - Erstellt ein standardisiertes Antwortobjekt
   - Bestimmt automatisch den Status basierend auf dem Statuscode
   - Statuscodes >= 400 werden als "error" markiert
   - Statuscodes < 400 werden als "success" markiert

2. **Erfolgsantwort**
   ```python
   @staticmethod
   def success(data)
   ```
   - Gibt eine 200 OK Antwort zurück
   - Wird für erfolgreiche Operationen verwendet
   - Beispiel:
     ```python
     Response.success({"user": "created"})
     # Gibt zurück:
     # {
     #     "status_code": 200,
     #     "status": "success",
     #     "message": {"user": "created"}
     # }
     ```

3. **Ungültige Anfrage-Antwort**
   ```python
   @staticmethod
   def bad_request(message)
   ```
   - Gibt eine 400 Bad Request Antwort zurück
   - Wird für Validierungsfehler oder ungültige Eingaben verwendet
   - Beispiel:
     ```python
     Response.bad_request("Ungültiges E-Mail-Format")
     # Gibt zurück:
     # {
     #     "status_code": 400,
     #     "status": "error",
     #     "message": "Ungültiges E-Mail-Format"
     # }
     ```

4. **Nicht autorisierte Antwort**
   ```python
   @staticmethod
   def unauthorized(message)
   ```
   - Gibt eine 401 Unauthorized Antwort zurück
   - Wird für Authentifizierungsfehler verwendet
   - Beispiel:
     ```python
     Response.unauthorized("Ungültige Anmeldedaten")
     # Gibt zurück:
     # {
     #     "status_code": 401,
     #     "status": "error",
     #     "message": "Ungültige Anmeldedaten"
     # }
     ```

5. **Interner Fehler-Antwort**
   ```python
   @staticmethod
   def internal_error(message)
   ```
   - Gibt eine 500 Internal Server Error Antwort zurück
   - Wird für serverseitige Fehler verwendet
   - Beispiel:
     ```python
     Response.internal_error("Datenbankverbindung fehlgeschlagen")
     # Gibt zurück:
     # {
     #     "status_code": 500,
     #     "status": "error",
     #     "message": "Datenbankverbindung fehlgeschlagen"
     # }
     ```

#### Verwendungsbeispiele

1. **In Controllern**
   ```python
   def post(self, data):
       try:
           # Daten verarbeiten
           return Response.success({"message": "Erfolgreich erstellt"})
       except ValidationError:
           return Response.bad_request("Ungültige Eingabe")
       except Exception:
           return Response.internal_error("Serverfehler")
   ```

2. **Fehlerbehandlung**
   ```python
   if not user_data:
       return Response.bad_request("Benutzer nicht gefunden")
   ```

3. **Erfolgsantwort**
   ```python
   return Response.success({
       "user": {
           "id": 1,
           "name": "John Doe",
           "email": "john@example.com"
       }
   })
   ```

#### Best Practices
1. Immer die Response-Klasse für konsistente API-Antworten verwenden
2. Geeignete Statuscodes für verschiedene Szenarien verwenden
3. Klare und beschreibende Fehlermeldungen bereitstellen
4. Konsistente Antwortdatenstruktur beibehalten
5. success() für erfolgreiche Operationen verwenden
6. Spezifische Fehlermethoden (bad_request, unauthorized, internal_error) für verschiedene Fehlertypen verwenden

## Authentifizierung

### JWT-Authentifizierung (helper/JWTManager.py)
Das Framework enthält JWT (JSON Web Token) Unterstützung für die Authentifizierung:

1. **Token-Erstellung**
   ```python
   jwt_manager = JWTManager()
   token = jwt_manager.create({"user_id": 123, "role": "admin"})
   ```
   - Erstellt JWT-Token mit Ablaufzeit
   - Standardablaufzeit: 60 Minuten
   - Verwendet HS256-Algorithmus
   - Fügt automatisch Ablaufzeitstempel hinzu

2. **Token-Überprüfung**
   ```python
   decoded = jwt_manager.verify(token)
   if decoded:
       # Token ist gültig
       user_data = decoded
   else:
       # Token ist ungültig oder abgelaufen
   ```
   - Überprüft Token-Gültigkeit
   - Prüft Ablaufzeit
   - Gibt dekodierte Nutzdaten oder False zurück

3. **Konfiguration**
   ```python
   self.__secret_key = "ihr-geheimer-schlüssel"
   self.__algorithm = "HS256"
   self.__expiration_minutes = 60
   ```
   - Konfigurierbarer geheimer Schlüssel
   - Konfigurierbarer Algorithmus
   - Konfigurierbare Ablaufzeit

4. **Verwendungsbeispiel**
   ```python
   # Token erstellen
   jwt_manager = JWTManager()
   user_data = {"user_id": 123, "role": "admin"}
   token = jwt_manager.create(user_data)

   # Token überprüfen
   decoded = jwt_manager.verify(token)
   if decoded:
       print("Dekodierte Daten:", decoded)
   ```

5. **Sicherheitshinweise**
   - Geheimer Schlüssel sollte in Umgebungsvariablen gespeichert werden
   - Token laufen nach 60 Minuten standardmäßig ab
   - Verwendet branchenüblichen HS256-Algorithmus
   - Behandelt Token-Ablauf ordnungsgemäß 

## Postman-Sammlung
Das Framework enthält eine Postman-Sammlung (`Micro Python.postman_collection.json`) mit vorkonfigurierten Anfragen für die Beispiel-API-Endpunkte. Dies erleichtert das Testen der API ohne curl-Befehle schreiben zu müssen.

### Sammlung importieren
1. Öffnen Sie Postman
2. Klicken Sie auf die "Import"-Schaltfläche in der oberen linken Ecke
3. Wählen Sie den "File"-Tab
4. Klicken Sie auf "Upload Files" und wählen Sie `Micro Python.postman_collection.json`
5. Klicken Sie auf "Import"

### Sammlung verwenden
Die Sammlung enthält folgende vorkonfigurierte Anfragen:

#### Auto-Endpunkte
- **GET /auto**: Liste aller Autos
- **POST /auto**: Neues Auto erstellen
  - Body: JSON mit Feldern `name` und `ps`
- **PUT /auto**: Auto aktualisieren
  - Body: JSON mit Feldern `id`, `name` und `ps`
- **DELETE /auto**: Auto löschen
  - Body: JSON mit Feld `id`

### Sammlungsfunktionen
- Vorkonfigurierte Header (Content-Type: application/json)
- Beispielanfrage-Bodies
- Organisierte Ordnerstruktur
- Umgebungsvariablen-Unterstützung
- Dokumentation für jeden Endpunkt

### Postman-Tipps
1. **Umgebung einrichten**
   - Neue Umgebung erstellen
   - Variable `base_url` mit Wert `http://localhost:8001` hinzufügen
   - `{{base_url}}` in Anfrage-URLs verwenden

2. **Test-Workflow**
   - Mit GET-Anfragen beginnen, um Daten anzuzeigen
   - POST für neue Einträge verwenden
   - PUT für bestehende Einträge verwenden
   - DELETE für Einträge entfernen

3. **Antwortverarbeitung**
   - Statuscodes überprüfen
   - Formatierte JSON-Antworten anzeigen
   - Postman-Testskripte für Automatisierung verwenden

## KI-Assistent-Funktionen
Das Framework enthält einen intelligenten Code-Assistenten (`CodeAssistant.py`), der bei der Code-Generierung und -Analyse hilft. Der Assistent kann über `ai_assistant_usage.py` verwendet werden.

> ⚠️ **Wichtiger Hinweis für Anfänger**: Der KI-Assistent ist ein Entwicklungswerkzeug, und generierter Code sollte vor der Verwendung sorgfältig überprüft werden. Immer:
> - Generierten Code gründlich testen
> - Alle Importe validieren
> - Methodennamen mit Framework-Konventionen abgleichen
> - Fehlerbehandlung mit Framework-Mustern abgleichen
> - Antwortformate validieren

### Hauptfunktionen
1. **Code-Analyse**
   - Projektstruktur- und Musteranalyse
   - Komponentenbeziehungen identifizieren
   - VS Code-Snippets basierend auf Mustern generieren
   - Kontextbasierte Code-Vorschläge

2. **CRUD-Endpunkt-Generierung**
   - Automatische Generierung vollständiger CRUD-Endpunkte
   - Controller-, Model- und Tabellendateien erstellen
   - Konsistente Muster über Codebase hinweg
   - Verwendungsbeispiel:
     ```python
     # CRUD-Endpunkte für neue Ressource generieren
     product_endpoints = assistant.generate_crud_endpoints("Product")
     ```

3. **Code-Vorschläge**
   - Kontextbasierte Code-Vorschläge
   - Verbesserungsvorschläge basierend auf Mustern
   - Verwendungsbeispiel:
     ```python
     # Vorschläge für Controller-Methode erhalten
     suggestions = assistant.suggest_code(context, "UserController.py")
     ```

4. **Dokumentationsgenerierung**
   - Dokumentation basierend auf Code-Mustern generieren
   - API-Dokumentation erstellen
   - Verwendungsbeispiel:
     ```python
     # Dokumentation für Controller generieren
     controller_docs = assistant.generate_documentation("controller")
     ```

## Eine Nachricht vom Entwickler

Vielen Dank, dass Sie sich die Zeit genommen haben, dieses Bildungs-Framework zu erkunden! Ich habe dieses Projekt entwickelt, um Anfängern das Verständnis der grundlegenden Konzepte der Webentwicklung und Python-Programmierung zu erleichtern.

Ich hoffe, dieses Framework dient als hilfreicher Schritt in Ihrer Lernreise. Denken Sie daran, dass jeder Experte einmal ein Anfänger war und dass der Schlüssel zum Beherrschen der Programmierung in kontinuierlicher Praxis und Neugier liegt.

Alles Gute für Ihre Lernreise!

Ali Khorsandfard
Entwickler und Pädagoge
