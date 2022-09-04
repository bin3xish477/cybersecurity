# AWS Security Best Practices

### Disable Default Execution Endpoint for API Gateway when Using Custom Domain

- most of the time, you are configuring API gateway to work with a custom domain, and leaving the default execute api endpoint enabled may allow attackers to bypass the security configurations you implemented that apply to requests to your custom domain and not the default api execute api endpoint.
- this also ensures we are reducing the APIs attack surface

```console
aws apigateway update-rest-api --rest-api-id "<api-id>" \
  --patch-operations "op=replace,path=/disableExecuteApiEndpoint,value='True'" \
  --profile $PROFILE
```

### High-level Security Best Practices Diagram for Basic Serverless Model

![image](https://user-images.githubusercontent.com/44281620/188323412-ff3b3de0-4cc7-42ca-8d3d-dac94a55cbe4.png)

Reference: https://www.youtube.com/watch?v=nEaAuX4O9TU
