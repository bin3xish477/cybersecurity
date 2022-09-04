# AWS Security Best Practices

### Disable Default Execution Endpoint for API Gateway when Using Custom Domain

- most of the time, you are configuring API gateway to work with a custom domain, and leaving the default execute api endpoint enabled may allow attackers to bypass the security configurations you implemented that apply to requests to your custom domain and not the default api execute api endpoint.
- this also ensures we are reducing the APIs attack surface

```console
aws apigateway update-rest-api --rest-api-id "<api-id>" \
  --patch-operations "op=replace,path=/disableExecuteApiEndpoint,value='True'" \
  --profile $PROFILE
```
