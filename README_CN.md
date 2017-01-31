##TurboPydDNS

又一个支持多个ddns服务的客户端 **只支持Python3** (故意的)

本客户端正在开发中,不保证master分支一定能够work。
建议使用TAG标定的版本号客户端

用法
----
```bash
python3 turbo_py_ddns_client.py pubyun --username=xx --password=xxx --ddnsname=xxx
```

TODO
----
- [x] 支持 `PUBYUN（公云）` 
- [ ] 支持 `DuckDNS` 
- [ ] 全局自动检测IP变化更新DNS
  
License
-------
Licensed under the Apache License, Version 2.0