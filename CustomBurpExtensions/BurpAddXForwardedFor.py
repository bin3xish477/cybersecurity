from burp import IBurpExtender
from burp import ISessionHandlingAction

class BurpExtender(IBurpExtender, ISessionHandlingAction):

    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        callbacks.setExtensionName("Add X-Forwarded-For Header")
        callbacks.registerSessionHandlingAction(self)
        return

    def getActionName(self):
        return None

    def performAction(self, currentRequest, macroItems):
        requestInfo = self._helpers.analyzeRequest(currentRequest)
        headers = requestInfo.getHeaders()
        msgBody = currentRequest.getRequest()[requestInfo.getBodyOffset():]
        headers.add("X-Forwarded-For: 192.168.4.28")
        message = self._helpers.buildHttpMessage(headers, msgBody)
        print(self._helpers.bytesToString(message))
        currentRequest.setRequest(message)
        return

