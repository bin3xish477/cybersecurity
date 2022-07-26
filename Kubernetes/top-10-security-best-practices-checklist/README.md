# Top 10 Kubernetes Security Best Practices Checklist

- [ ] Image Scanning
  - perform image scanning to detect malicious images attempting to infiltrate deployments
  - use static security and vulnerability scanning tools such as `docker scan` which leverages Snyk, Clair, Anchore, Qualys, etc
- [ ] Avoid Using Root User
  - users with the least amount of privileges required to perform a function should be created to execute containerized applications
  - helps prevent against common container breakout techniques
  - `RUN groupadd -r app && useradd -g app appuser`
- [ ] Users & Permissions with Role-based Access Controls (RBAC)
- [ ] Use Network Policies
- [ ] Encrypt Communication
- [ ] Secure Secrets
- [ ] Secure etcd
- [ ] Automated Backup & Restore
- [ ] Configure Security Policies
- [ ] Disaster Recovery

#### References

- [TechWorld with Nana Kubernetes Security Best Practices Video](https://www.youtube.com/watch?v=oBf5lrmquYI)
