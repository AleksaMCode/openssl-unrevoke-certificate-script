<img width="150" align="right" title="Python icon" src="https://www.internetsociety.org/wp-content/uploads/2016/09/OpenSSL.png" alt_text="OPENSSL"></img>
# OPENSSL Unrevoke Certificate
<p align="justify">Did you ever want to unrevoke a certificate you have previously revoked using <b>openessl</b> without manually changing a <i>index.txt</i> file? I know I have, especially when I was first learning to use <b>openssl</b>. Now you can unrevoke the certificate simply by executing a python script.</p>

> **_NOTE:_**
> 
> I'm fully aware that once the certificate is on the revoked list it should stay there. That's why it's recommended to never revoke it unless you know it's been compromised. You could make an argument for unrevoking the certificate that has been revoked with the revocation reason code <ins>Certificate Hold</ins>.

## Usage
<p align="justify">You need to run the python script with two arguments, a name of the CA database, which is <i>index.txt</i> by default, and a serial number of the revoked certificate, i.e.</p>

```bash
$ python3 openssl-unrevoke.py index.txt C1
```
