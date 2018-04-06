# Boilerplate for django rest project and dockers.

Переменые окружения находяться в `configs/environments/` в зашифрованном виде.
Зашифровка/Расшифровка находиться в makefile `encrypt/decrypt` соотвественно.
Ключи:
* development - development
* stage - stage
* production - production
Пример:
```bash
$ export CRYPTO_SECRET_KEY=stage
$ make decrypt environment=stage
```

## Install.
```bash
$ make install
```
