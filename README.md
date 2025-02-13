# 📌 Sistema de Clínica Médica - Django

Este é um sistema de gerenciamento de usuários para uma clínica médica, desenvolvido em **Django**. Ele permite a criação e gerenciamento de usuários com diferentes grupos, como **Médicos** e **Funcionários**, além de contar com um sistema de autenticação personalizado.

---

## 🚀 Tecnologias Utilizadas
- **Python 3.12+**
- **Django**
- **SQLite (padrão, pode ser alterado para PostgreSQL, MySQL, etc.)**

---

## 📦 Configuração do Projeto

### 1️⃣ **Clonar o Repositório**
```sh
 git clone https://github.com/Arcane6/senac.git
 cd seu-repositorio
```

### 2️⃣ **Criar e Ativar o Ambiente Virtual**
```sh
python -m venv venv
# Ativar no Windows
venv\Scripts\activate
# Ativar no macOS/Linux
source venv/bin/activate
```

### 3️⃣ **Instalar Dependências**
```sh
pip install -r requirements.txt
```

### 4️⃣ **Rodar as Migrações**
```sh
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ **Criar o Superusuário**
```sh
python manage.py createsuperuser --email admin@email.com --name "Administrador"
```
🚨 **Será solicitado que você informe uma matrícula manualmente.**

### 6️⃣ **Rodar o Servidor**
```sh
python manage.py runserver
```
Acesse **http://127.0.0.1:8000/** no navegador.

---

## 👥 Sistema de Usuários

### **Grupos de Usuários**
O sistema utiliza os grupos padrão do Django para diferenciar os usuários:
- **Médico** → A matrícula começa com "M" e é gerada automaticamente.
- **Funcionário** → A matrícula começa com "F" e é gerada automaticamente.

### **Autenticação Personalizada**
- O **campo de login é a matrícula** do usuário.
- A matrícula é gerada automaticamente ao criar um usuário normal.
- Superusuários devem inserir a matrícula manualmente ao serem criados.

---

## ⚙️ Personalização
Se quiser trocar o banco de dados, edite o arquivo **settings.py**:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Troque para 'mysql' ou outro banco
        'NAME': 'seu_banco',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
Após editar, rode:
```sh
python manage.py migrate
```

---

## 🎨 Personalizando o Django Admin com `django-admin-interface`

Para melhorar a aparência do Django Admin e torná-lo mais moderno, utilizamos o **django-admin-interface**, que permite customizar cores, logos e layout diretamente pelo painel administrativo.

### 🔄 Instalação
```sh
pip install django-admin-interface
```

Adicione ao `settings.py`:
```python
INSTALLED_APPS = [
    "admin_interface",
    "colorfield",  # Dependência do django-admin-interface
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
```

Aplique as migrações:
```sh
python manage.py migrate
```

No `settings.py`, permita o carregamento correto dos estilos:
```python
X_FRAME_OPTIONS = "SAMEORIGIN"
SILENCED_SYSTEM_CHECKS = ["security.W019"]
```

### 🔧 Customização via Django Admin

1. Acesse **Admin > Interface do Admin**
2. Edite o tema padrão e personalize:
   - **Cores** (background, botões, texto)
   - **Logo personalizada**
   - **Fonte personalizada**
   - **Modo escuro**

Com isso, o Django Admin fica com um visual mais moderno e intuitivo!

🔄 Reinicie o servidor e veja as alterações:
```sh
python manage.py runserver
```

---

