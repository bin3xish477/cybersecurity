# Securing XML Parsers from XXE

### Disabling DTDs (External Entities)

Disabling external entities is the safest way to handle untrusted user input that gets passed to an XML parser. All parsers should have a way to disable DTDs.

Disabling or nullifying DTDs for different programming languages:

#### Java

```java
factory.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
```

```java
dbFactory.setFeature("http://xml.org/sax/features/external-general-entities", false);
dbFactory.setFeature("http://xml.org/sax/features/external-parameter-entities", false);
dbFactory.setFeature("http://apache.org/xml/features/nonvalidating/load-external-dtd", false);

dbFactory.setXIncludeAware(false);
dbFactory.setExpandEntityReferences(false);
```

#### C#

```csharp
XmlDocument xmlDoc = new XmlDocument();
xmlDoc.XmlResolver = null;
xmlDoc.LoadXml(OurOutputXMLString);
```

### C/C++

The Enum xmlParserOption from the libxml2 library should not define the following options:

- `XML_PARSE_NOENT`: Expands entities and substitutes them with replacement text
- `XML_PARSE_DTDLOAD`: Loads external DTD

#### Python

Use the [defusedxml](https://pypi.org/project/defusedxml/) package to parse untrusted XML data and prevent potentially malicious XML operations

