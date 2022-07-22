/* Can you spot the vulnerability?? */

public Document parseXMLInput(String xml) throws ParsingException, IOException {
  return new Document(xml); // `Document` defined below
}

/* Document definition */
public Document(String xml) throws ParsingException, IOException {
  SAXBuilder sax = initializeSAXBuilder();

  try {
    this.jdomDocument = sax.build(new StringReader(xml));
    initializeStringOutputter();
  } catch (JDOMException e) {
    throw new ParsingException(e);
  }
}
