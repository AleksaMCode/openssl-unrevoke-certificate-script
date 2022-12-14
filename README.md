<img width="150" align="right" title="Python icon" src="https://www.internetsociety.org/wp-content/uploads/2016/09/OpenSSL.png" alt_text="OPENSSL"></img>
# OPENSSL Unrevoke Certificate
<p align="justify">Did you ever want to unrevoke certificate you have previously revoked using <b>openessl</b> without manually changing <i>index.txt</i> file? I know I have, especially when I was first learning to use <b>openssl</b>. Now you can unrevoke certificate simply by executing a python script.</p>

> **_NOTE:_**
> 
> I'm fully aware that once the certificate is on revoked list it should stay there. That's why it's recommended to never revoke cert unless you know it's been compromised. You could make an argument for unrevoking a cert that has been revoke as Certificate Hold.

## Usage
<p align="justify">You need to run a python script with two arguments, name of the CA database, which is <i>index.txt</i> by default, and the serial number of the revoked certificate, i.e.</p>

```bash
$ python3 openssl-unrevoke.py index.txt C1
```
