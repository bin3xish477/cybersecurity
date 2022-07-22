/* Can you spot the vulnerability?? */

public String addNewSession() {
  this.lock.lock()
  final byte[] bytes = new byte[16];
  boolean isJSessionIdFoundInCache = null;
  String newJSessionId = null;

  try {
    do {
      PBPSessionManager.random.nextBytes(bytes);
      newJSessionId = Hex.encodeHexString(bytes);
      isJSessionIdFoundInCache = (this.jsessionCache.get(newJSessionId) != null);
    } while (isJSessionIdFoundInCache);

    final JSession jSession = new JSession(newJSessionId);
    this.jsessionCache.put(newJSessionId, jSession);
    return newJSessionId;

  } finally {
    this.lock.unlock()
  }
}

