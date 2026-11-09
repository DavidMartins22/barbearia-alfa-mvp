# Barbearia Alfa Concept - MVP de Agendamento Autônomo

Este repositório contém o código-fonte e a arquitetura técnica do Produto Mínimo Viável (MVP) desenvolvido para a **Barbearia Alfa Concept**, localizada no bairro Jardim das Flores. O sistema substitui o modelo arcaico de agendamento baseado em cadernos de papel e mensagens manuais de WhatsApp por uma aplicação web responsiva leve e livre de fricções ("zero-friction").

## 🎯 Alinhamento com a Agenda 2030 (ONU)
O projeto está diretamente conectado ao **ODS 8 — Trabalho Decente e Crescimento Econômico**, atendendo especificamente à **Meta 8.2**: *Aumentar os níveis de produtividade econômica por meio da diversificação, modernização tecnológica e inovação*. 
A automação elimina a ineficiência logística, impede colisões de horários e mitiga o absenteísmo de clientes, garantindo previsibilidade financeira e otimização do tempo de trabalho dos barbeiros autônomos da comunidade.

## 🛠️ Stack Tecnológica de Engenharia
*   **Padrão Principal:** Python 3.12
*   **Framework Web:** FastAPI (Roteamento assíncrono e validação via Pydantic)
*   **Mapeamento de Dados:** SQLModel (ORM coeso com consultas parametrizadas contra SQL Injection)
*   **Persistência Relacional:** PostgreSQL (Estrutura relacional estável hospedada no Supabase)
*   **Segurança e Criptografia:** Passlib com algoritmo robusto BCrypt (Geração de hash não-reversível para senhas)
*   **Interface Gráfica (View):** Vanilla Web (HTML5/CSS3/JavaScript puros) projetada com *Mobile-First*, targets de toque de **48x48dp** e alto contraste (WCAG 2.1 AA)

## 🧬 Estrutura do Projeto
```text
├── .github/workflows/ci.yml   # Pipeline de Integração Contínua (GitHub Actions)
├── app/
│   ├── database.py            # Configuração e injeção de sessão do banco
│   ├── main.py                # Controlador FastAPI e regras de colisão de horários
│   ├── models.py              # Modelagem de entidades e restrições únicas
│   ├── security.py            # Hashing robusto de senhas dos profissionais
│   └── templates/
│       └── index.html         # Front-end Vanilla Web responsivo e acessível
└── tests/
    ├── test_integration.py    # Teste automatizado que comprova o bloqueio de colisão
    └── test_security.py       # Testes unitários da camada de criptografia
```

## 🧪 Como Executar os Testes Automatizados Localmente

1. Certifique-se de ter o Python 3.12 instalado.
2. Instale as dependências listadas no manifesto:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o conjunto de testes automatizados unitários e de integração via terminal:
   ```bash
   pytest tests/ -v
   ```

## 🔄 Esteira de DevOps (CI)
O repositório está configurado com um pipeline automatizado de **Integração Contínua (CI)** via **GitHub Actions**. A cada commit ou Pull Request enviado para as ramificações de desenvolvimento, o pipeline monta o ambiente virtual Ubuntu, instala as dependências do `requirements.txt` e dispara a bateria de testes de forma autônoma para garantir a integridade das regras de negócio do MVP antes de qualquer deploy.
