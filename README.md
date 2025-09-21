# EPA Converter

Konvertiert einen EPA String nach einem bestimmten Format.
Die CSV muss folgende Spalten beinhalten: **"Katalog"**, **"CODE"**, **"Klarname"**.

Alle weiteren Spalten werden entfernt. 

### Installation
Das Tool wird direkt als *.exe gestartet und kann ohne weitere Installationen verwendet werden.

### Verwendung
1. Öffne die Datei `epa_converter.exe`.
2. Wähle eine CSV-Datei aus
3. Wähle ein Katalog aus der Dropdownliste

Der Code baut sich zusammen aus den Werten aus den Spalten 

```
*katalog*+*CODE*+*Klarname*,XDS_CLASS_CODE#XDS_CONTENT_TYPE_CODE#XDS_FORMAT_CODE#COMPANYTYPE_20#XDS_TYPE_CODE#XDS_PRACTICE_SETTING_CODE#XDS_CONFIDENTIALY_CODE"
```

Beispiel:
```
'XDS_CLASS_CODE,RESEARCH,Forschung,XDS_CLASS_CODE#XDS_CONTENT_TYPE_CODE#XDS_FORMAT_CODE#COMPANYTYPE_20#XDS_TYPE_CODE#XDS_PRACTICE_SETTING_CODE#XDS_CONFIDENTIALY_CODE'
```