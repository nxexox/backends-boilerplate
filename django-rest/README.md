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
** Внимание, make install заново расшифровывает env. 
Потому перед make install, лучше настроить env и зашифровать. 
Иначе они перетруться. **

** В .env обязательно прописать `DJANGO_SECRET_KEY`. **
